---
layout: default_paper
id: 621
order: 154
oral_session: 8
poster_session: 4
session_id: 10
title: "Learning from Counting: Leveraging Temporal Classification for Weakly Supervised Object Localization and Detection"
authors:
  - author: "Chia-Yu Hsu (Arizona State University)"
  - author: "Wenwen Li (Arizona State University)"
all_authors: "Chia-Yu Hsu and Wenwen Li"
code: ""
keywords:
  - word: "weakly supervised object detection"
  - word: "object detection"
  - word: "region proposal"
  - word: "weak supervision"
  - word: "MIL"
  - word: "WSOD"
  - word: ""
paper: "papers/0621.pdf"
supp: ""
abstract: "This paper reports a new solution of leveraging temporal classification to support weakly supervised object detection (WSOD). Specifically, we introduce raster scan-order techniques to serialize 2D images into 1D sequence data, and then leverage a combined LSTM (Long, Short-Term Memory) and CTC (Connectionist Temporal Classification) network to achieve object localization based on a total count (of interested objects). We term our proposed network LSTM-CCTC (Count-based CTC). This “learning from counting” strategy differs from existing WSOD methods in that our approach automatically identifies critical points on or near a target object. This strategy significantly reduces the need of generating a large number of candidate proposals for object localization. Experiments show that our method yields state-of-the-art performance based on an evaluation on PASCAL VOC datasets. 
"
slides-id: 38934007
channel-id: "paper_154_P4_id_0621"
---
