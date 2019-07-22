import re, nltk, argparse


def get_score(review):
    return int(re.search(r'Overall = ([1-5])', review).group(1))


def get_text(review):
    return re.search(r'Text = "(.*)"', review).group(1)


def read_reviews(file_name):
    """
    Dont change this function.

    :param file_name:
    :return:
    """
    file = open(file_name, "rb")
    raw_data = file.read().decode("latin1")
    file.close()

    positive_texts = []
    negative_texts = []
    first_sent = None
    for review in re.split(r'\.\n', raw_data):
        overall_score = get_score(review)
        review_text = get_text(review)
        if overall_score > 3:
            positive_texts.append(review_text)
        elif overall_score < 3:
            negative_texts.append(review_text)
        if first_sent == None:
            sent = nltk.sent_tokenize(review_text)
            if (len(sent) > 0):
                first_sent = sent[0]
    return positive_texts, negative_texts, first_sent


########################################################################
## Dont change the code above here
######################################################################

#extra funtion for checking a string contains a word character
def is_word(word):
    word_pattern = r'(.*\w.*)'
    re_match = re.search(word_pattern, word)
    return re_match is not None


def process_reviews(file_name):
    positive_texts, negative_texts, first_sent = read_reviews(file_name)
    stop_words = nltk.corpus.stopwords.words('english')
    # There are 150 positive reviews and 150 negative reviews.
    #print(len(positive_texts))
    #print(len(negative_texts))

    # Your code goes here
    pos_words=[]
    neg_words=[]
    i=0
    for text in positive_texts:
        for sent in nltk.sent_tokenize(positive_texts[i]):
            pos_words.extend(nltk.word_tokenize(sent))
        for sent in nltk.sent_tokenize(negative_texts[i]):
            neg_words.extend(nltk.word_tokenize(sent))
        i+=1

    clean_pos_words=[]
    clean_neg_words=[]
    for word in pos_words:
        word=word.casefold()
        if word not in stop_words:
            if is_word(word):
                clean_pos_words.append(word)

    for word in neg_words:
        word = word.casefold()
        if word not in stop_words:
            if is_word(word):
                clean_neg_words.append(word)

    pos_uni = nltk.FreqDist(clean_pos_words)
    neg_uni = nltk.FreqDist(clean_neg_words)
    write_unigram_freq('positive',pos_uni.most_common())
    write_unigram_freq('negative',neg_uni.most_common())

    pos_bg = nltk.bigrams(clean_pos_words)
    neg_bg = nltk.bigrams(clean_neg_words)

    pos_bi = nltk.FreqDist(pos_bg)
    neg_bi = nltk.FreqDist(neg_bg)

    write_bigram_freq('positive', pos_bi.most_common())
    write_bigram_freq('negative', neg_bi.most_common())

    print("Positive Collocations:")
    nltk.Text(clean_pos_words).collocations()
    print("Negative Collocations:")
    nltk.Text(clean_neg_words).collocations()

#    string=''
#    for item in pos_uni.most_common(15):
#        addition = item[0]+'('+str(item[1])+'), '
#        string+=addition
#    print(string)
#   string=''
#    for item in neg_uni.most_common(15):
#        addition = item[0] + '(' + str(item[1]) + '), '
#        string += addition
#    print(string)
#    string = ''
#    for item in pos_bi.most_common(15):
#        addition = item[0][0]+ ' '+item[0][1] + '(' + str(item[1]) + '), '
#        string += addition
#    print(string)
#    string = ''
#    for item in neg_bi.most_common(15):
#        addition = item[0][0]+ ' '+item[0][1] + '(' + str(item[1]) + '), '
#        string += addition
#    print(string)
#    string = ''


# Write to File, this function is just for reference, because the encoding matters.
def write_file(file_name, data):
    file = open(file_name, 'w', encoding="utf-8")  # or you can say encoding="latin1"
    file.write(data)
    file.close()

#extra function for writing bigram files, modeled after the function below provided
def write_bigram_freq(category, bigrams):
    """
    A function to write the unigrams and their frequencies to file.

    :param category: [string]
    :param bigrams: list of ((word,word), frequency) tuples
    :return:
    """
    bi_file = open("{0}-bigram-freq.txt".format(category), 'w', encoding="utf-8")
    for word, count in bigrams:
        bi_file.write("{0:<20s}{1:<20s}{2:<d}\n".format(word[0],word[1], count))
    bi_file.close()


def write_unigram_freq(category, unigrams):
    """
    A function to write the unigrams and their frequencies to file.

    :param category: [string]
    :param unigrams: list of (word, frequency) tuples
    :return:
    """
    uni_file = open("{0}-unigram-freq.txt".format(category), 'w', encoding="utf-8")
    for word, count in unigrams:
        uni_file.write("{0:<20s}{1:<d}\n".format(word, count))
    uni_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Assignment 2')
    parser.add_argument('-f', dest="fname", default="restaurant-training.data", help='File name.')
    args = parser.parse_args()
    fname = args.fname

    process_reviews(fname)