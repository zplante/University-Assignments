
import nltk
import re
import word_category_counter
import data_helper
import os, sys

DATA_DIR = "liwc"
LIWC_DIR = "liwc"

word_category_counter.load_dictionary(LIWC_DIR)
#a helper function I wrote for ASG2
def is_word(word):
    word_pattern = r'(.*\w.*)'
    re_match = re.search(word_pattern, word)
    return re_match is not None

def normalize(token, should_normalize=True):
    """
    This function performs text normalization.

    If should_normalize is False then we return the original token unchanged.
    Otherwise, we return a normalized version of the token, or None.

    For some tokens (like stopwords) we might not want to keep the token. In
    this case we return None.

    :param token: str: the word to normalize
    :param should_normalize: bool
    :return: None or str
    """
    if not should_normalize:
        normalized_token = token

    else:
        stop_words = nltk.corpus.stopwords.words('english')
        token = token.casefold()
        if token not in stop_words:
            if is_word(token):
                normalized_token=token
            else:
                normalized_token=None
        else:
            normalized_token=None
        ###     YOUR CODE GOES HERE (its above)
        #raise NotImplemented

    return normalized_token



def get_words_tags(text, should_normalize=True):
    """
    This function performs part of speech tagging and extracts the words
    from the review text.

    You need to :
        - tokenize the text into sentences
        - word tokenize each sentence
        - part of speech tag the words of each sentence

    Return a list containing all the words of the review and another list
    containing all the part-of-speech tags for those words.

    :param text:
    :param should_normalize:
    :return:
    """
    words = []
    tags = []

    # tokenization for each sentence
    sentences = nltk.sent_tokenize(text)
    for sent in sentences:
        cur_words = nltk.word_tokenize(sent)
        word_tag = nltk.pos_tag(cur_words)
        for pair in word_tag:
            if normalize(pair[0]) is not None:
                words.append(normalize(pair[0],should_normalize))
            tags.append(pair[1])


    ###     YOUR CODE GOES HERE (its above)
    #raise NotImplemented

    return words, tags


def get_ngram_features(tokens):
    """
    This function creates the unigram and bigram features as described in
    the assignment3 handout.

    :param tokens:
    :return: feature_vectors: a dictionary values for each ngram feature
    """
    feature_vectors = {}
    word_dist = nltk.FreqDist(tokens)
    word_list = word_dist.most_common()
    for pair in word_list:
        feature_vectors[pair[0]]= bin(pair[1])
    bi = nltk.bigrams(tokens)
    bi_list = nltk.FreqDist(bi).most_common()
    for pair in bi_list:
        feature_vectors[pair[0]]=bin(pair[1])

    ###     YOUR CODE GOES HERE
    #raise NotImplemented

    return feature_vectors


def get_pos_features(tags):
    """
    This function creates the unigram and bigram part-of-speech features
    as described in the assignment3 handout.

    :param tags: list of POS tags
    :return: feature_vectors: a dictionary values for each ngram-pos feature
    """
    feature_vectors = {}

    tag_dist = nltk.FreqDist(tags)
    tag_list = tag_dist.most_common()
    for pair in tag_list:
        feature_vectors[pair[0]] = bin(pair[1])
    bi = nltk.bigrams(tags)
    bi_list = nltk.FreqDist(bi).most_common()
    for pair in bi_list:
        feature_vectors[pair[0]]  = bin(pair[1])

    ###     YOUR CODE GOES HERE
    #raise NotImplemented

    return feature_vectors


def bin(count):
    """
    Results in bins of  0, 1, 2, 3 >=
    :param count: [int] the bin label
    :return:
    """
    the_bin = None
    ###     YOUR CODE GOES HERE
    if count<4:
        the_bin=count
    else:
        the_bin=3
    #raise NotImplemented

    return the_bin


def get_liwc_features(words):
    """
    Adds a simple LIWC derived feature

    :param words:
    :return:
    """

    # TODO: binning

    feature_vectors = {}
    text = " ".join(words)
    liwc_scores = word_category_counter.score_text(text)

    # All possible keys to the scores start on line 269
    # of the word_category_counter.py script
    negative_score = liwc_scores["Negative Emotion"]
    positive_score = liwc_scores["Positive Emotion"]
    feature_vectors["Negative Emotion"] = negative_score
    feature_vectors["Positive Emotion"] = positive_score

    if positive_score > negative_score:
        feature_vectors["liwc:positive"] = 1
    else:
        feature_vectors["liwc:negative"] = 1

    return feature_vectors


FEATURE_SETS = {"word_pos_features", "word_features", "word_pos_liwc_features"}

def get_features_category_tuples(category_text_dict, feature_set, datafile):
    """

    You will might want to update the code here for the competition part.

    :param category_text_dict:
    :param feature_set:
    :return:
    """
    features_category_tuples = []
    all_texts = []

    assert feature_set in FEATURE_SETS, "unrecognized feature set:{}, Accepted values:{}".format(feature_set, FEATURE_SETS)

    for category in category_text_dict:
        for text in category_text_dict[category]:

            words, tags = get_words_tags(text)
            feature_vectors = {}
            if feature_set == "word_features":
                feature_vectors.update(get_ngram_features(words))
            elif feature_set == "word_pos_features":
                feature_vectors.update(get_ngram_features(words))
                feature_vectors.update(get_pos_features(tags))
            elif feature_set == "word_pos_liwc_features":
                feature_vectors.update(get_ngram_features(words))
                feature_vectors.update(get_pos_features(tags))

                feature_vectors.update(get_liwc_features(words))



            ###     YOUR CODE GOES HERE
            # raise NotImplemented

            features_category_tuples.append((feature_vectors, category))
            all_texts.append(text)

    return features_category_tuples, all_texts


def write_features_category(features_category_tuples, outfile_name):
    """
    Save the feature values to file.

    :param features_category_tuples:
    :param outfile_name:
    :return:
    """
    with open(outfile_name, "w", encoding="utf-8") as fout:
        for (features, category) in features_category_tuples:
            fout.write("{0:<10s}\t{1}\n".format(category, features))






if __name__ == "__main__":
    pass

