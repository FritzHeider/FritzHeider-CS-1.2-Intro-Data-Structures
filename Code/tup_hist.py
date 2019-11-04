from sys import argv
import sys
import re

text_input = str(sys.argv[1:])

def tuples_hist(text_input):
    text_list = re.split(r'\W+', text_input)
    histo = list()
    for word in text_list:
        found = False
        for pair in histo:
            if pair[0] == word.upper() and not found:
                number = pair[1] + 1
                histo.remove(pair)
                histo.append((word.upper(), number))
                found = True
        if not found:
            histo.append((word.upper(), 1))

    for pair in histo:
        if pair[0] == "":
            histo.remove(pair)

    return histo

    if __name__== "__main__":
        text_input = str(sys.argv[1:])

print(tuples_hist(text_input))
