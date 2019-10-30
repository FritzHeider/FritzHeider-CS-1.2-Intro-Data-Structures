import sys
import random

f = open("/usr/share/dict/words", "r")
words_read = f.read()
dictionary_list = words_read.split("\n")
f.close()
words_num = 4

# print(dictionary_list)

def new_sent(words_num):
    new_sentence = ""
    for i in range(words_num):
        new_sentence += random.choice(dictionary_list)
        if i == 0:
            new_sentence = new_sentence.capitalize()
        if i != words_num -1:
            new_sentence += " "
        else:
            punc = [".", "?", "!", "...", "!?!?"]
            new_sentence += random.choice(punc)


    return new_sentence


print(new_sent(words_num))

if __name__== "__main__":
    words_num = sys.argv[1:]
