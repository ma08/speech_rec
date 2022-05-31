## Abstract

This project aims to develop an open-source baseline Automatic
Speech Recognition (ASR) pipeline for the Dravidian languages Tamil
and Telugu. We propose to use different speech datasets to train time-delayed
neural networks. As the total size of usable Telugu speech data (45 hours) from
these sources doesn't quite fit the requirement to achieve reasonable
performance levels, we investigate the application of transfer learning from
another Dravidian language, Tamil for which the data is relatively much more accessible. 
We present an end-to-end pipeline of taking a raw text corpus for the language model and
generating a clean dataset along with a simple tool to verify its quality.
Finally, a customized Kaldi recipe is developed by modifying the TEDLIUM one
to build the language model and train a time-delayed neural network for the acoustic modeling
using cleansed datasets and evaluate the performance of the models. In this evaluation, we also investigate the success of
using transfer learning from Tamil and English to Telugu. We aim to contribute to the low-resource open-source
ASR world and the general Speech Recognition and NLP ecosystem by publishing the
tools and techniques used in this project as a modular library after sufficient
testing and iterations.

## Folder Structure
- [Dataset Related](dataset_related/) Preprocessing and utility scripts for the speech datasets to create input data files for kaldi.
- [Language Model](dataset_related/) Preprocessing and utility scripts for  language corpora for building Language Models.
- [Kaldi Recipe](https://github.com/ma08/kaldi_tamtel/) Kaldi recipes repo used in this project.
- [Kaldi DB](https://github.com/ma08/kaldi_tamtel_db/) Repository that maintains history of some of Kaldi data files to track changes across different stages. 
  - TODO: Explore git-lfs to store all data files for more comprehensive versioning.
- [Documents](documents/) Documents written for this project.
