#! /bin/bash
# Working with the data downloaded via the download_iwslt_2017_data.sh script

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data

mkdir -p $data/cleaned

# preprocess slightly
for lang in $(echo it; echo en);
do
  for text in $(echo dev; echo train; echo test);
  do
    cat data/$text.en-it.$lang | python tools/preprocess.py > data/$text.en-it.$lang
  done
done

