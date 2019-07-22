
import re, nltk, pickle, argparse
import os, sys
import data_helper
import features


from sklearn import svm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
import sklearn, numpy
import pandas as pd
import random
from sklearn import tree
from nltk.classify import SklearnClassifier




DATA_DIR = "data"

random.seed(10)


MODEL_DIR = "models/"
OUTPUT_DIR = "output/"
FEATURES_DIR = "features/"

def select_features(classifier):
    best = (0.0, 16384)
    best_features = classifier.most_informative_features(10000)
    
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
    #write_features_category(train_data, "save_feat.txt")
    return classifier

def build_features(data_file, feat_name, save_feats=None):
    # read text data
    positive_texts, negative_texts = data_helper.get_reviews(os.path.join(DATA_DIR, data_file))

    category_texts = {"positive": positive_texts, "negative": negative_texts}

    # build features
    features_category_tuples, texts = features.get_features_category_tuples(category_texts, feat_name)

    # save features to file
    #if save_feats is not None:
    #    features_category_tuples = select_features(features_category_tuples)
    #    write_features_category(features_category_tuples, save_feats)

    return features_category_tuples, texts
#def get_sel_feat(file):


def train_model(model):
    train_data="train_examples.tsv"
    feat_file="data/save_feat.txt"
    f = open(feat_file, 'r')
    l = f.readlines()
    feats=[]
    for line in l:
        #print(line)
        sent_r = r"([^\s]+)"
        dic_r= r"\{([^}]+)\}"
        key_r=r"([^\s]+)"
        sent = re.findall(sent_r, line)[0]
        #print(sent)
        dic = re.findall(dic_r,line)[0]
        dic = dic[0:len(dic)]
       # print(dic)
        dic_list = dic.split(",")
        #print(dic_list)
        feat_dic = {}
        for stuff in dic_list:
            pair = re.findall(key_r,stuff)
            key = pair[0][1:len(pair[0])-2]
            val = pair[1]
            #print(key+":"+val)
            feat_dic.update({key:int(val)})
        feats.append((feat_dic,sent))
    #print(feats)
    model.train(feats)
    return model
def get_we_feat(file):
    feat,text=build_features(file,"word_features")
    feat_list = []
    i=0
    for rev in text:

        w2v_feat=features.get_word_embedding_features(rev)
        feat_list.append((w2v_feat,feat[i][1]))
        i+=1
    return feat_list

def train_word_embem_model(model):
    train_data="train_examples.tsv"
    feat_list=get_we_feat(train_data)
    model.train(feat_list)
    return model
def build_classifier(classifier_name):
    """
    Accepted names: nb, dt, svm, sk_nb, sk_dt, sk_svm

    svm and sk_svm will return the same type of classifier.

    :param classifier_name:
    :return:
    """
    if classifier_name == "nb":
        cls = nltk.classify.NaiveBayesClassifier
    elif classifier_name == "nb_sk":
        cls = SklearnClassifier(BernoulliNB())
    elif classifier_name == "dt":
        cls = nltk.classify.DecisionTreeClassifier
    elif classifier_name == "dt_sk":
        cls = SklearnClassifier(tree.DecisionTreeClassifier())
    elif classifier_name == "svm_sk" or classifier_name == "svm":
        cls = SklearnClassifier(svm.SVC())
    else:
        assert False, "unknown classifier name:{}; known names: nb, dt, svm, nb_sk, dt_sk, svm_sk".format(classifier_name)

    return cls


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

def main(reviews,output):
    model1 = build_classifier("nb_sk")
    print("nb_sk")
    model1=train_model(model1)
    model2 = build_classifier("dt_sk")
    print("dt_sk")
    model2=train_model(model2)
    model3=build_classifier("svm")
    print("svm")
    model3=train_model(model3)
    model4=build_classifier("svm")
    print("svm we")
    model4 = train_word_embem_model(model4)
    models=[model1,model2,model3,model4]
    file = open(output,"w+")
    i = 1
    for model in models:
        if i == 4:
            file.write("model"+str(i)+"\n")
            dev_data = "dev_examples.tsv"
            file.write(dev_data+"\n")
            dev_feats= get_we_feat(dev_data,)
            #print(dev_feats)
            acc, cm = evaluate(model,dev_feats,dev_text)
            file.write(str(acc)+"\n"+str(cm)+"\n")
            file.write(reviews+"\n")
            test_feat= get_we_feat(reviews)
            #print(test_feat)
            acc, cm = evaluate(model,test_feat,test_text)
            file.write(str(acc)+"\n"+str(cm)+"\n")
            i+=1
        else:
            file.write("model"+str(i)+"\n")
            dev_data = "dev_examples.tsv"
            file.write(dev_data+"\n")
            dev_feats, dev_text= build_features(dev_data,"word_features")
            #print(dev_feats)
            acc, cm = evaluate(model,dev_feats,dev_text)
            file.write(str(acc)+"\n"+str(cm)+"\n")
            file.write(reviews+"\n")
            test_feat,test_text = build_features(reviews,"word_features")
            #print(test_feat)
            acc, cm = evaluate(model,test_feat,test_text)
            file.write(str(acc)+"\n"+str(cm)+"\n")
            i+=1




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Assignment 3')
    parser.add_argument('-r', dest="reviews", default=None, required=False,
                        help='The file with the reviews in it to be classified.')
    parser.add_argument('-p', dest="pred_file", default="predictions.txt", required=False,
                        help='The file to write predictions to.')

    args = parser.parse_args()
    main(args.reviews, args.pred_file)










