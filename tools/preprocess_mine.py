import logging, argparse, sys

from collections import Counter
from itertools import chain

from nltk.tokenize import word_tokenize


def tokenize(infile):
    if str(infile).endswith('it'):
        language = 'it'
    elif str(infile).endswith('en'):
        language = 'en'
    with open(infile, 'r+', encoding='utf-8') as infile:
        infile = infile.read()
        tokenized = word_tokenize(infile, language=language)
        return tokenized


def main():
    logging.basicConfig(level=logging.DEBUG)
    text = sys.stdin
    all_tokens = tokenize(text)

    flat_tokens = chain.from_iterable(all_tokens)

    counter = Counter(flat_tokens)

    # try to free up memory early

    del flat_tokens
    vocabulary = [token for token, frequency in counter.most_common(5000)]

    for tokens in all_tokens:
        output_tokens = []
        for token in tokens:
            if token in vocabulary:
                output_tokens.append(token)

        output_string = " ".join(output_tokens)
        sys.stdout.write(output_string + "\n")


if __name__ == '__main__':
    main()