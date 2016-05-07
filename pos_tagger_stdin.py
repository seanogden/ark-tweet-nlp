import subprocess
import sys

tagger = subprocess.Popen(
    'java -Xmx500m -jar ark-tweet-nlp/target/bin/ark-tweet-nlp-0.3.2.jar --decoder viterbi --output-format conll --model model.20120919',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE)

for line in open(sys.argv[1]):
    tagger.stdin.write(line + "\n")

while True:
    tag = tagger.stdout.readline()
    if tag != "\n":
        tag = tag.rstrip('\n').strip(' ')
        tag = tag.split('\t')[1]
        print tag
    else:
        break

tagger.
