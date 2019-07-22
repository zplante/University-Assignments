import csv
import re
import os
import string
from os.path import isfile, join
from qa_engine.base import QABase
from qa_engine.score_answers import main as score_answers
import nltk, operator
from nltk.corpus import wordnet as wn
from word2vec_extractor import Word2vecExtractor
from nltk import WordNetLemmatizer
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity


"""
GLOBALS
"""


STOPWORDS = set(nltk.corpus.stopwords.words("english"))
glove_w2v_file = "data/glove-w2v.txt"
DATA_DIR = "./wordnet"
W2vecextractor = Word2vecExtractor(glove_w2v_file)
lmtzr = WordNetLemmatizer()


"""
UTILITY FUNCTIONS
"""


# The standard NLTK pipeline for POS tagging a document
def get_sentences(text):

    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    return sentences


# return a list of the characters in the story given the story text
def get_characters_in_story(text):
    sentences = get_sentences(text)  # pos tagged sentences
    characters = []

    for sent in sentences:
        for tup in sent:
            if tup[1] == "NNP" and text.count(tup[0]) > 1:
                characters.append(tup[0])

    characters = set(characters)
    answer = "a " + " and a ".join(character.lower() for character in characters)

    return answer


# Replace pronouns in story text with the noun subject that pronoun is referring to
def prp_to_nns(best_sentence_tree):
    subject_word = None
    subject_tag = None
    flg = 0

    for word, tag in best_sentence_tree:

        if "NNP" in tag and flg == 0:
            subject_word = word
            subject_tag = tag
            flg = 1

        if "PRP" in tag and subject_word is not None and subject_tag is not None:
            best_sentence_tree = [((w.replace(word, subject_word)), (t.replace(tag, subject_tag))) for w, t in best_sentence_tree]
            return best_sentence_tree

    return best_sentence_tree


def get_story_text(qtype, story):

    if qtype == "sch":
        stext = story["sch"]

    else:
        stext = story["text"]

    return stext


def get_question_text(question):

    qtext = question["text"]

    return qtext


"""
CHUNKING_DEMO
"""


GRAMMAR = """
                N: {<PRP>|<NN.*>}
                V: {<V.*>}
                ADJ: {<JJ.*>}
                NP: {<DT>? <ADJ>* <N>}
                PP: {<IN> <NP>}
                VP: {<TO>? <V> (<NP>|<PP>)*}
            """

LOC_PP = set(["in", "on", "at", "under", "above", "to", "along", "around"])


def pp_filter(subtree):
    return subtree.label() == "PP"


def is_location(prep):
    return prep[0] in LOC_PP


def find_locations(tree):
    # Starting at the root of the tree
    # Traverse each node and get the subtree underneath it
    # Filter out any subtrees who's label is not a PP
    # Then check to see if the first child (it must be a preposition) is in
    # our set of locative markers
    # If it is then add it to our list of candidate locations

    # How do we modify this to return only the NP: add [1] to subtree!
    # How can we make this function more robust?
    # Make sure the crow/subj is to the left
    locations = []

    for subtree in tree.subtrees(filter=pp_filter):

        if is_location(subtree[0]):
            locations.append(subtree)

    return locations


def find_where_candidates(crow_sentence, chunker):

    # print(crow_sentence)
    # print("\n\n")

    tree = chunker.parse(crow_sentence)

    # print(tree)

    locations = find_locations(tree)

    return locations


"""
DEPENDENCY_DEMO
"""


def find_main(graph):
    for node in graph.nodes.values():
        if node['rel'] == 'root':
            return node
    return None


def find_phrase(qbow, sent):
    tokens = nltk.word_tokenize(sent)

    # Travel from the end to begin.
    for i in range(len(tokens) - 1, 0, -1):
        word = tokens[i]
        # If find a word that match the question,
        # return the phrase that behind that word.
        # For example, "lion" occur in the question,
        # So we will return "want to eat the bull" which originally might look like this "... the lion want to eat the bull"
        if word in qbow:
            return " ".join(tokens[i+1:])


def find_node(word, graph):
    for node in graph.nodes.values():
        if node["word"] == word:
            return node
    return None


def get_dependents(node, graph):
    results = []

    for item in node["deps"]:
        address = node["deps"][item][0]
        dep = graph.nodes[address]
        results.append(dep)
        results = results + get_dependents(dep, graph)

    return results


def find_answer(qgraph, sgraph):
    qmain = find_main(qgraph)
    qword = qmain["word"]
    # print(qword)
    snode = find_node(qword, sgraph)

    for node in sgraph.nodes.values():
        if snode is not None:
            if node.get('head', None) == snode["address"]:
                if node['rel'] == "nmod":
                    deps = get_dependents(node, sgraph)
                    deps = sorted(deps + [node], key=operator.itemgetter("address"))

                    return " ".join(dep["word"] for dep in deps)
    return None


"""
CONSTITUENCY_DEMO
"""


def find_pattern(qtext):
    qtype = qtext.split(" ")[0].lower()
    qtext = qtext.lower()

    # print(qtext)
    # print("\n\n")
    # print(stext)
    # print("\n\n")

    if "where" in qtype:
        return "(PP)"

    elif "when" in qtype:
        return "(SBAR)"

    elif "what" in qtype:

        if "did" in qtext:
            return "(VP)"

        elif "was" in qtext:
            return "(PP)"

        else:
            return "(NP)"

    elif "who" in qtype:
        return "(NP)"

    elif "why" in qtype:
        return "(SBAR)"

    elif "how" in qtype:
        return "(ADVP)"

    elif "did" in qtext:
        return "(VP)"

    elif "happened" in qtext:
        return "(VP)"

    else:
        return "(NP)"


# See if our pattern matches the current root of the tree
def matches(pattern, root):

    # Base cases to exit our recursion
    # If both nodes are null we've matched everything so far
    if root is None and pattern is None:
        return root

    # We've matched everything in the pattern we're supposed to (we can ignore the extra
    # nodes in the main tree for now)
    elif pattern is None:
        return root

    # We still have something in our pattern, but there's nothing to match in the tree
    elif root is None:
        return None

    # A node in a tree can either be a string (if it is a leaf) or node
    plabel = pattern if isinstance(pattern, str) else pattern.label()
    rlabel = root if isinstance(root, str) else root.label()

    # If our pattern label is the * then match no matter what
    if plabel == "*":
        return root
    # Otherwise they labels need to match
    elif plabel == rlabel:
        # If there is a match we need to check that all the children match
        # Minor bug (what happens if the pattern has more children than the tree)
        for pchild, rchild in zip(pattern, root):
            match = matches(pchild, rchild)
            if match is None:
                return None
        return root

    return None


def pattern_matcher(pattern, tree):
    for subtree in tree.subtrees():
        node = matches(pattern, subtree)

        if node is not None:
            return node

    return None


"""
BASELINE_DEMO
"""


def get_bow(tagged_tokens, stopwords):
    return set([t[0].lower() for t in tagged_tokens if t[0].lower() not in stopwords])


# qtokens: is a list of pos tagged question tokens with SW removed
# sentences: is a list of pos tagged story sentences
# stopwords is a set of stopwords
def baseline_best(qbow, sentences, stopwords):
    answers = []

    # Collect all the candidate answers
    for sent in sentences:
        # A list of all the word tokens in the sentence
        sbow = get_bow(sent[0], stopwords)

        # Count the # of overlapping words between the Q and the A
        # & is the set intersection operator
        intersect = qbow & sbow
        overlap = len(intersect)

        answers.append((overlap, sent))

    # Sort the results by the first element of the tuple (i.e., the count)
    # Sort answers from smallest to largest by default, so reverse it
    answers = sorted(answers, key=operator.itemgetter(0), reverse=True)

    # Return the best answer and best tree
    best_sentence = answers[0][1][0]
    best_tree = answers[0][1][1]

    return best_sentence, best_tree


def baseline_answer(qbow, subtrees, best_tree, stopwords):
    answers = []

    # Collect all the candidate answers
    for tree in subtrees:
        # A list of all the word tokens in the sentence
        tbow = get_bow(" ".join(best_tree.leaves()), stopwords)

        # Count the # of overlapping words between the Q and the A
        # & is the set intersection operator
        intersect = qbow & tbow
        overlap = len(intersect)

        answers.append((overlap, tree))

    # Sort the results by the first element of the tuple (i.e., the count)
    # Sort answers from smallest to largest by default, so reverse it
    answers = sorted(answers, key=operator.itemgetter(0), reverse=True)

    # Return the answer
    answer = " ".join(" ".join(tup[1].leaves())for tup in answers)

    # print(answer)

    return answer


def baseline_word2vec_verb(sentences, W2vecextractor, q_verb, sgraphs):
    q_feat = W2vecextractor.word2v(q_verb)
    candidate_answers = []

    # print("\nROOT of question: " + str(q_verb) + "\n")

    for i in range(0, len(sentences)):
        sent = sentences[i]
        s_verb = find_main(sgraphs[i])['word']

        # print("\nROOT of sentence: " + str(s_verb) + "\n")

        a_feat = W2vecextractor.word2v(s_verb)

        dist = cosine_similarity([q_feat], [a_feat])
        candidate_answers.append((dist[0], sent))

    answers = sorted(candidate_answers, key=operator.itemgetter(0), reverse=True)

    # Return the best answer and the best graph
    best_answer = answers[0][1][0]
    best_graph = answers[0][1][1]

    return best_answer, best_graph


"""
LEMMATIZATION TRANSFORM FUNCTIONS
"""


# question_sents here is the result of get_sentences(qtext)[0]
# Also calls penn_to_wn on tags within question_sents.
def lemma_question_transform(question_sent):

    question_sent_lemma = [(lmtzr.lemmatize(token, penn_to_wn(tag)), tag) for token, tag in question_sent]

    # question_sent_lemma = [(lmtzr.lemmatize(token, penn_to_wn(tag)), penn_to_wn(tag)) for token, tag in question_sent]

    return question_sent_lemma


# question_sents here is the result of get_sentences(qtext)[0]
# Also calls penn_to_wn on tags within question_sents.
def lemma_story_transform(story_sents):
    story_sents_lemma = []

    for sentence in story_sents:
        story_sent_lemma = [(lmtzr.lemmatize(token, penn_to_wn(tag)), tag) for token, tag in sentence]

        # story_sent_lemma = [(lmtzr.lemmatize(token, penn_to_wn(tag)), penn_to_wn(tag)) for token, tag in sentence]

        story_sents_lemma.append(story_sent_lemma)

    return story_sents_lemma


"""
WORDNET_DEMO
"""


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


# Part-of-speech conversion from penn tree-bank to wordnet.
def penn_to_wn(tag):

    if is_adjective(tag):
        return wn.ADJ

    elif is_noun(tag):
        return wn.NOUN

    elif is_adverb(tag):
        return wn.ADV

    elif is_verb(tag):
        return wn.VERB

    return 'n'


# Called by get_wordnet_ids to retrieve the wordnet folder and files through relative path
def load_wordnet_ids(filename):
    file = open(filename, 'r')

    if "noun" in filename:
        type = "noun"

    else:
        type = "verb"

    csvreader = csv.DictReader(file, delimiter=",", quotechar='"')
    word_ids = defaultdict()

    for line in csvreader:
        word_ids[line['synset_id']] = {'synset_offset': line['synset_offset'], 'story_'+type: line['story_'+type], 'stories': line['stories']}

    return word_ids


# File retrieval using relative pathing (expected wordnet folder)
def get_wordnet_ids():
    wordnet_path = os.path.dirname(os.path.abspath(__file__)) + "/wordnet"
    noun_ids = None
    verb_ids = None

    if os.path.isdir(wordnet_path):
        for file in os.listdir(wordnet_path):
            file = join(wordnet_path, file)

            if os.path.isfile(file):

                # print(join(wordnet_path, file))

                if "nouns" in file:
                    noun_ids = load_wordnet_ids(file)

                elif "verbs" in file:
                    verb_ids = load_wordnet_ids(file)
    else:
        print("Folder missing:\n\"wordnet\"\n")

    return noun_ids, verb_ids


# Question sentence reconstruction
def wordnet_replacement(question_sent):
    noun_ids, verb_ids = get_wordnet_ids()

    if noun_ids is not None and verb_ids is not None:
        for word, tag in question_sent:

            # Check if word in original question sentence is either a noun or a verb
            if tag.startswith("N") or tag.startswith("V") and word not in STOPWORDS:

                # Word ids are those that she gave in the files
                word_ids = None

                if "N" in tag[0]:
                    word_ids = noun_ids

                elif "V" in tag[0]:
                    word_ids = verb_ids

                # From the original question sentence
                word_synsets = wn.synsets(word)

                # print("WORD_SYNSETS:\n")
                # print(word_synsets)
                # print("\n\n")

                if len(word_synsets) > 0:
                    for synset in word_synsets:

                        """
                        SYNONYM REPLACEMENT
                        """

                        # Checking if synonym is in wordnet
                        if synset.name() in word_ids:
                            question_sent = [(w.replace(word, synset.name()[0:synset.name().index(".")]), t) for w, t in question_sent]

                        """
                        HYPONYM REPLACEMENT
                        """

                        # Checking for hyponyms
                        word_hypo = synset.hyponyms()
                        for hypo in word_hypo:
                            if hypo.name() in word_ids:
                                question_sent = [(w.replace(word, hypo.name()[0:synset.name().index(".")]), t) for w, t in question_sent]

                        """
                        HYPERNYM REPLACEMENT
                        """

                        # Checking for hypernyms
                        word_hyper = synset.hypernyms()
                        for hyper in word_hyper:
                            if hyper.name() in word_ids:
                                question_sent = [(w.replace(word, hyper.name()[0:hyper.name().index(".")]), t) for w, t in question_sent]

                # If there are no synsets, then return the original question sentence.
                else:
                    return question_sent

        return question_sent


"""
SELECTION FUNCTIONS
"""


# Given a list of sentences, returns the sentence that appears the most if there is one
def find_best_sentence(stext, qtype, qtext, story, question):

    if "|" in qtype:
        qtype = "story"

    # A list representing the story text.
    # This list embeds lists where each list represents a sentence.
    # Each element in each list is a tuple (word, part-of-speech)
    story_sents = get_sentences(stext)

    # A list representing the question sentence.
    # Each element in this sentence is a tuple (word, part-of-speech)
    question_sent = get_sentences(qtext)[0]

    if "Hard" in question["difficulty"]:
        question_sent = wordnet_replacement(question_sent)

        # print(question_sent)
        # print("\n\n")

    """
    LEMMATIZATION PROCESS
    """

    # Here we lemmatize the story sentences (which can call penn_to_wn)
    story_sents_lemma = lemma_story_transform(story_sents)

    # Here we lemmatize the question sentence (which can call penn_to_wn)
    question_sent_lemma = lemma_question_transform(question_sent)

    """
    CONSTITUENCY IMPLEMENTATION
    """

    story_trees = []
    for tree in story[qtype + "_par"]:
        story_trees.append(tree)

    qbow = get_bow(question_sent_lemma, STOPWORDS)
    tree_sentences = list(zip(story_sents_lemma, story_trees))

    # best_sentence_tree is the best sentence retrieved from constituency parses (tree_sentences)
    best_sentence_tree, best_tree = baseline_best(qbow, tree_sentences, STOPWORDS)

    """
    DEPENDENCY IMPLEMENTATION
    """

    sgraph = []
    for dependent in story[qtype + "_dep"]:
        # nodes = list(dependent.nodes.values())
        sgraph.append(dependent)

    qgraph = question["dep"]
    q_verb = find_main(qgraph)['word']
    graph_sentences = list(zip(story_sents_lemma, sgraph))

    # best_sentence_graph is the best sentence retrieved from dependency parses (graph_sentences)
    best_sentence_graph, best_graph = baseline_word2vec_verb(graph_sentences, W2vecextractor, q_verb, story[qtype + "_dep"])

    return best_sentence_tree, best_tree, best_sentence_graph, best_graph


def get_answer(question, story):
    """
    :param question: dict
    :param story: dict
    :return: str

    question is a dictionary with keys:
        dep -- A list of dependency graphs for the question sentence.
        par -- A list of constituency parses for the question sentence.
        text -- The raw text of story.
        sid --  The story id.
        difficulty -- easy, medium, or hard
        type -- whether you need to use the 'sch' or 'story' versions
                of the .
        qid  --  The id of the question.


    story is a dictionary with keys:
        story_dep -- list of dependency graphs for each sentence of
                    the story version.
        sch_dep -- list of dependency graphs for each sentence of
                    the sch version.
        sch_par -- list of constituency parses for each sentence of
                    the sch version.
        story_par -- list of constituency parses for each sentence of
                    the story version.
        sch --  the raw text for the sch version.
        text -- the raw text for the story version.
        sid --  the story id
    """
    ###     Your Code Goes Here         ###
    answer = None
    answer_sentence_graph = None
    qtype = question["type"].lower()
    qtext = get_question_text(question)
    stext = get_story_text(qtype, story)

    """
    EDGE CASE SELECTION
    """

    # Edge case Who is the story about?
    if "who is the story about?" in qtext.lower():
        return get_characters_in_story(story["text"])

    # Edge case "Did"
    if "did" in qtext.lower().split(" ")[0]:
        return "no yes"

    """
    KEYWORD SELECTION
    """

    best_sentence_tree, best_tree, best_sentence_graph, best_graph = \
        find_best_sentence(stext, qtype, qtext, story, question)

    answer_sentence = " ".join(t[0] for t in best_sentence_tree)            # Constituency parsed sentences
    answer_sentence_graph = " ".join(g[0] for g in best_sentence_graph)     # Dependency parsed sentences

    """
    CONSTITUENCY PROCESS
    """

    pattern = nltk.Tree.fromstring(find_pattern(qtext))
    subtrees = pattern_matcher(pattern, best_tree)

    if subtrees is not None:
        qbow = get_bow(get_sentences(qtext)[0], STOPWORDS)
        answer = baseline_answer(qbow, subtrees, best_tree, STOPWORDS)

    """
    DEPENDENCY PROCESS
    """

    # if best_graph is not None:
    #
    #     test = find_answer(question["dep"], best_graph)
    #
    #     if test is not None and "where" in qtext.split(" ")[0].lower():
    #         answer_sentence_graph = " ".join(g[0] for g in best_sentence_graph)
    #         return answer_sentence_graph

    """
    CHUNKING PROCESS
    """

    # Where type question chunking
    if "where" in qtext.split(" ")[0].lower():

        # Extract the candidate locations from these sentences
        chunker = nltk.RegexpParser(GRAMMAR)
        location = find_where_candidates(best_sentence_graph, chunker)

        # print(location)

        chunk_answers = []
        for loc in location:

            # print(loc)

            chunk_answer = (" ".join([token[0] for token in loc.leaves()]))

            if chunk_answer is not None:
                chunk_answers.append(chunk_answer)

        if len(chunk_answers) > 0:
            answer = " ".join(chunk_answers)

    # print(answer)
    # print("\n\n")

    if answer is not None:
        return answer
    else:
        return answer_sentence

    # return answer
    # return answer, answer_sentence


#############################################################
###     Dont change the code in this section
#############################################################
class QAEngine(QABase):
    @staticmethod
    def answer_question(question, story):
        answer = get_answer(question, story)
        return answer


def run_qa(evaluate=False):
    QA = QAEngine(evaluate=evaluate)
    QA.run()
    QA.save_answers()

#############################################################


def main():
    # set evaluate to True/False depending on whether or
    # not you want to run your system on the evaluation
    # data. Evaluation data predictions will be saved
    # to hw6-eval-responses.tsv in the working directory.
    run_qa(evaluate=False)
    # You can uncomment this next line to evaluate your
    # answers, or you can run score_answers.py
    score_answers()


if __name__ == "__main__":
    main()
