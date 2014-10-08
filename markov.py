#!/usr/bin/env python

from sys import argv
import random

def make_markov_chain(input_text):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # list_of_text = list(input_text)
    # list_of_text = [line.replace("\n", " ") for line in list_of_text]
    # print "".join(list_of_text)

    markov_chain = {}
    text = input_text.read().split()
    for word_index in range(len(text) - 2):
        key = (text[word_index], text[word_index + 1])
        value = text[word_index + 2]
        markov_chain.setdefault(key, []).append(value)
    return markov_chain

def make_text(markov_chain):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # randomly selects a key of words to start with, if the first word starts with a capital letter
    text_seed = random.choice(filter(lambda x: x[0][0].isupper(), markov_chain.keys()))
    # print text_seed
    # start the sentence off, with the first two words
    sentence = [text_seed[0], text_seed[1]]

    # as long as our key is still in the dictionary
    while text_seed in markov_chain:
        if text_seed[1][-1] in ".?!":
            break
        # randomly choose the word from the value options
        next_word = random.choice(markov_chain[text_seed])
        # add that word to the sentence
        sentence.append(next_word)
        # set the next word pair
        text_seed = (text_seed[1], next_word)
    return " ".join(sentence)

def main(filename):

    input_text = open(filename)

    chain_dict = make_markov_chain(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    script, filename = argv
    main(filename)