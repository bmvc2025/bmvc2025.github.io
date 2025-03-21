---
layout: default_paper
id: 772
order: 84
poster_session: 2
session_id: 5
title: "From Saturation to Zero-Shot Visual Relationship Detection Using Local Context"
authors:
  - author: "Nikolaos Gkanatsios (DeepLab)"
  - author: "Vassilis Pitsikalis (DeepLab)"
  - author: "Petros Maragos (National Technical University of Athens)"
all_authors: "Nikolaos Gkanatsios, Vassilis Pitsikalis and Petros Maragos"
code: "https://github.com/deeplab-ai/zs-vrd-bmvc20"
keywords:
  - word: "Visual Relationship Detection"
  - word: "Scene Graph Generation"
  - word: "Zero-shot Classification"
  - word: "Local Context"
  - word: "Language Bias"
  - word: ""
paper: "papers/0772.pdf"
supp: ""
abstract: "Visual relationship detection has been motivated by the ``insufficiency of objects to describe rich visual knowledge''. However, we find that training and testing on current popular datasets may not support such statements; most approaches can be outperformed by a naive image-agnostic baseline that fuses language and spatial features. We visualize the errors of numerous existing detectors, to discover that most of them are caused by the coexistence and penalization of antagonizing predicates that could describe the same interaction. Such annotations hurt the dataset's causality and models tend to overfit the dataset biases, resulting in a saturation of accuracy to artificially low levels.
		
We construct a simple architecture and explore the effect of using language on generalization. Then, we introduce adaptive local-context-aware classifiers, that are built on-the-fly based on the objects' categories. To improve context awareness, we mine and learn predicate synonyms, i.e. different predicates that could equivalently hold, and apply a distillation-like loss that forces synonyms to have similar classifiers and scores. The last also serves as a regularizer that mitigates the dominance of the most frequent classes, enabling zero-shot generalization. We evaluate predicate accuracy on existing and novel test scenarios to display state-of-the-art results over prior biased baselines."
slides-id: 38934028
channel-id: "paper_084_P2_id_0772"
---
