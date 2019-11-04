from sys import argv
import sys
import re

text_input = str(sys.argv[1:])

def list_hist(text_input):
    text_list = re.split('\W+', text_input)
    histo = list()
    for word in text_list:
        found = False
        for pair in histo:
            if pair[0] == word.upper() and not found:
                pair[1] += + 1
                found = True
        if not found:
            histo.append([word.upper(), 1])

    for pair in histo:
        if pair[0] == "":
            histo.remove(pair)

    return histo


if __name__== "__main__":
    text_input = str(sys.argv[1:])

print(list_hist(text_input))
