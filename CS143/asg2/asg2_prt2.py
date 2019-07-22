from nltk.corpus import wordnet as wn


# http://stevenloria.com/tutorial-wordnet-textblob/
# http://www.nltk.org/howto/wordnet.html
# http://wordnetweb.princeton.edu/perl/webwn

def print_syn_lemmas(word):
    ## Synsets and Lemmas
    print("1. Synsets and Lemmas")
    print("Word: " + word)
    print("")
    print("Synsets:")
    [print(s) for s in wn.synsets(word)]
    print("")
    first_synset = wn.synsets(word)[0]
    print("First synset: " + str(first_synset))
    print("")

    # word_synset = wn.synset("dog.n.01")
    print("Lemma names: ")
    [print(l) for l in first_synset.lemma_names()]
    print("")
    last_lemma = first_synset.lemmas()[len(first_synset.lemma_names()) - 1]
    # word_lemma = wn.lemma("dog.n.01.domestic_dog")
    print("Last lemmas: " + str(last_lemma))
    print("")
    print("Synset of Last lemmas: " + str(last_lemma.synset()))
    print("")
    for synset in wn.synsets(word):
        print(str(synset) + ": lemma_name" + str(synset.lemma_names()))
    print("")
    print("Lemmas of {}:".format(word))
    [print(l) for l in wn.lemmas(word)]
    print("")
    print("")


def print_def_exp(synset):
    ## Definitions and Examples
    print("2. Definitions and Examples")
    print("Synset: " + str(synset))
    print("Definition: " + synset.definition())
    print("")
    print("Example: " + str(synset.examples()))
    print("")
    print("Synsets of first lemma " + str(synset.lemma_names()[0]) + ": ")
    for synset in wn.synsets(synset.lemma_names()[0]):
        print(synset, ": definition (", synset.definition() + ")")
    print("")
    print("")


def print_lexical_rel(synset):
    ## Lexical Relations
    print("3. Lexical Relations")
    print("Synset: " + str(synset))
    print("")
    print("Hypernyms: " + str(synset.hypernyms()))
    print("")
    print("Hyponyms: " + str(synset.hyponyms()))
    print("")
    print("Root hypernyms: " + str(synset.root_hypernyms()))
    print("")

    paths = synset.hypernym_paths()
    print("Hypernym path length of {} = {} ".format(str(synset), str(len(paths))))
    print("")
    for i in range(len(paths)):
        print("Path[{}]:".format(i))
        [print(syn.name()) for syn in paths[i]]
        print("")
    print("")


def print_other_lexical_rel():
    good1 = wn.synset('good.a.01')
    wn.lemmas('good')
    print("Antonyms of 'good': " + str(good1.lemmas()[0].antonyms()))
    print("")
    print("Entailment of 'walk': " + str(wn.synset('walk.v.01').entailments()))
    print("")
#My Code
def prt2(word):
    file = open('wordnet.txt','w+')
    #prints synsets and definitions
    syns = wn.synsets(word)
    file.write(word)
    file.write('\n')
    for syn in syns:
        file.write(str(syn.name())+": "+syn.definition()+'\n')
    syn = syns[0]
    file.write('\n')
    #prints hyponyms and root hypernym
    file.write(str(syn.name()))
    file.write('\n')
    syn = wn.synset(syn.name())
    hypo = syn.hyponyms()
    file.write('Hyponyms: \n')
    for h in hypo:
        file.write(str(h.name()))
        file.write('\n')
    file.write('\n')
    r_hyper = syn.root_hypernyms()
    file.write('Root Hypernyms: \n')
    for r in r_hyper:
        file.write(str(r.name()))
        file.write('\n')
    file.write('\n')
    #prints path
    paths = syn.hypernym_paths()
    i =0
    for path in paths:
        file.write('Path '+str(i)+'\n')
        for item in path:
            file.write(str(item.name())+'\n')
        file.write('\n')



if __name__ == '__main__':
    #print_syn_lemmas('dog')
    #print_def_exp(wn.synset("dog.n.01"))
    #print_lexical_rel(wn.synset("dog.n.01"))
    #print_other_lexical_rel()
    #My Code, I will be using the word cat because my roomate wanted me too
    word = "cat"
    prt2(word)






