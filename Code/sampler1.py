import random

def histo(phrase):
    dict_hist = {}
    for word in phrase:
        if word not in dict_hist:
            dict_hist[word] = 1
        else:
            dict_hist[word] += 1
    return dict_hist

def sample_test(histo):
    words = []
    for _ in range(0, 10000):
        words.append(sample(test))
    hist = count_words(words)
    print(hist)


def frequency_sample(dict_hist):
    tokens = sum(dict_hist.values())
    ran_num = random.uniform(0, tokens)
    num = 0
    for word in dict_hist:
        count = dict_hist[word]
        num += count
        if num > ran_num:
            return word

if __name__ == '__main__':
    phrase = histo("one fish two fish red fish blue fish".split(" "))
    sample_list = 'garfield ant hobbes'.split()
    cats = histo(sample_list)
    print(phrase)
    words = []
    for _ in range(0, 100):
        words.append(frequency_sample(phrase))

    print(histo(words))
