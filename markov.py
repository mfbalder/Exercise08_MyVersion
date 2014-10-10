#!/usr/bin/env python

from sys import argv
import random


def assemble_dictionary(list_of_opened_files):
    """Takes a list of opened files, cleans them up, and adds them to a dictionary"""

    def clean_file(input_file):
        cleaned_text = input_file.read().split()
        for word in cleaned_text:
            word.strip(',()[]')
        return cleaned_text

    def add_file_to_dict(cleaned_text):
        for word_index in range(len(cleaned_text) - 2):
            key = (cleaned_text[word_index], cleaned_text[word_index + 1])
            value = cleaned_text[word_index + 2]
            markov_chain.setdefault(key, []).append(value)

    markov_chain = {}
    for each_file in list_of_opened_files:
        cleaned_text = clean_file(each_file)
        add_file_to_dict(cleaned_text)
    return markov_chain

def assemble_text(chain):
    """Takes a dictionary of markov chains as input, and returns a random text"""
    start = random.choice(filter(lambda x: x[0][0].isupper(), chain.keys()))
    sentence = [start[0], start[1]]
    while start in chain.keys():
        next_word = random.choice(chain[start])
        sentence.append(next_word)
        if next_word[-1] in ".?":
            break
        start = (sentence[-2], sentence[-1])

    return " ".join(sentence)


def main(files):
    # for each file that the user passes as an argument, open it and process it
    opened_files = [open(file_name) for file_name in files]
    markov_chain = assemble_dictionary(opened_files)
    print assemble_text(markov_chain)

if __name__ == "__main__":
    files = argv[1:]
    main(files)