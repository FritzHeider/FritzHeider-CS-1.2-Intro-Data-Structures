from sys import argv
import sys
import re

text_input = str(sys.argv[1:])
#print(text_input)

def dict_hist(text_input):
    text_list = re.split('\W+', text_input)
    histo = dict()
    for word in text_list:
        if word.upper() in histo:
            histo[word.upper()] += 1
        else:
            histo[word.upper()] = 1

    if "" in histo:
        histo.pop("")
    #print(histo)
    return histo

if __name__== "__main__":
    text_input = str(sys.argv[1:])

print(dict_hist(text_input))
