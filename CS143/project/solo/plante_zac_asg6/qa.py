
from qa_engine.base import QABase
from qa_engine.score_answers import main as score_answers
import nltk, operator
import chunk, constituency, dependency
from nltk.stem.wordnet import WordNetLemmatizer
import operator
# things to try: stemmed and non-stemmed keywords, intersection of q and sent, stemming sentence
STOPWORDS = set(nltk.corpus.stopwords.words("english"))


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

def find_verbs(tags):
    i = 1
    ret = []
    for w in tags:
        if i>1:
            if "VB" in w[1]:
                ret.append(w[0])
        i+=1
    return ret
def find_nouns(tags):
    i = 1
    ret = []
    for w in tags:
        if i>1:
            if "NN" in w[1]:
                ret.append(w[0])
        i+=1
    return ret
def find_adj(tags):
    i = 1
    ret = []
    for w in tags:
        if i>1:
            if "JJ" in w[1]:
                ret.append(w[0])
        i+=1
    return ret
def find_most_common(contexts,qtext):
    sents={}
    sentences = []
    for s in contexts:
        if s in sents:
            value=sents[s]+1
            ret = {s:value}
        else:
            ret = {s:1}
        sents.update(ret)
    qwords = nltk.word_tokenize(qtext)
    return max(sents.items(), key=operator.itemgetter(1))[0]
def find_who(tree,qtext):
    subtree=chunk.find_nphrases(tree)
    possible=[]
    for sub in subtree:
        possible.append(" ".join([token[0] for token in sub.leaves()]))
    return possible[0]
def find_what(tree):
    subtree=chunk.find_vphrases(tree)
    possible=[]
    for sub in subtree:
        s = chunk.find_nphrases(sub)
        for p in s:

            possible.append(" ".join([token[0] for token in p.leaves()]))
    if len(possible)==0:
        find_what_did(tree)
    else:
        return possible[0]
def find_what_did(tree):
    subtree=chunk.find_vphrases(tree)
    possible=[]
    for sub in subtree:
        possible.append(" ".join([token[0] for token in sub.leaves()]))
    return possible[0]
def find_when(tree):
    subtree=chunk.find_pphrases(tree)
    for sub in subtree:
        if chunk.is_time(sub[0]):
            answer=" ".join([token[0] for token in sub.leaves()])
def find_where(tree):
    subtree=chunk.find_pphrases(tree)
    for sub in subtree:
        if chunk.is_location(sub[0]):
            answer=" ".join([token[0] for token in sub.leaves()])
def find_why(answer):
    if "because" in answer:
        i=answer.index("because")
        answer=answer[i+8:]
    elif "to" in answer:
        i=answer.index("to")
        answer=answer[i+3:]
    return answer


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
    mode = question["type"]
    if mode == "Sch":
        key = "sch"
    else:
        key = "text"

    stext = story[key]
    qtext = question["text"]
    sentences = get_sentences(stext)
    
    chunker = nltk.RegexpParser(chunk.GRAMMAR)
    lmtzr = WordNetLemmatizer()
    qtag = nltk.pos_tag(nltk.word_tokenize(qtext))
    qtree = chunker.parse(qtag)
    verb = None
    noun = None
    prep = None
    adj =None
    print(qtext)
    verb = find_verbs(qtag)
    prep = chunk.find_pphrases(qtree)
    noun = find_nouns(qtag)
    adj = find_adj(qtag)
    stem_noun=[]
    stem_verb=[]
    joined_prep=[]
    if noun is not None:
        for w in noun:
            stem_noun.append(lmtzr.lemmatize(w, "n"))
    if verb is not None:
        for w in verb:
            stem_verb.append(lmtzr.lemmatize(w,"v"))
    if adj is not None:
        for w in adj:
            stem_noun.append(lmtzr.lemmatize(w,"n"))
    if prep is not None:
        for w in prep:
            w =" ".join([token[0] for token in w.leaves()])
            joined_prep.append(w)
    stem_noun.extend(noun)
    stem_noun.extend(noun)
    stem_verb.extend(verb)
    keywords=[]
    keywords.extend(stem_noun)
    keywords.extend(stem_verb)
    keywords.extend(joined_prep)
    print(keywords)
    possible_context = chunk.find_sentences(keywords,sentences)
    if len(possible_context)==0:
        print("")
        answer=""
    else:
        answers=[]
        for w in possible_context:
            answers.append(" ".join(t[0] for t in w))
        
        answer=find_most_common(answers,qtext)
    print(answer)
    atags =nltk.pos_tag(nltk.word_tokenize(answer))
    tree = chunker.parse(atags)
    if "where" in qtext or  "Where" in qtext:
        find_where(tree)
    elif "who" in qtext or "Who" in qtext:
        answer = find_who(tree,qtext)
    elif "why" in qtext or "Why" in qtext:
        answer=find_why(answer)
        #subtree=chunk.find_sbarphrases(tree)
        #if len(subtree)==0:
        #    subtree=chunk.find_vphrases(tree)
        #    for sub in subtree:
        #        if chunk.is_reason(sub[0]):
        #            answer = " ".join([token[0] for token in sub.leaves()])
        #else:
        #   answer = " ".join([token[0] for token in subtree[0].leaves()])
    elif "what" in qtext or "What" in qtext:
        if "do" in qtext:
            i=1
            find_what_did(tree)
        else:
            i=1
            find_what(tree)
            
    elif "when" in qtext or "When" in qtext:
        find_when(tree)
    ###     End of Your Code         ###
    return answer



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
