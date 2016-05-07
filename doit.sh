#!/bin/bash
#convert to one tweet per line
python maketweets_train.py train.txt > traintweets.txt
python maketweets.py TestNoLabels.txt > TestTweets.txt

#run the tagger
java -Xmx500m -jar ark-tweet-nlp/target/bin/ark-tweet-nlp-0.3.2.jar --decoder viterbi --output-format conll --model model.20120919 traintweets.txt 2> /dev/null > trainPOS.txt
java -Xmx500m -jar ark-tweet-nlp/target/bin/ark-tweet-nlp-0.3.2.jar --decoder viterbi --output-format conll --model model.20120919 TestTweets.txt 2> /dev/null >TestNoLabelPOS.txt 

#make into one dataset
cat TestNoLabelPOS.txt trainPOS.txt > POS.txt
