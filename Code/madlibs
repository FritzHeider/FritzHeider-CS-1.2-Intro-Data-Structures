
import sys
import random


def rearrange(words_input, words_num):
    word_list = list()

    for index in range(words_num):
        list_item = random.choice(words_input) #picks at random from words words_input
        word_list.append(list_item) #appends pick to word list
        words_input.remove(list_item) #removes pick from remaining choices

    for item in word_list:
        print(item, end=" ") #prints item along with a space

    print()


if __name__== "__main__":
    words_num = len(sys.argv) - 1
    words_input = sys.argv[1:]

    rearrange(words_input, words_num)
