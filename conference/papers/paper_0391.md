---
layout: default_paper
id: 391
order: 160
poster_session: 4
session_id: 11
title: "Refinement of Boundary Regression Using Uncertainty in Temporal Action Localization"
authors:
  - author: "Yunze Chen (Center of Precision Sensing and Control, Institute of Automation, Chinese Academy of Sciences, School of Artificial Intelligence, University of Chinese Academy of Sciences)"
  - author: "Mengjuan Chen (Center of Precision Sensing and Control, Institute of Automation, Chinese Academy of Sciences)"
  - author: "Rui Wu (Horizon Robotics)"
  - author: "Jiagang Zhu (Institute of Automation, Chinese Academy of Sciences, University of Chinese Academy of Sciences )"
  - author: "Zheng Zhu (Institute of Automation, Chinese Academy of Sciences)"
  - author: "Qingyi Gu (Institute of Automation, Chinese Academy of Sciences)"
all_authors: "Yunze Chen, Mengjuan Chen, Rui Wu, Jiagang Zhu, Zheng Zhu and Qingyi Gu"
code: ""
keywords:
  - word: "Temporal Action Localization"
  - word: "Temporal Action Detection"
  - word: "Activity recognition and understanding"
  - word: ""
paper: "papers/0391.pdf"
supp: ""
abstract: "Boundary localization is a key component of most temporal action localization frameworks for untrimmed video. Deep-learning methods have brought remarkable progress in this field due to large-scale annotated datasets (e.g., THUMOS14 and ActivityNet). However, natural ambiguity exists for labeling accurate action boundary with such datasets. In this paper, we propose a method to model this uncertainty. Specifically, we construct a Gaussian model for predicting the uncertainty variance of boundary. The captured variance is further used to select more reliable proposals, and to refine proposal boundary by variance voting during post-processing. For most existing one- and two-stage frameworks, more accurate boundaries and reliable proposals can be obtained without additional computation. For the one-stage decoupled single-shot temporal action detection (Decouple-SSAD) framework, we first apply adaptive pyramid feature fusion method to fuse its features of different scales and optimize its structure. Then, we introduce the uncertainty based method, and improve state-of-the-art mAP@0.5 value from 37.9% to 41.6% on THUMOS14. Moreover, for the two-stage proposal–proposal interaction through a graph convolutional network (P-GCN), with such uncertainty method, we also gain significant improvements on both THUMOS14 and ActivityNet v1.3 datasets."
slides-id: 38933963
channel-id: "paper_160_P4_id_0391"
---
