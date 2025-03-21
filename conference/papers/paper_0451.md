---
layout: default_paper
id: 451
order: 121
poster_session: 3
session_id: 8
title: "Class Interference Regularization"
authors:
  - author: "Bharti Munjal (OSRAM)"
  - author: "Sikandar Amin (OSRAM GmbH)"
  - author: "Fabio Galasso (Sapienza University)"
all_authors: "Bharti Munjal, Sikandar Amin and Fabio Galasso"
code: ""
keywords:
  - word: "regularization"
  - word: "few-shot learning"
  - word: "person search"
  - word: "person re-identification"
  - word: "average embeddings"
  - word: "class interference"
  - word: "classification"
paper: "papers/0451.pdf"
supp: ""
abstract: "Contrastive losses yield state-of-the-art performance for person re-identification, face verification and few shot learning. They have recently outperformed the cross-entropy loss on classification at the ImageNet scale and outperformed all self-supervision prior results by a large margin (SimCLR). Simple and effective regularization techniques such as label smoothing and self-distillation do not apply anymore, because they act on multinomial label distributions, adopted in cross-entropy losses, and not on tuple comparative terms, which characterize the contrastive losses.

Here we propose a novel, simple and effective regularization technique, the Class Interference Regularization (CIR), which applies to cross-entropy losses but is especially effective on contrastive losses. CIR perturbs the output features by randomly moving them towards the average embeddings of the negative classes. To the best of our knowledge, CIR is the first regularization technique to act on the output features.

In experimental evaluation, the combination of CIR and a plain Siamese-net with
triplet loss yields best few-shot learning performance on the challenging tieredImageNet. CIR also improves the state-of-the-art technique in person re-identification on the Market-1501 dataset, based on triplet loss, and the state-of-the-art technique in person search on the CUHK-SYSU dataset, based on a cross-entropy loss. Finally, on the task of classification CIR performs on par with the popular label smoothing, as demonstrated for CIFAR-10 and -100.
"
slides-id: 38933979
channel-id: "paper_121_P3_id_0451"
---
