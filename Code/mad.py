
import sys
import random

word_list = list()
words_num = 4
words_input = list()
words_input.append(input("Hello welcome to the mad libs game, Enter 4 Adjectives PLease! "))
words_input.append(input("3 more please "))
words_input.append(input("almost there "))
words_input.append(input("one more! "))
print(words_input)

def rearrange(words_input, words_num):


    for index in range(words_num):
        list_item = random.choice(words_input) #picks at random from words words_input
        word_list.append(list_item) #appends pick to word list
        words_input.remove(list_item) #removes pick from remaining choices

    for item in word_list:
        print(item, end=" ")  #prints item along with a space

    print()



rearrange(words_input, words_num)

print("the " + word_list[0] + " dog sat there next to the " + word_list[1] + " peterodactyl friend of his who he had noticed watching the " + word_list[2] + " cat who napped down the street by the " + word_list[3] + " Deli" )
