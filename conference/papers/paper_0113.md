---
layout: default_paper
id: 113
order: 48
poster_session: 1
session_id: 2
title: "STQ-Nets: Unifying Network Binarization and Structured Pruning"
authors:
  - author: "Aurobindo Munagala (IIIT Hyderabad)"
  - author: "Ameya Prabhu (University of Oxford)"
  - author: "Anoop Namboodiri (IIIT Hyderabad)"
all_authors: "Aurobindo Munagala, Ameya Prabhu and Anoop Namboodiri"
code: ""
keywords:
  - word: "quantization"
  - word: "binary networks"
  - word: "binarization"
  - word: "pruning"
  - word: "compression"
  - word: "inference"
  - word: ""
paper: "papers/0113.pdf"
supp: ""
abstract: "We discuss a formulation for network compression combining two major paradigms: binarization and pruning. Past works on network binarization have demonstrated that networks are robust to the removal of activation/weight magnitude information, and can perform comparably to full-precision networks with signs alone. Pruning focuses on generating efficient and sparse networks. Both compression paradigms aid deployment in portable settings, where storage, compute and power are limited. 

We argue that these paradigms are complementary, and can be combined to offer high levels of compression and speedup without any significant accuracy loss. Intuitively, weights/activations closer to zero have higher binarization error making them good candidates for pruning. Our proposed formulation incorporates speedups from binary convolution algorithms through structured pruning, enabling the removal of pruned parts of the network entirely post-training, beating previous works attempting the same by a significant margin. Overall, our method brings up to 89x layer-wise compression over the corresponding full-precision networks --  achieving only 0.33% loss on CIFAR-10 with ResNet-18 with a 40% PFR (Prune Factor Ratio for filters), and 0.3% on ImageNet with ResNet-18 with a 19% PFR."
slides-id: 38933891
channel-id: "paper_048_P1_id_0113"
---
