---
layout: default_paper
id: 817
order: 93
poster_session: 2
session_id: 5
title: "Paying more Attention to Snapshots of Iterative Pruning: Improving Model Compression via Ensemble Distillation"
authors:
  - author: "Duong Le (Ho Chi Minh City University of Technology)"
  - author: "Nhan Vo  (Ho Chi Minh City University of Technology	)"
  - author: "Nam Thoai (Ho Chi Minh City University of Technology	)"
all_authors: "Duong Le, Nhan Vo and Nam Thoai"
code: "https://github.com/lehduong/kesi"
keywords:
  - word: "network pruning"
  - word: "knowledge distillation"
  - word: "ensemble learning"
  - word: ""
paper: "papers/0817.pdf"
supp: "supp/0817_supp.zip"
abstract: "  Network pruning is one of the most dominant methods for reducing the heavy inference cost of deep neural networks. Existing methods often iteratively prune networks to attain high compression ratio without incurring significant loss in performance. However, we argue that conventional methods for retraining pruned networks (i.e., using small, fixed learning rate) are inadequate as they completely ignore the benefits from snapshots of iterative pruning. In this work, we show that strong ensembles can be constructed from snapshots of iterative pruning, which achieve competitive performance and vary in network structure.  Furthermore, we present a simple, general and effective pipeline that generates strong ensembles of networks during pruning with textit{large learning rate restarting}, and utilizes knowledge distillation with those ensembles to improve the predictive power of compact models. In standard image classification benchmarks such as CIFAR and Tiny-Imagenet, we advance state-of-the-art pruning ratio of structured pruning by integrating simple $ell_1$-norm filters pruning into our pipeline. Specifically, we reduce 75-80% of total parameters and 65-70% MACs of numerous variants of ResNet architectures while having comparable or better performance than that of original networks. "
slides-id: 38934038
channel-id: "paper_093_P2_id_0817"
---
