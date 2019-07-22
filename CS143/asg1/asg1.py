#!/usr/bin/env python

import nltk, zipfile, argparse, sys


###############################################################################
## Utility Functions ##########################################################
###############################################################################
# This method takes the path to a zip archive.
# It first creates a ZipFile object.
# Using a list comprehension it creates a list where each element contains
# the raw text of the fable file.
# We iterate over each named file in the archive:
#     for fn in zip_archive.namelist()
# For each file that ends with '.txt' we open the file in read only
# mode:
#     zip_archive.open(fn, 'rU')
# Finally, we read the raw contents of the file:
#     zip_archive.open(fn, 'rU').read()
def unzip_corpus(input_file):
    zip_archive = zipfile.ZipFile(input_file)
    try:
        contents = [zip_archive.open(fn, 'rU').read().decode('utf-8')
                    for fn in zip_archive.namelist() if fn.endswith(".txt")]
    except ValueError as e:
        contents = [zip_archive.open(fn, 'r').read().decode('utf-8')
                    for fn in zip_archive.namelist() if fn.endswith(".txt")]
    return contents


###############################################################################
## Stub Functions #############################################################
###############################################################################
def process_corpus(corpus_name):
    print("Corpus to examine: " + corpus_name)
    input_file = corpus_name + ".zip"
    corpus_contents = unzip_corpus(input_file)
    sentences = []
    words=[]
    pos_results = open(corpus_name + "-pos.txt", 'w+')
    cur_sentence = []
    all_pos = []
    for entry in corpus_contents:
            sentences.append(nltk.sent_tokenize(entry))
    for story in sentences:
        for sent in story:
            word_sent = nltk.word_tokenize(sent)
            words.extend(word_sent)
            cur_sentence=nltk.pos_tag(word_sent)
            all_pos.extend(cur_sentence)
            for pair in cur_sentence:
                pos_results.write(pair[0] + "/" + pair[1])
                pos_results.write('\n')
        pos_results.write('\n')
    print("Number of words: " + str(len(words)))
    i=0
    for word in words:
            words[i]=word.casefold()
            i += 1
    print("The vocabulary size is: " + str(len(set(words))))
    most_common = nltk.FreqDist(pos for (word, pos) in all_pos)
    freq_list = most_common.most_common()
    print("The most common part of speech is " + str(freq_list[0][0]) + " which occurs " + str(freq_list[0][1]) + " times.")
    print("")
    word_dist = nltk.FreqDist(word for word in words)
    word_freq = word_dist.most_common()
    freq_results = open(corpus_name + "-word-freq.txt", 'w+')
    for pair in word_freq:
        freq_results.write(str(pair))
        freq_results.write('\n')
    chart_freq = nltk.ConditionalFreqDist((word.casefold(),tag) for (word, tag) in all_pos)
    con_freq = nltk.ConditionalFreqDist((tag,word.casefold()) for (word, tag) in all_pos)
    copy = sys.stdout
    sys.stdout = open(corpus_name + "-pos-word-freq.txt", 'w+')
    chart_freq.tabulate()
    sys.stdout=copy
    common_words_by_pos = [con_freq['NN'].most_common()[0],con_freq['VBD'].most_common()[0],con_freq['JJ'].most_common()[0],con_freq['RB'].most_common()[0]]
    text_words=nltk.Text(words)
    print("The most common Noun is "+ common_words_by_pos[0][0] +". Similar words include:")
    text_words.similar(common_words_by_pos[0][0])
    print("The most common Past Tense Verb is " + common_words_by_pos[1][0] + ". Similar words include:")
    text_words.similar(common_words_by_pos[1][0])
    print("The most common Adjective is " + common_words_by_pos[2][0] + ". Similar words include:")
    text_words.similar(common_words_by_pos[2][0])
    print("The most common Adverb is " + common_words_by_pos[3][0] + ". Similar words include:")
    text_words.similar(common_words_by_pos[3][0])
    print("")
    print("The found collocations are:")
    text_words.collocations()







    pass


###############################################################################
## Program Entry Point ########################################################
###############################################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment 1')
    parser.add_argument('--corpus', required=True, dest="corpus", metavar='NAME',
                        help='Which corpus to process {fables, blogs}')

    args = parser.parse_args()

    corpus_name = args.corpus

    if corpus_name == "fables" or "blogs":
        process_corpus(corpus_name)
    else:
        print("Unknown corpus name: {0}".format(corpus_name))
