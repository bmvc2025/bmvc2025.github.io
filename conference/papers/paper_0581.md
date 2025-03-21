---
layout: default_paper
id: 581
order: 71
poster_session: 2
session_id: 5
title: "Rethinking Curriculum Learning with Incremental Labels and Adaptive Compensation"
authors:
  - author: "Madan Ravi Ganesh (University of Michigan)"
  - author: "Jason Corso (University of Michigan)"
all_authors: "Madan Ravi Ganesh and Jason Corso"
code: ""
keywords:
  - word: "label smoothing"
  - word: "curriculum learning"
  - word: "incremental labels"
  - word: "adaptive compensation"
  - word: "negative mining"
paper: "papers/0581.pdf"
supp: "supp/0581_supp.pdf"
abstract: "Like humans, deep networks have been shown to learn better when samples are organized and introduced in a meaningful order or curriculum. Conventional curriculum learning schemes introduce samples in their order of difficulty.  This forces models to begin learning from a subset of the available data while adding the external overhead of evaluating the difficulty of samples.  In this work, we propose Learning with Incremental Labels and Adaptive Compensation (LILAC), a two-phase method that incrementally increases the number of unique output labels rather than the difficulty of samples while consistently using the entire dataset throughout training.  In the first phase, Incremental Label Introduction, we partition data into mutually exclusive subsets, one that contains a subset of the ground-truth labels and another that contains the remaining data attached to a pseudo-label.  Throughout the training process, we recursively reveal unseen ground-truth labels in fixed increments until all the labels are known to the model. In the second phase, Adaptive Compensation, we optimize the loss function using altered target vectors for previously misclassified samples. The target vectors of such samples are modified to a smoother distribution to help models learn better. On evaluating across three standard image benchmarks, CIFAR-10, CIFAR-100, and STL-10, we show that LILAC outperforms all comparable baselines. Further, we detail the importance of pacing the introduction of new labels to a model as well as the impact of using a smooth target vector."
slides-id: 38934004
channel-id: "paper_071_P2_id_0581"
---
