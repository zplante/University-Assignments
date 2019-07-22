
import re, nltk, pickle, argparse
import os, sys
import data_helper
import features

DATA_DIR = "liwc"


def write_features_category(features_category_tuples, output_file_name):
    output_file = open("{}-features.txt".format(output_file_name), "w", encoding="utf-8")
    for (features, category) in features_category_tuples:
        output_file.write("{0:<10s}\t{1}\n".format(category, features))
    output_file.close()


def get_classifier(classifier_fname):
    classifier_file = open(classifier_fname, 'rb')
    classifier = pickle.load(classifier_file)
    classifier_file.close()
    return classifier


def save_classifier(classifier, classifier_fname):
    classifier_file = open(classifier_fname, 'wb')
    pickle.dump(classifier, classifier_file)
    classifier_file.close()
    info_file = open(classifier_fname.split(".")[0] + '-informative-features.txt', 'w', encoding="utf-8")
    for feature, n in classifier.most_informative_features(100):
        info_file.write("{0}\n".format(feature))
    info_file.close()


def evaluate(classifier, features_category_tuples, reference_text,feature_set, data_set_name=None):

    cap = ""
    if feature_set == "word_features":
        cap = "ngrams"
    if feature_set == "word_pos_features":
        cap = "pos"
    if feature_set == "word_pos_liwc_features":
        cap ="liwc"

    accuracy= nltk.classify.accuracy(classifier, features_category_tuples)

    # TODO: evaluate your model
    #raise NotImplemented
    fout = open("output-"+cap+".txt","w+")
    ref = [pair[1]for pair in features_category_tuples]
    pred = classifier.classify_many([pair[0]for pair in features_category_tuples])
    confusion_matrix = nltk.ConfusionMatrix(ref,pred)
    i =0;
    for t in reference_text:
        p = pred[i]
        fout.write(p+ " "+ t+ "\n")
        i+=1
    fout.write(str(accuracy)+"\n"+str(confusion_matrix)+" \n")
    fout.close()
    return accuracy, confusion_matrix


def build_features(data_file, feat_name, save_feats=None, binning=False):
    # read text liwc
    positive_texts, negative_texts = data_helper.get_reviews(os.path.join(DATA_DIR, data_file))

    category_texts = {"positive": positive_texts, "negative": negative_texts}

    # build features
    features_category_tuples, texts = features.get_features_category_tuples(category_texts, feat_name,data_file)

    # save features to file
    if save_feats is not None:
        write_features_category(features_category_tuples, save_feats)

    return features_category_tuples, texts



def train_model(datafile, feature_set, save_model=None):

    features_data, texts = build_features(datafile, feature_set)
    classifier = nltk.classify.NaiveBayesClassifier.train(features_data)


    ###     YOUR CODE GOES HERE
    # TODO: train your model here
    #raise NotImplemented


    if save_model is not None:
        save_classifier(classifier, save_model)
    return classifier


def train_eval(train_file, feature_set, eval_file=None):

    # train the model
    split_name = "train"
    model = train_model(train_file, feature_set)
    copy = sys.stdout
    sys.stdout = open(feature_set +"-training-informative-features.txt", 'w+')
    model.show_most_informative_features(20)
    sys.stdout = copy
    # save the model
    #if model is None:
    #    model = get_classifier(save_model)

    # evaluate the model
    if eval_file is not None:
        features_data, texts = build_features(eval_file, feature_set, binning=True)
        accuracy, cm = evaluate(model, features_data, texts, feature_set,data_set_name=None,)
        #copy = sys.stdout
        #sys.stdout = open("all-results.txt", 'a')
        print("The accuracy of {} is: {}".format(eval_file, accuracy))
        print("Confusion Matrix:")
        print(str(cm))
        #sys.stdout = copy
    else:
        accuracy = None

    return accuracy

def predict(feat_set,eval_data,train_data,out):
    model = train_model(train_data, feat_set)
    texts= data_helper.get_reviews(os.path.join(DATA_DIR, eval_data))
    fout = open(out,"w+")
    for text in texts:
        words, tags = features.get_words_tags(text)
        feature_vectors = {}
        if feat_set == "word_features":
            feature_vectors.update(features.get_ngram_features(words))
        elif feat_set == "word_pos_features":
            feature_vectors.update(features.get_ngram_features(words))
            feature_vectors.update(features.get_pos_features(tags))
        elif feat_set == "word_pos_liwc_features":
            feature_vectors.update(features.get_ngram_features(words))
            feature_vectors.update(features.get_pos_features(tags))
            feature_vectors.update(features.get_liwc_features(words))
        fout.write(model.classify(feature_vectors)+ " "+text+"\n")

    return
def write_features():
    feat_sets = ["word_features", "word_pos_features", "word_pos_liwc_features"]
    data_sets=["-training","-development","-testing"]
    end = "-features.txt"
    for data in data_sets:
        for feat in feat_sets:
                fout=open(feat+data+end,"w+")
                if data == "-training":
                   file = "train_examples.tsv"
                if data =="-development":
                    file = "dev_examples.tsv"
                if data == "-testing":
                    file = "test.txt"
                positive_texts, negative_texts = data_helper.get_reviews(os.path.join(DATA_DIR, file))
                for text in positive_texts:
                    words, tags = features.get_words_tags(text)
                    fout.write("positive ")
                    temp_vec={}
                    if feat == "word_features":
                        print(features.get_ngram_features(words).keys)

                    elif feat == "word_pos_features":
                        print(features.get_ngram_features(words).keys)

                        print(features.get_pos_features(tags).keys)

                    elif feat == "word_pos_liwc_features":
                        features.get_ngram_features(words)

                        features.get_pos_features(tags)
                        features.get_liwc_features(words)




    return
def main():


    # add the necessary arguments to the argument parser

    train_data = "train_examples.tsv"  # args.data_fname
    if sys.argv[1]=="print":
        write_features()
    if len(sys.argv)==3:
        eval_data = sys.argv[1]
        out = sys.argv[2]
        feat_set = "word_features"
        print("\nTraining with {}".format(feat_set))
        predict(feat_set,eval_data,train_data,out)
    else:
        eval_data = "dev_examples.tsv"
        out = "default.txt"
        for feat_set in ["word_features", "word_pos_features", "word_pos_liwc_features"]:
            print("\nTraining with {}".format(feat_set))
            acc = train_eval(train_data, feat_set, eval_file=eval_data)













if __name__ == "__main__":
    main()




