#! /bin/env/python
import sys
import time
import logging
import random

from collections import Counter
from itertools import chain

import nltk

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')

random.seed(42)

def main():

    tic = time.time()

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    lines = sys.stdin.readlines()

    all_tokens = []

    if len(lines) > 100000:
        logging.info(f"Reducing {len(lines)} to 100'000 lines.")
        sample_lines = random.sample(lines, 100000)
        logging.info(sample_lines[-10:])
        for line in sample_lines:
            t = line.split()
            all_tokens.append(t)

    else:
        for line in lines:
            t = line.split()
            all_tokens.append(t)

    flat_tokens = chain.from_iterable(all_tokens)

    counter = Counter(flat_tokens)

    del flat_tokens

    logging.info("Vocabulary size before/after/max_allowed = %d/%d/%d" % (len(counter.keys()), min(5000, len(counter.keys())), 5000))

    vocabulary = [token for token, frequency in counter.most_common(5000)]

    for tokens in all_tokens:
        output_tokens = []
        for token in tokens:
            if token in vocabulary:
                output_tokens.append(token)

        output_string = " ".join(output_tokens)
        sys.stdout.write(output_string + "\n")

    toc = time.time() - tic

    logging.info("Time taken: %f seconds" % toc)

if __name__ == '__main__':
    main()
