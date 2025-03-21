---
layout: default_paper
id: 479
order: 70
poster_session: 2
session_id: 5
title: "Making L-BFGS Work with Industrial-Strength Nets"
authors:
  - author: "Abhay Yadav (University of Maryland)"
  - author: "Tom Goldstein (University of Maryland, College Park)"
  - author: "David Jacobs (University of Maryland, USA)"
all_authors: "Abhay Yadav, Tom Goldstein and David Jacobs"
code: ""
keywords:
  - word: "deep network training"
  - word: "efficient training"
  - word: "second-order optimization"
  - word: ""
paper: "papers/0479.pdf"
supp: "supp/0479_supp.pdf"
abstract: "L-BFGS has been one of the most popular methods for convex optimization, but good performance by L-BFGS in deep learning has been elusive.
Recent work has modified L-BFGS for deep networks for classification tasks and been able to show performance competitive with SGD and Adam (the most popular current algorithms) when batch normalization is not used. 
However, this work cannot be applied with batch normalization. Since batch normalization is a defacto standard and important to good performance in deep networks, this still limits the use of L-BFGS. In this paper, we address this issue. Our proposed method can be used as a drop-in replacement without changing existing code. The proposed method performs consistently better than Adam and existing L-BFGS approaches, and comparable to carefully tuned SGD. We show results on three datasets, CIFAR-10, CIFAR-100, and STL-10 using three different popular deep networks ResNet, DenseNet and Wide ResNet. This work marks another significant step towards making L-BFGS 
competitive in the deep learning community."
slides-id: 38933985
channel-id: "paper_070_P2_id_0479"
---
