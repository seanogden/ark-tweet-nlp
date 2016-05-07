import sys
line = list()
for w in open(sys.argv[1]):
    line += [w.strip("\n").split("\t")[0]] 
    if w == "\n":
        print " ".join(line)
        line = list()
