---
layout: default_paper
id: 79
order: 165
poster_session: 4
session_id: 11
title: "On the Exploration of Incremental Learning for Fine-grained Image Retrieval"
authors:
  - author: "Wei Chen (Leiden University)"
  - author: "Yu Liu (KU Leuven)"
  - author: "Weiping Wang (National University of Defense Technology)"
  - author: "Tinne Tuytelaars (KU Leuven)"
  - author: "Erwin M. Bakker (Leiden University)"
  - author: "Michael Lew (Leiden Institute of Advanced Computer Science)"
all_authors: "Wei Chen, Yu Liu, Weiping Wang, Tinne Tuytelaars, Erwin M. Bakker and Michael Lew"
code: ""
keywords:
  - word: "Incremental learning"
  - word: "Fine-grained image retrieval"
  - word: "Catastrophic forgetting"
  - word: "Maximum Mean Discrepancy"
paper: "papers/0079.pdf"
supp: "supp/0079_supp.zip"
abstract: "In this paper, we consider the problem of fine-grained image retrieval in an incremental setting, when new categories are added over time. On the one hand, repeatedly training the representation on the extended dataset is time-consuming. On the other hand, fine-tuning the learned representation only with the new classes leads to catastrophic forgetting. To this end, we propose an incremental learning method to mitigate retrieval performance degradation caused by the forgetting issue. Without accessing any samples of the original classes, the classifier of the original network provides soft “labels” to transfer knowledge to train the adaptive network, so as to preserve the previous capability for classification. More importantly, a regularization function based on Maximum Mean Discrepancy is devised to minimize the discrepancy of new classes features from the original network and the adaptive network, respectively. Extensive experiments on two datasets show that our method effectively mitigates the catastrophic forgetting on the original classes while achieving high performance on the new classes."
slides-id: 38933880
channel-id: "paper_165_P4_id_0079"
---
