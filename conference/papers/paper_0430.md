---
layout: default_paper
id: 430
order: 7
oral_session: 2
poster_session: 1
session_id: 1
title: "Weakly-supervised Salient Instance Detection"
authors:
  - author: "Xin Tian (Dalian University of Technology, City University of Hong Kong)"
  - author: "Ke Xu (Dalian University of Technology, City University of Hong Kong)"
  - author: "Xin Yang (Dalian University of Technology)"
  - author: "Baocai Yin (Dalian University of Technology)"
  - author: "Rynson Lau (City University of Hong Kong)"
all_authors: "Xin Tian, Ke Xu, Xin Yang, Baocai Yin and Rynson Lau"
code: ""
keywords:
  - word: "Salient Instance Detection"
  - word: "SID"
  - word: "weak supervision"
  - word: "saliency detection"
  - word: "subitizing"
  - word: ""
paper: "papers/0430.pdf"
supp: "supp/0430_supp.zip"
abstract: "Existing salient instance detection (SID) methods typically learn from pixel-level annotated datasets. In this paper, we present the first weakly-supervised approach to the SID problem. Although weak supervision has been considered in general saliency detection, it is mainly based on using class labels for object localization. However, it is non-trivial to use only class labels to learn instance-aware saliency information, as salient instances with high semantic affinities may not be easily separated by the labels. We note that subitizing information provides an instant judgement on the number of salient items, which naturally relates to detecting salient instances and may help separate instances of the same class while grouping different parts of the same instance. Inspired by this insight, we propose to use class and subitizing labels as weak supervision for the SID problem. We propose a novel weakly-supervised network with three branches: a Saliency Detection Branch leveraging class consistency information to locate candidate objects; a Boundary Detection Branch exploiting class discrepancy information to delineate object boundaries; and a Centroid Detection Branch using subitizing information to detect salient instance centroids. This complementary information is further fused to produce salient instance maps. We conduct extensive experiments to demonstrate that the proposed method plays favorably against carefully designed baseline methods adapted from related tasks."
slides-id: 38933972
channel-id: "paper_007_P1_id_0430"
---
