#!/usr/bin/env python

from sys import argv
import random
import re


def assemble_dictionary(list_of_opened_files):
    """Takes a list of opened files, cleans them up, and adds them to a dictionary"""

    def clean_file(input_file):
        # text = input_file.read().split()
        # cleaned_text = [re.sub(r'[,?.]', '', word) for word in text]
        # return cleaned_text
        cleaned_text = []
        text = input_file.read().split()
        for word in text:
            word = re.sub(r'[,?.]', '', word)
            cleaned_text.append(word)
        # print cleaned_text
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
    start = random.choice(filter(lambda x: x[0][-1] not in ".", chain.keys()))
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
    final_sentence1 = assemble_text(markov_chain)
    final_sentence2 = assemble_text(markov_chain)
    while len(final_sentence1 + final_sentence2) > 140:
        final_sentence1 = assemble_text(markov_chain)
        final_sentence2 = assemble_text(markov_chain)
    print final_sentence1[0].upper() + final_sentence1[1:] + " " + final_sentence2[0].upper() + final_sentence2[1:]


if __name__ == "__main__":
    files = argv[1:]
    main(files)