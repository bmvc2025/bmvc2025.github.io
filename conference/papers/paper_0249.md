---
layout: default_paper
id: 249
order: 104
oral_session: 6
poster_session: 3
session_id: 7
title: "Multi-label Zero-shot Classification by Learning to Transfer from External Knowledge"
authors:
  - author: "He Huang (University of Illinois at Chicago)"
  - author: "Wei Tang (University of Illinois at Chicago)"
  - author: "Philip  Yu (UIC)"
  - author: "Yuanwei Chen (Alibaba Group)"
  - author: "Wenhao Zheng (Alibaba Group)"
  - author: "Qing-Guo Chen (Alibaba)"
all_authors: "He Huang, Wei Tang, Philip  Yu, Yuanwei Chen, Wenhao Zheng and Qing-Guo Chen"
code: ""
keywords:
  - word: "zero-shot learning"
  - word: "graph neural networks"
  - word: "multi-label classification"
paper: "papers/0249.pdf"
supp: ""
abstract: "Multi-label zero-shot classification aims to predict multiple unseen class labels for an input image. It is more challenging than its single-label counterpart. On one hand, the unconstrained number of labels assigned to each image makes the model more easily overfit to those seen classes. On the other hand, there is a large semantic gap between seen and unseen classes in the existing multi-label classification datasets. To address these difficult issues, this paper introduces a novel multi-label zero-shot classification framework by learning to transfer from external knowledge. We observe that ImageNet is commonly used to pretrain the feature extractor and has a large and fine-grained label space. This motivates us to exploit it as external knowledge to bridge the seen and unseen classes and promote generalization. Specifically, we construct a knowledge graph including not only classes from the target dataset but also those from ImageNet. Since ImageNet labels are not available in the target dataset, we propose a novel PosVAE module to infer their initial states in the extended knowledge graph. Then we design a relational graph convolutional network (RGCN) to propagate information among classes and achieve knowledge transfer. Experimental results on two benchmark datasets demonstrate the effectiveness of the proposed approach."
slides-id: 38933931
channel-id: "paper_104_P3_id_0249"
---
