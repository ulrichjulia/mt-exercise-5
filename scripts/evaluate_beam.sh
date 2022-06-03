#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data
configs=$base/configs

translations=$base/translations

mkdir -p $translations

src=en
trg=it
beam=35

# cloned from https://github.com/bricksdont/moses-scripts

num_threads=4
device=0

# measure time

SECONDS=0

model_name=transformer_sample_config_subword_15k_$beam

echo "###############################################################################"
echo "model_name $model_name"

translations_sub=$translations/$model_name

mkdir -p $translations_sub

CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python3 -m joeynmt translate configs/$model_name.yaml < data/test.en-it.$src > translations/$model_name/test.$model_name.it

# undo BPE

cat translations/$model_name/test.$model_name.$trg | sed 's/\@\@ //g' > translations/$model_name/test.tokenized.$model_name.$trg

cat translations/$model_name/test.tokenized.$model_name.$trg | sacremoses detokenize > translations/$model_name/test.$model_name.nt.$trg

cat translations/$model_name/test.$model_name.nt.it | sacrebleu data/test.en-it.it

echo "time taken:"
echo "$SECONDS seconds"
