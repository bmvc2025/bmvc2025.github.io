---
layout: default_paper
id: 184
order: 53
oral_session: 3
poster_session: 2
session_id: 3
title: "Bipartite Conditional Random Fields for Panoptic Segmentation"
authors:
  - author: "Sadeep Jayasumana (University of Oxford)"
  - author: "Kanchana  Ranasinghe (University of Moratuwa)"
  - author: "Sahan Liyanaarachchi (University of Moratuwa)"
  - author: "Bethmage Mayuka Jayawardhana (University of Moratuwa)"
  - author: "Harsha Ranasinghe (University of Moratuwa)"
  - author: "Sina Samangooei (Five AI Ltd.)"
all_authors: "Sadeep Jayasumana, Kanchana  Ranasinghe, Sahan Liyanaarachchi, Bethmage Mayuka Jayawardhana, Harsha Ranasinghe and Sina Samangooei"
code: "https://github.com/sahan-liyanaarachchi/bcrf-detectron"
keywords:
  - word: "conditional random fields"
  - word: "panoptic segmentation"
  - word: "deep learning"
  - word: ""
paper: "papers/0184.pdf"
supp: "supp/0184_supp.pdf"
abstract: " We tackle the panoptic segmentation problem with a conditional random field (CRF) model. Panoptic segmentation involves assigning a semantic label and an instance label to each pixel of a given image. At each pixel, the semantic label and the instance label should be compatible. Furthermore, a good panoptic segmentation should have a number of other desirable properties such as the spatial and color consistency of the labeling. To tackle this problem, we propose a CRF model, named Bipartite CRF or BCRF, with two types of random variables for semantic and instance labels. In this formulation, various energies are defined within and across the two types of random variables to encourage a consistent panoptic segmentation. We propose a mean-field-based efficient inference algorithm for solving the CRF and empirically show its convergence properties. This algorithm is fully differentiable, and therefore, BCRF inference can be included as a trainable module in any deep network. In the experimental evaluation, we quantitatively and qualitatively show that the BCRF yields superior panoptic segmentation results in practice."
slides-id: 38933911
channel-id: "paper_053_P2_id_0184"
---
