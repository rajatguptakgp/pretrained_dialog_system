# Improving Dialog Systems with Pretrained Models



***
## Overview
This work is about exploring whether dialog systems can be improved with regards to context and natural langugage relevance through pretraining or not.

## Results

| Description | Non-pretrained HRED  | Pretrained HRED  |
| :---:   | :-: | :-: |
| EPOCHS | 30 | 60 |
| Training PPL | 61.67 | 5.53 |
| Validation PPL | 278.75 | 813.49 |
| Test PPL | 284.11 | 593.11 |
| BLEU | 0.03 | 0.22 |

From the generated dialog responses, it is inferred that after pretraining, the problem of natural language generation goes away but context relevance still remains to be an issue.

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
 
