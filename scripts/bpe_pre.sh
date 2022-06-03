#! /bin/bash
# preparing the bpe model

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data
models=$base/models

mkdir -p $data/bpe
mkdir -p $models/bpe

# combine all files to create bpe vocabulary

cat data/dev.en-it.it data/train.en-it.it data/test.en-it.it > data/combined_for_bpe.it
cat data/dev.en-it.it data/train.en-it.en data/test.en-it.en > data/combined_for_bpe.en

# learn a joint bpe model
subword-nmt learn-joint-bpe-and-vocab --input data/combined_for_bpe.en data/combined_for_bpe.it --write-vocabulary data/bpe/bpe_vocab_en data/bpe/bpe_vocab_it -s 5000 --total-symbols -o data/bpe/bpe_model_en-it

# apply models individually to texts
# NOTE: had to make changes to the apply-bpe script since I kept running into error messages
for text in $(echo test; echo train; echo dev);
do
  for lang in $(echo it; echo en);
  do
    subword-nmt apply-bpe -c data/bpe/bpe_model_en-it --vocabulary data/bpe/bpe_vocab_$lang --vocabulary-threshold 10 < data/$text.en-it.$lang > data/bpe/$text.bpe.en-it.$lang
  done
done

# build vocab file
python tools/joeynmt/scripts/build_vocab.py data/bpe/train.bpe.en-it.en data/bpe/train.bpe.en-it.it --output_path data/bpe/bpe_vocab.en-it


