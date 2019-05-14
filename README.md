# EstSimLex-999

All the results from the models and the EstSimLex-999 data set can be accessed [here](https://docs.google.com/spreadsheets/d/12IWabZzPIn0QvetZJvxAshZPX_g0fhoLh1g6OYYSZ0E/edit#gid=0). 


## Description of used models

Three families of computational models were evaluated in this thesis. Almost all the code can be accessed from this GitHUb repository, except code for convolutional autoencoder. Next, it is shown were the used resources can be found and how the similarity between concept pairs from EstSimLex-999 were calculated. 

## Distributional models

All the used distributional models can be downloaded online. 
1. Eleri Aedmaa's word and sense vectors can be downloaded [here](https://github.com/eleriaedmaa/embeddings).
2. Estnltk models can be downloaded [here](https://github.com/estnltk/word2vec-models).
3. Facebook research models can be downloaded [here](https://github.com/facebookresearch/fastText/blob/master/docs/crawl-vectors.md).

To use sense vectors it is necessary to install [SenseGram](https://github.com/uhh-lt/sensegram).

Used similarity metric is cosine similarity between word ans sense vectors. 

## Semantic networks

Two semantic networks were used: Estonian Wordnet and Estonian Wikipedia bitaxonomy. 
Wordnet version 2.2 can be downloaded [here](https://gitlab.keeleressursid.ee/avalik/data/blob/master/estwn/estwn-et-2.2.0.xml).
Wikipedia bitaxonomy is not publicly available, but this taxonomy can be accessed online - [MultiWiBi](http://wibitaxonomy.org/).

Three path-based similarity measures were implemented: path similarity, Leacock & Chodorow and Wu & Palmer. 

## Computer vision models 

Used code for implementing convolutional autoencoder can be accessed [here](https://github.com/ankonzoid/artificio/tree/master/image_retrieval). This code was changed a bit to met the needs of this work. 

Pre-trained ResNet-18 was accessed through PyTorch subpackage torchvision.models. Documentation for that can be found [here](https://pytorch.org/docs/stable/torchvision/models.html).

Similarity between embeddings were calculated as the cosine similarity. 

