---
layout: default_paper
id: 790
order: 171
poster_session: 4
session_id: 11
title: "MDA-Net: Memorable Domain Adaptation Network for Monocular Depth Estimation"
authors:
  - author: "Jing  Zhu (New York University)"
  - author: "Yunxiao Shi (New York University)"
  - author: "Mengwei Ren (New York University)"
  - author: "Yi Fang (New York University)"
all_authors: "Jing  Zhu, Yunxiao Shi, Mengwei Ren and Yi Fang"
code: ""
keywords:
  - word: "depth estimation"
  - word: "LSTM"
  - word: "autonomous driving"
  - word: "visual perception"
  - word: ""
paper: "papers/0790.pdf"
supp: ""
abstract: "Monocular depth estimation is a challenging task that aims to predict a corresponding depth map from a given single RGB image. Recent deep learning models have been proposed to predict the depth from the image by learning the alignment of deep features between the RGB image and the depth domains. In this paper, we present a novel approach, named Memorable Domain Adaptation Network (MDA-Net), to more effectively transfer domain features for monocular depth estimation by taking into account the common structure regularities (e.g., repetitive  structure  patterns,  planar  surfaces, symmetries) in domain adaptation. To this end, we introduce a new Structure-Oriented Memory (SOM) module to learn and memorize the structure-specific information between RGB image domain and the depth domain. More specifically, in the SOM module, we develop a Memorable Bank of Filters (MBF) unit to learn a set of filters that memorize the structure-aware image-depth residual pattern, and also an Attention Guided Controller (AGC) unit to control the filter selection in the MBF given image features queries. Given the query image feature, the trained SOM module is able to adaptively select the best customized filters for cross-domain feature transferring with an optimal structural disparity between image and depth. In summary, we focus on addressing this structure-specific domain adaption challenge by proposing a novel end-to-end multi-scale memorable network for monocular depth estimation. The experiments show that our MDA-Net demonstrates the superior performance compared to the existing supervised monocular depth estimation approaches on the challenging KITTI and NYU Depth V2 benchmarks."
slides-id: 38934033
channel-id: "paper_171_P4_id_0790"
---
