---
layout: default_paper
id: 97
order: 188
poster_session: 4
session_id: 11
title: "N2NSkip: Learning Highly Sparse Networks using Neuron-to-Neuron Skip Connections"
authors:
  - author: "Arvind Subramaniam (Bits Pilani Hyderabad Campus)"
  - author: "Avinash Sharma (CVIT, IIIT-Hyderabad)"
all_authors: "Arvind Subramaniam and Avinash Sharma"
code: ""
keywords:
  - word: "model compression"
  - word: "pruning"
  - word: "heat diffusion"
  - word: "Convolutional Neural Networks (CNN)"
  - word: "undirected graphs"
  - word: "heat diffusion"
  - word: "skip connections"
  - word: "N2NSkip"
  - word: "scree diagram"
  - word: "connection sensitivity"
  - word: ""
paper: "papers/0097.pdf"
supp: ""
abstract: "The over-parametrized nature of Deep Neural Networks (DNNs) leads to considerable hindrances during deployment on low-end devices with time and space constraints. Network pruning strategies that sparsify DNNs using iterative prune-train schemes are often computationally expensive. As a result, techniques that prune at initialization, prior to training, have become increasingly popular. In this work, we propose neuron-to-neuron skip (N2NSkip) connections, which act as sparse weighted skip connections, to enhance the overall connectivity of pruned DNNs. Following a preliminary pruning step, N2NSkip connections are randomly added between individual neurons/channels of the pruned network, while maintaining the overall sparsity of the network. We demonstrate that introducing N2NSkip connections in pruned networks enables significantly superior performance, especially at high sparsity levels, as compared to pruned networks without N2NSkip connections. Additionally, we present a heat diffusion-based connectivity analysis to quantitatively determine the connectivity of the pruned network with respect to the reference network. We evaluate the efficacy of our approach on two different preliminary pruning methods which prune at initialization and consistently obtain superior performance by exploiting the enhanced connectivity resulting from N2NSkip connections."
slides-id: 38933886
channel-id: "paper_188_P4_id_0097"
---
