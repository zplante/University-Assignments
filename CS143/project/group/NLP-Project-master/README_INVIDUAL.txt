1.
My name is Leahd Lipkin (llipkin@ucsc.edu). I am responsible for submitting the code.

Team members:
Leahd Lipkin (llipkin@ucsc.edu)
Osamah Mahmood (omahmood@ucsc.edu)
Sasha Gonzalez (saligonz@ucsc.edu)
Zac Plante (zplante@ucsc.edu)

--------------------------------------------------------------------------------------------------

2.
Throughout this phase of our project, Osamah, Sasha, Zac and I met for multiple days in person and we worked on our project together.

The four of us also collaborated via Google Hangouts and together, we implemented additional wordnet features such as synonym, hypernym, and hyponym replacement within question sentences. 

After having produced synonyms, hypernyms, and hyponyms for nouns and verbs within question sentences, we would then search for them within respective noun and verb wordnet files that were provided. To search for those files and and to retrieve synset_ids within them, we used relative pathing such that a "/wordnet" folder is expected at the directory level one-up from the directory that qa.py is located in. The program will continue with synonym, hypernym, and hyponym replacement only if the "/wordnet" folder exists and inside are two files: One file contains "noun" in it's filename. The other file contains "verb" in it's filename. Otherwise, the program will continue as usual without snonym, hypernym, and hyponym replacement.

On the account of a matched synset_id in the files, we would thereafter replace original nouns and verbs within question sentences with their synonym, hypernym, or hyponym counterparts. And, after extensive testing, we determined our sentence replacement functions to be working correctly. While this increased the f-measure by 2%, we were expecting greater and more concrete results.

Another idea that we had tried implementing was replacing pronouns such as "he" and "she" within the stories with the noun subject that they refer to. For example, the sentence "A Lion asleep in his lair was waked up by a Mouse running over his face" would therefore become "A Lion asleep in Lion lair was waked up by a Mouse running over Lion face." And, while we successfully implemented a method to do this for story text, we ran into trouble implementing the same for constituency-parsed trees. And, since our final answer that is returned in get_answer is in link to our constituency parses, performing pronoun-subject replacement for just the story text alone did not produce increases.

We used tools such as Github, Slack, Pycharm's built-in debugger, and corenlp.run to accomplish a lot all of our tasks throughout this final phase. And, having reconstructed the NLP pipeline in the previous phase proved very useful. In addition, this provided flexibility for new feature implementations.

Also, after much trial and error, we again found dependency parses to be sacrifical in comparison to our already-built constituency structures. Our pattern-fueled constituency parses proved better results. In contrast, we established higher precision chunking "where" type questions while also using penn-to-wordnet transforms.

Our best sentences and best trees were retrieved using lemmatization, synonym, hypernym, and hyponym replacement, constituency parsing, and multiple baselines. We also found that chunking "where" type questions produced slight increases.

--------------------------------------------------------------------------------------------------

3. 
I worked on wordnet folder and file retrieval using relative pathing. I also worked on synonym, hypernym, and hyponym replacement for nouns and verbs found within the question sentence. However, this replacement would only occur if the determined synonym, hypernym, or hyponym were matched to a synset_id within the provided wordnet files. Lastly, I worked on pronoun to noun subject replacement where the idea was to replace pronouns within the stories with the noun subjects that they refer to. And, while I progressed this to work for story text, I ran into trouble doing the same for constituency parses. However, I now believe that I have an idea on how to do this, by reconstructing "story_par" with hardcoded regex replacements. At the same time, I'd like to make sure that this would not cause overfitting.

--------------------------------------------------------------------------------------------------

4.
Osamah, Sasha, and Zac also worked on sentence selection, pattern selection, and baseline. Osamah's help with synonym, hypernym, and hyponym replacement provided many gains as he helped me with extensive. Sasha produced new innovative patterns and features and without overfitting, managed to fullfill many more edge cases. And, despite having joined our group late, Zac helped with a lot of debugging, provided many useful insights on traversing through constituency trees, and helped with determining many of our patterns, and taught us some things using corenlp.run.

Lastly, I'd like to thank and make clear the equal measure of work performed by each group member, and that all of us put in a great deal of time and effort, while enjoying this project to the fullest!

Thank you graders and TAs as well for the awesome work!


