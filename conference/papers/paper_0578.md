---
layout: default_paper
id: 578
order: 170
poster_session: 4
session_id: 11
title: "Learning Effectively from Noisy Supervision for Weakly Supervised Semantic Segmentation"
authors:
  - author: "Wenbin Xie (Tsinghua University)"
  - author: "Qiaoqiao Wei (Tsinghua University)"
  - author: "Zheng Li (Tsinghua University)"
  - author: "Hui Zhang (Tsinghua University)"
all_authors: "Wenbin Xie, Qiaoqiao Wei, Zheng Li and Hui Zhang"
code: ""
keywords:
  - word: "Semantic Segmentation"
  - word: "Weakly Supervised Semantic Segmentation"
  - word: "Self Attention"
paper: "papers/0578.pdf"
supp: "supp/0578_supp.pdf"
abstract: "Semantic segmentation based on deep learning has undergone tremendous progress in recent years. However, it continues to depend heavily on massive densely annotated data.  In this paper, we propose a novel framework for weakly supervised semantic segmentation (WSSS) using bounding boxes to alleviate the need for pixel-wise annotations. We argue that the most important problem of WSSS should be learning effectively from noisy supervision. Therefore, we present a constrained foreground segmentation network (CFS) to generate high-quality dense annotations from noisy proposals. The network converts the segmentation task from multi-class classification to two-class classification and removes most of irrelevant regions, making the task easier to optimize. Besides, we introduce a loss-guided self-attention (LGSA) module to encourage self-correcting among intra-class pixels. Instead of allowing global information exchanges in existing non-local networks, our module imposes loss constraints on the information exchanges between different categories and learns a more reasonable affinity matrix which can be used for further random walk. Experiments indicate that our LGSA module has better performance and interpretability even with noisy supervision. We obtain state-of-the-art results on the Pascal VOC 2012 validation set by combining the two novel components."
slides-id: 38934003
channel-id: "paper_170_P4_id_0578"
---
