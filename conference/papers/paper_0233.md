---
layout: default_paper
id: 233
order: 172
poster_session: 4
session_id: 11
title: "Making a Case for 3D Convolutions for Object Segmentation in Videos"
authors:
  - author: "Sabarinath Mahadevan (RWTH Aachen University)"
  - author: "Ali Athar (RWTH Aachen)"
  - author: "Aljosa Osep (TUM Munich)"
  - author: "Laura Leal-Taixé (TUM)"
  - author: "Bastian Leibe (RWTH Aachen University-)"
  - author: "Sebastian Hennen (RWTH Aachen)"
all_authors: "Sabarinath Mahadevan, Ali Athar, Aljosa Osep, Laura Leal-Taixé, Bastian Leibe and Sebastian Hennen"
code: "https://github.com/sabarim/3DC-Seg"
keywords:
  - word: "object tracking"
  - word: "video segmentation"
  - word: "video object segmentation"
  - word: "video scene understanding"
  - word: "object segmentation"
paper: "papers/0233.pdf"
supp: "supp/0233_supp.zip"
abstract: "The task of object segmentation in videos is usually accomplished by processing appearance and motion information separately using standard 2D convolutional networks, followed by a learned fusion of the two sources of information. On the other hand, 3D convolutional networks have been successfully applied for video classification tasks, but have not been leveraged as effectively to problems involving dense per-pixel interpretation of videos compared to their 2D convolutional counterparts and lag behind the aforementioned networks in terms of performance. In this work, we show that 3D CNNs can be effectively applied to dense video prediction tasks such as salient object segmentation. We propose a simple yet effective encoder-decoder network architecture consisting entirely of 3D convolutions that can be trained end-to-end using a standard cross-entropy loss. To this end, we leverage an efficient 3D encoder, and propose a 3D decoder architecture, that comprises novel 3D Global Convolution layers and 3D Refinement modules. Our approach outperforms existing state-of-the-arts by a large margin on the DAVIS'16 Unsupervised, FBMS and ViSal dataset benchmarks in addition to being faster, thus showing that our architecture can efficiently learn expressive spatio-temporal features and produce high quality video segmentation masks. We have made our code and trained models publicly available at: https://github.com/sabarim/3DC-Seg"
slides-id: 38933926
channel-id: "paper_172_P4_id_0233"
---
