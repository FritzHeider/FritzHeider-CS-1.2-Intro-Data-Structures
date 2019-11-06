
from sys import argv
import sys
import re
import random

text_input = "one fish two fish red fish blue fish"
#text_input = str(sys.argv[1:])
print(text_input)

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
    print(histo)

    return histo

def random_word_list(histo):
    histogram1 = dict_hist(text_input)
    index = random.randrange(len(text_input.split(" ")))
    value = 0
    hist_ind = 0
    while value <= index and hist_ind < len(histogram1):
        value += histogram1[hist_ind][1]
        hist_ind += 1
    return histogram1[hist_ind - 1][0]

if __name__== "__main__":
    #input_list = sys.argv[1:]
    text_input = "one fish two fish red fish blue fish"
    print(random_word_list("one fish two fish red fish blue fish"))
    #
    # for count in range(100000):
    #     word = random_word_list(text_input)
    #     if word == "ONE":
    #         one += 1
    #     elif word == "TWO":
    #         two += 1
    #     elif word == "RED":
    #         red += 1
    #     elif word == "BLUE":
    #         blue += 1
    #     elif word == "FISH":
    #         fish += 1
    #
    # print("one:  ", (1.0 * one  / 1000), "%")
    # print("two:  ", (1.0 * two  / 1000), "%")
    # print("red:  ", (1.0 * red  / 1000), "%")
    # print("blue: ", (1.0 * blue / 1000), "%")
    # print("fish: ", (1.0 * fish / 1000), "%")
