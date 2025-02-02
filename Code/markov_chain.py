from random import randrange
from dictogram import Dictogram
from dictionary_words import open_file

def get_pairs(words):
    """Make a list of tuples of adjacent words."""
    list = []
    for i in range(len(words) - 1):
        tuple = words[i], words[i+1]
        list.append(tuple)
    return list

def markov_chain(pairs):
    """Make a dictionary of markov chains."""
    words_dict = {}
    for pair in pairs:
        if pair[0] in words_dict.keys():
            if pair[1] in words_dict[pair[0]].keys():
                words_dict[pair[0]][pair[1]] += 1
            else:
                words_dict[pair[0]][pair[1]] = 1
        else:
            dict = {pair[1]: 1}
            words_dict[pair[0]] = dict

    for key in words_dict:
        words_dict[key] = Dictogram(words_dict[key])

    return words_dict

def generate_sentences(markov_chain, word_num):
    sentences = []
    list_keys = list(markov_chain)
    rand_num = randrange(len(list_keys))
    sentences.append(list_keys[rand_num])
    for i in range(word_num):
        sentences.append(markov_chain[sentences[i]].sample())

    return ' '.join(sentences)


if __name__ == "__main__":

    words = open_file('siddhartha.txt')
    print(markov_chain(get_pairs(words)))
    print(generate_sentences(markov_chain(get_pairs(words)), 30))
