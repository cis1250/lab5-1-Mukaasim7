#!/usr/bin/env python3
import re
import string


def is_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False
    if not text[0].isupper():
        return False
    if not re.search(r'[.!?]$', text):
        return False
    if not re.search(r'\w+', text):
        return False
    return True


def get_sentence():
    while True:
        sentence = input("Enter a sentence: ")
        if is_sentence(sentence):
            return sentence
        print("This does not meet the criteria for a sentence.")


def calculate_frequencies(sentence):
    translator = str.maketrans("", "", string.punctuation)
    words = sentence.lower().translate(translator).split()

    word_list = []
    freq_list = []

    for w in words:
        if w in word_list:
            idx = word_list.index(w)
            freq_list[idx] += 1
        else:
            word_list.append(w)
            freq_list.append(1)

    return word_list, freq_list


def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)


if __name__ == "__main__":
    main()
