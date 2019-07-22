'''
Created on May 14, 2014
@author: Reid Swanson

Modified on May 21, 2015
'''

import re, sys, nltk

from qa_engine.base import QABase




# Our simple grammar from class (and the book)
GRAMMAR =   """
            N: {<PRP>|<NN.*>}
            V: {<V.*>}
            ADJ: {<JJ.*>}
            NP: {<DT>? <ADJ>* <N>+}
            PP: {<IN> <NP>}
            VP: {<TO>? <V> (<NP>|<PP>)*}
            """

LOC_PP = set(["in", "on", "at","around","among","above","across",
                "behind","below","beneath","beside","between","beyond",
                "by","inside","near","to"])
TEMP_PP = set(["after","around","before","between","during"])


def get_sentences(text):
    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    
    return sentences

def pp_filter(subtree):
    return subtree.label() == "PP"
def np_filter(subtree):
    return subtree.label() == "NP"
def vp_filter(subtree):
    return subtree.label() == "VP"
def sbar_filter(subtree):
    return subtree.label() == "SBAR"

def is_reason(prep):
    return prep[0] =="to"
def is_location(prep):
    return prep[0] in LOC_PP
def is_time(prep):
    return prep[0] in TEMP_PP
def find_sbarphrases(tree):
    locations=[]
    for subtree in tree.subtrees(filter=sbar_filter):
        locations.append(subtree)
    return locations
def find_pphrases(tree):

    locations = []
    for subtree in tree.subtrees(filter=pp_filter):
        
        locations.append(subtree)
    
    return locations
def find_nphrases(tree):
    locations = []
    for subtree in tree.subtrees(filter=np_filter):
        
        locations.append(subtree)
    
    return locations
def find_vphrases(tree):
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
    for subtree in tree.subtrees(filter=vp_filter):
        
        locations.append(subtree)
    
    return locations

def find_candidates(sentences, chunker, filter):
    candidates = []
    for sent in sentences:
        tree = chunker.parse(sent)
        # print(tree)
        candidates.extend(find_pphrases(tree))
        
    return candidates

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
            if matches:
                result.append(sent)
            
    return result
