---
layout: default_paper
id: 928
order: 90
poster_session: 2
session_id: 5
title: "Mish: A Self Regularized Non-Monotonic Activation Function"
authors:
  - author: "Diganta Misra (Kalinga Institute of Industrial Technology)"
all_authors: "Diganta Misra"
code: "https://github.com/digantamisra98/Mish"
keywords:
  - word: "activation functions"
  - word: "non-linear dynamics"
  - word: "loss landscapes"
  - word: ""
paper: "papers/0928.pdf"
supp: ""
abstract: "We propose Mish, a novel self-regularized non-monotonic activation function which can be mathematically defined as: f(x) = xtanh(softplus(x)). As activation functions play a crucial role in the performance and training dynamics in neural networks, we validated experimentally on several well-known benchmarks against the best combinations of architectures and activation functions. We also observe that data augmentation techniques have a favorable effect on benchmarks like ImageNet-1k and MS-COCO across multiple architectures. For example, Mish outperformed Leaky ReLU on YOLOv4 with a CSP-DarkNet-53 backbone on average precision (AP-50 val) by 2.1% in MS-COCO object detection and ReLU on ResNet-50 on ImageNet-1k in Top-1 accuracy by 1% while keeping all other network parameters and hyperparameters constant. Furthermore, we explore the mathematical formulation of Mish in relation with the Swish family of functions and propose an intuitive understanding on how the first derivative behavior may be acting as a regularizer helping the optimization of deep neural networks. Code is publicly available at https://github.com/digantamisra98/Mish."
slides-id: 38934052
channel-id: "paper_090_P2_id_0928"
---
