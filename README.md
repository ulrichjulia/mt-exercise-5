# MT Exercise 5: Byte Pair Encoding, Beam Search

This repo is just a collection of scripts showing how to install [JoeyNMT](https://github.com/joeynmt/joeynmt), download
data and train & evaluate models.

# Requirements


# Steps

Clone this repository in the desired place:

    git clone https://github.com/emmavdbold/mt-exercise-5

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

# Findings

All using k = 5 for beam search.

| Use BPE | Vocabulary Size | BLEU |
| :---         |     :---:      |          ---: |
| no   | 5000     | 12.98    |
| yes     | 5000       | 19.49      |
| yes     | 1500       | 2.50      |
