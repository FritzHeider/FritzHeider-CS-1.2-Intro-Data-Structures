from sys import argv
import sys
import re

source_text = str(sys.argv[1:])
#print(source_text)

def dict_hist(source_text):
    text_list = re.split('\W+', source_text)
    histogram = dict()
    for word in text_list:
        if word.upper() in histogram:
            histogram[word.upper()] += 1
        else:
            histogram[word.upper()] = 1

    if "" in histogram:
        histogram.pop("")
    #print(histogram)
    return histogram


if __name__== "__main__":
    source_text = str(sys.argv[1:])

print(dict_hist(source_text))
