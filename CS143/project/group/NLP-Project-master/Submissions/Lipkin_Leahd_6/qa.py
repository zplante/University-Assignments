import re

from nltk import WordNetLemmatizer

from qa_engine.base import QABase
from qa_engine.score_answers import main as score_answers
import nltk, operator
from nltk.corpus import wordnet as wn

STOPWORDS = set(nltk.corpus.stopwords.words("english"))

GRAMMAR = """
                N: {<PRP>|<NN.*>}
                V: {<V.*>}
                ADJ: {<JJ.*>}
                NP: {<DT>? <ADJ>* <N>}
                PP: {<IN> <NP>}
                VP: {<TO>? <V> (<NP>|<PP>)*}
            """

LOC_PP = set(["in", "on", "at", "under", "above", "to", "along", "around"])

LOC_CC = set(["the", "a"])


# The standard NLTK pipeline for POS tagging a document
def get_sentences(text):

    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    return sentences


def get_bow(tagged_tokens, stopwords):

    return set([t[0].lower() for t in tagged_tokens if t[0].lower() not in stopwords])


def find_phrase(tagged_tokens, qbow):

    for i in range(len(tagged_tokens) - 1, 0, -1):

        word = (tagged_tokens[i])[0]

        if word in qbow:
            return tagged_tokens[i + 1:]


# Given a list of sentences, returns the sentence that appears the most if there is one
def find_best_sentence(sentences):

    if len(sentences) > 1:
        for i in range(len(sentences)-1):

            if sentences[i] == sentences[i+1]:
                return sentences[i]

    return None


def find_sentences(patterns, sentences):

    # Get the raw text of each sentence to make it easier to search using regexes
    raw_sentences = [" ".join([token[0] for token in sent]) for sent in sentences]

    result = []

    for sent, raw_sent in zip(sentences, raw_sentences):
        for pattern in patterns:

            if not re.search(pattern, raw_sent):
                matches = False

            else:
                matches = True

        if matches is True:
            result.append(sent)

    return result


def pp_filter(subtree):

    return subtree.label() == "PP"


def cc_filter(subtree):

    return subtree.label() == "CC"


def is_location(prep):

    return prep[0] in LOC_PP


def is_character(prep):

    return prep[0] in LOC_CC


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


def find_characters(tree):
    # Starting at the root of the tree
    # Traverse each node and get the subtree underneath it
    # Filter out any subtrees who's label is not a PP
    # Then check to see if the first child (it must be a preposition) is in
    # our set of locative markers
    # If it is then add it to our list of candidate locations

    # How do we modify this to return only the NP: add [1] to subtree!
    # How can we make this function more robust?
    # Make sure the crow/subj is to the left
    characters = []

    for subtree in tree.subtrees(filter=cc_filter):

        if is_character(subtree[0]):
            characters.append(subtree)

    return characters


def find_where_candidates(crow_sentences, chunker):
    candidates = []

    for sent in crow_sentences:
        tree = chunker.parse(sent)

        # print(tree)

        locations = find_locations(tree)

        candidates.extend(locations)

    return candidates


# return a list of the characters in the story given the story text
def get_characters_in_story(text):

    sentences = get_sentences(text)  # pos tagged sentences
    characters = []

    for sent in sentences:
        for tup in sent:

            if tup[1] == "NNP" and text.count(tup[0]) > 1:

                characters.append(tup[0])

    characters = set(characters)

    return characters


def find_who_candidates(crow_sentences, chunker):
    candidates = []

    for sent in crow_sentences:
        tree = chunker.parse(sent)

        # print(tree)

        characters = find_characters(tree)

        # print(characters)

        # characters = get_characters_in_story(tree)

        candidates.extend(characters)

    return candidates


def get_text_question(question):
    driver = QABase()

    qid = question["qid"]
    q = driver.get_question(qid)
    question = q["text"]

    raw_tags = get_sentences(question)[0]
    word_array = []
    tag_array = []

    for word, tag in raw_tags:
        word_array.append(word)
        tag_array.append(tag)

    questions = []

    for i in range(len(word_array) - 1):

        regex_vb = re.findall(r'(VB\w?)', tag_array[i])
        regex_nn = re.findall(r'(NN\w?)', tag_array[i])
        regex_jj = re.findall(r'(JJ\w?)', tag_array[i])

        """
        if tag_array[i] == 'WRB':
            word = str(word_array[i]).lower()
            questions.append((word, tag_array[i]))

        if tag_array[i] == 'WP':
            word = str(word_array[i]).lower()
            questions.append((word, tag_array[i]))

        """

        if len(regex_vb) > 0:
            if tag_array[i] == regex_vb[0]:
                word = str(word_array[i]).lower()
                questions.append((word, tag_array[i]))

        if len(regex_nn) > 0:
            if tag_array[i] == regex_nn[0]:
                word = str(word_array[i]).lower()
                questions.append((word, tag_array[i]))

        if len(regex_jj) > 0:
            if tag_array[i] == regex_jj[0]:
                word = str(word_array[i]).lower()
                questions.append((word, tag_array[i]))

    # print(len(questions))
    # print(questions)
    # print("\n")

    return questions


# qtokens: is a list of pos tagged question tokens with SW removed
# sentences: is a list of pos tagged story sentences
# stopwords is a set of stopwords
def baseline(qbow, sentences, stopwords):
    # Collect all the candidate answers
    answers = []
    for sent in sentences:
        # A list of all the word tokens in the sentence
        sbow = get_bow(sent, stopwords)

        # Count the # of overlapping words between the Q and the A
        # & is the set intersection operator
        intersect = qbow & sbow
        overlap = len(intersect)

        answers.append((overlap, sent))

    # Sort the results by the first element of the tuple (i.e., the count)
    # Sort answers from smallest to largest by default, so reverse it
    answers = sorted(answers, key=operator.itemgetter(0), reverse=True)

    # Return the best answer
    best_answer = answers[0][1]
    return best_answer


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


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

    lmtzr = WordNetLemmatizer()
    sentences = []
    patterns = []
    word_array = []
    tag_array = []

    stext = None
    qtext = get_text_question(question)

    if question["type"] == "Sch":
        stext = story["sch"]

    else:
        stext = story["text"]

    # gets verbs, nouns in question
    for word, tag in qtext:

        word_array.append(word)
        tag_array.append(tag)

        wordlem = lmtzr.lemmatize(word, penn_to_wn(tag))
        patterns.append(wordlem)

    # gives list of sentences that has a word from the question in it in result
    for sentence in nltk.sent_tokenize(stext):
        for pattern in patterns:

            # should return one pos tagged sentence
            sent = get_sentences(sentence)[0]

            # print(sent)

            lemmatized_sentence = [lmtzr.lemmatize(token, penn_to_wn(tag)) for token, tag in sent]

            lemmatized_sentence = " ".join(token for token in lemmatized_sentence)

            if not re.search(pattern, lemmatized_sentence):
                matches = False

            else:
                matches = True

            if matches:
                sentences.append(sentence)

    # for sentence in raw_sentences:
    #     for pattern in patterns:
    #
    #         if not re.search(pattern, sentence):
    #             matches = False
    #
    #         else:
    #             matches = True
    #
    #         if matches:
    #              sentences.append(sentence)

    baseline_answer = None
    if find_best_sentence(sentences) is not None:

        baseline_answer = find_best_sentence(sentences)

    else:
        qbow = get_bow(get_sentences(question["text"])[0], STOPWORDS)

        sentences = get_sentences(" ".join(sentences))

        best_sentence = baseline(qbow, sentences, STOPWORDS)

        baseline_answer = " ".join(t[0] for t in best_sentence)

    question_type = str(nltk.word_tokenize(question["text"])[0]).lower()

    # print("\nQUESTION TYPE:")
    # print(question_type)

    # replace with the sentence containing answer
    sentences = get_sentences(baseline_answer)

    # Find the sentences that have all of our keywords in them
    # How could we make this better?
    keyword_sentences = find_sentences(patterns, sentences)

    # print("\nSENTENCES FROM BASELINE:\n")
    # print(sentences)
    # print("\nPATTERNS CREATED FROM get_text_question:\n")
    # print(patterns)
    # print("\nKEYWORD SENTENCES FOUND FROM PATTERNS:\n")
    # print(keyword_sentences)

    # if "what" in question_type:
    #
    #     sentwords = sentences[0]
    #
    #     answer = []
    #     # print(sentwords)
    #
    #     for tup in sentwords:
    #
    #         if "." in tup[0]:
    #
    #             continue
    #
    #         new_tup = tup[0]
    #
    #         # Taking any word that's in the question out of the story sentence
    #         if new_tup not in patterns and nltk.word_tokenize(new_tup.lower())[0] not in STOPWORDS:
    #             answer.append(new_tup)
    #
    #     # print(answer)
    #
    #     what_answer = " ".join(token for token in answer)
    #
    #     # print(what_answer)
    #     if len(what_answer) > 0:
    #         return what_answer

    # Where type question chunking
    if "where" in question_type:

        chunker = nltk.RegexpParser(GRAMMAR)

        # Extract the candidate locations from these sentences
        locations = find_where_candidates(keyword_sentences, chunker)

        chunk_answers = []
        for loc in locations:

            # print(loc)

            chunk_answer = (" ".join([token[0] for token in loc.leaves()]))

            if chunk_answer is not None:

                chunk_answers.append(chunk_answer)

        if len(chunk_answers) > 0:

            baseline_answer = " ".join(chunk_answers)

    # Who type question chunking
    if "who" in question_type:

        stext = story["text"]

        characters = get_characters_in_story(stext)

        if question["text"] == "Who is the story about?":

            char_answer = "a "
            char_suf = " and a ".join(char for char in characters)
            char_answer += char_suf

            return char_answer

        char_answer = " the ".join(char for char in characters)

        """
        chunker = nltk.RegexpParser(GRAMMAR)
        
        characters = find_who_candidates(keyword_sentences, chunker)
        
        chunk_answers = []
        for char in characters:

            # print(char)

            chunk_answer = (" ".join([token[0] for token in char.leaves()]))

            if chunk_answer is not None:

                chunk_answers.append(chunk_answer)

        if len(chunk_answers) > 0:

            baseline_answer = " ".join(chunk_answers)
        """

        return "the " + char_answer

    return baseline_answer


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
