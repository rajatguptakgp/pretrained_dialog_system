# Improving Dialog Systems with Pretrained Models



***
## Overview
This work is about exploring whether dialog systems can be improved with regards to context and natural langugage relevance through pretraining or not.

## Dependencies
 - PyTorch
 - TorchText
 - spaCy
 
 ## Installation
 - To install PyTorch, see installation instructions on the PyTorch website.
 - To install TorchText: `pip install torchtext`
 - To install spaCy: 
 ```
 pip install -U spacy
 python -m spacy download en_core_web_sm
 ```
 
## Dataset
This work makes use of the [DailyDialog Dataset](https://arxiv.org/abs/1710.03957). 

## Data Preprocessing
The data in original form is a raw text file with `_eou_` as the delimiter between any two sentences. 

### For Vanilla Seq2Seq
- Use the `make_data_vseq2seq.py` script to process the data splits (train, validation and test) into a CSV file.

### For HRED
- Use the `make_data_hred.py` script to process the data splits (train, validation and test) into a CSV file. Additional samples for each dialog have been created since they have generic responses and also because the number of dialogs is less, which may not be enough to train the model effectively. 

## Reference
* [PyTorch Seq2Seq](https://github.com/bentrevett/pytorch-seq2seq)
 
