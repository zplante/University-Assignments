
import re, nltk, pickle, argparse
import os,sys
import data_helper
import features 
DATA_DIR = "data"

def select_features(classifier):
    best = (0.0, 0)
    best_features = classifier.most_informative_features(10000)
    for i in [2**i for i in range(5, 14)]:
        selected_features = set([fname for fname, value in best_features[:i]])
        #print(selected_features)
        temp_train,dis = build_features("train_examples.tsv","word_features")
        train_data = []
        for rev in temp_train:
            temp_dic={}
            for key,value in rev[0].items():
                if key in selected_features:
                    temp_dic.update({key:value})   
            train_data.append((temp_dic,rev[1]))



        develop_data,textsd    = build_features("dev_examples.tsv","word_features")
        
    
        classifier = nltk.NaiveBayesClassifier.train(train_data)
        accuracy = nltk.classify.accuracy(classifier, develop_data)
        print("{0:6d} {1:8.5f}".format(i, accuracy))
    
        if accuracy > best[0]:
            best = (accuracy, i)
    
     # Now train on the best features
    selected_features = set([fname for fname, value in best_features[:best[1]]])
    temp_train,dis = build_features("train_examples.tsv","word_features")
    train_data = []
    for rev in temp_train:
            temp_dic={}
            for key,value in rev[0].items():
                if key in selected_features:
                    temp_dic.update({key:value})   
            train_data.append((temp_dic,rev[1]))




    
        
    
    classifier = nltk.NaiveBayesClassifier.train(train_data)
    write_features_category(train_data, "save_feat.txt")
    return classifier
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


def evaluate(classifier, features_category_tuples, reference_text, data_set_name=None):

    # test on the data
    accuracy = nltk.classify.accuracy(classifier, features_category_tuples)


    #accuracy_results_file = open("{}_results.txt".format(data_set_name), 'w', encoding='utf-8')
    #accuracy_results_file.write('Results of {}:\n\n'.format(data_set_name))
    #accuracy_results_file.write("{0:10s} {1:8.5f}\n\n".format("Accuracy", accuracy))

    features_only = []
    reference_labels = []
    for feature_vectors, category in features_category_tuples:
        features_only.append(feature_vectors)
        reference_labels.append(category)

    predicted_labels = classifier.classify_many(features_only)

    confusion_matrix = nltk.ConfusionMatrix(reference_labels, predicted_labels)

    #accuracy_results_file.write(str(confusion_matrix))
    #accuracy_results_file.write('\n\n')
    #accuracy_results_file.close()

    #predict_results_file = open("{}_output.txt".format(data_set_name), 'w', encoding='utf-8')
    #for reference, predicted, text in zip(
    #        reference_labels,
    #        predicted_labels,
    #        reference_text
    #):
    #    if reference != predicted:
    #        predict_results_file.write("{0} {1}\n{2}\n\n".format(reference, predicted, text))
    #predict_results_file.close()

    return accuracy, confusion_matrix



def build_features(data_file, feat_name, save_feats=None):
    # read text data
    positive_texts, negative_texts = data_helper.get_reviews(os.path.join(DATA_DIR, data_file))

    category_texts = {"positive": positive_texts, "negative": negative_texts}

    # build features
    features_category_tuples, texts = features.get_features_category_tuples(category_texts, feat_name)

    # save features to file
    if save_feats is not None:
        #features_category_tuples = select_features(features_category_tuples)
        write_features_category(features_category_tuples, save_feats)

    return features_category_tuples, texts



def train_model(datafile, feature_set, split_name, save_model=None, save_feats=None, binning=False):

    features_data, texts = build_features(datafile, feature_set)
    classifier = nltk.classify.NaiveBayesClassifier.train(features_data)

    if save_model is not None:
        save_classifier(classifier, save_model)
    classifier = select_features(classifier)
    return classifier


def train_eval(train_file, eval_file,review_file, feature_set,pred_file):

    # train the model
    split_name = "train"
    model = train_model(train_file, feature_set, split_name)

    # evaluate the model
    if model is None:
        model = get_classifier(classifier_fname)

    copy = sys.stdout
    sys.stdout = open(pred_file,'a')
    print("Using "+feature_set)
    print(eval_file)
    features_data, texts = build_features(eval_file, feature_set)
    accuracy, cm = evaluate(model, features_data, texts, data_set_name="eval-{}".format(feature_set))
    print("\nThe accuracy of {} is: {}".format(eval_file, accuracy))
    #print("Confusion Matrix:")
    #print(str(cm))

    
    if "test" in review_file:
        texts= data_helper.get_reviews(os.path.join(DATA_DIR, review_file))
        for text in texts:
            words, tags = features.get_words_tags(text)
            feature_vectors = {}
            feature_vectors.update(features.get_ngram_features(words))
            print(model.classify(feature_vectors)+ " "+text+"\n")  
    else:
        features_data, texts = build_features(review_file, feature_set)
        accuracy, cm = evaluate(model, features_data, texts, data_set_name="eval-{}".format(feature_set))
        print(review_file)
        print("\nThe accuracy of {} is: {}".format(eval_file, accuracy))
        #print("Confusion Matrix:")
        #print(str(cm))
    sys.stdout = copy


def predict_main(review_file, pred_file):
    # train the model
    train_data = "train_examples.tsv"
    eval_data = "dev_examples.tsv"
    split_name = "train"
    feat_set = "word_features"
    
   
    print("\n" + "-"*50)
    print("Training with {} \n".format(feat_set))
    acc = train_eval(train_data, eval_data,review_file,feat_set,pred_file)

       



if __name__ == "__main__":
    """
    (a) The file with the reviews in it to be classified.
    (b) The second should be the name of a file to write predictions to. When saving predictions, each
    predicted label should be on a separate line in the output file, in the same order as the input file.
    This file should be the output of a function called evaluate. The evaluate function should also
    calculate the accuracy and confusion matrix if it is supplied with the example labels.
    """

    "data/test.txt"
    parser = argparse.ArgumentParser(description='Assignment 3')
    parser.add_argument('-r', dest="reviews", default=None, required=False,
                        help='The file with the reviews in it to be classified.')
    parser.add_argument('-p', dest="pred_file", default="predictions.txt", required=False,
                        help='The file to write predictions to.')

    args = parser.parse_args()

    if args.reviews is not None:
        # An example way of calling the script to make predictions
        # python3 classify.py -r data/test.txt -p test-preds.txt
        predict_main(args.reviews, args.pred_file)
       





