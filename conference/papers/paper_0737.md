---
layout: default_paper
id: 737
order: 177
poster_session: 4
session_id: 11
title: "Reducing Label Noise in Anchor-Free Object Detection"
authors:
  - author: "Nermin Samet (Middle East Technical University)"
  - author: "Samet Hicsonmez (Hacettepe University)"
  - author: "Emre Akbas (Middle East Technical University)"
all_authors: "Nermin Samet, Samet Hicsonmez and Emre Akbas"
code: "https://github.com/nerminsamet/ppdet"
keywords:
  - word: "Object Detection"
  - word: "Anchor-Free"
  - word: "Prediction Pooling"
  - word: "Sum Pooling"
paper: "papers/0737.pdf"
supp: ""
abstract: "Current anchor-free object detectors label all the features that spatially fall inside a predefined central region of a ground-truth box as positive. This approach causes label noise during training, since some of these positively labeled features may be on the background or an occluder object, or they are simply not discriminative features. In this paper, we propose a new labeling strategy aimed to reduce the label noise in anchor-free detectors. We sum-pool predictions stemming from individual features into a single prediction. This allows the model to reduce the contributions of non-discriminatory features during training. We develop a new one-stage, anchor-free object detector, PPDet, to employ this labeling strategy during training and a similar prediction pooling method during inference. On the COCO dataset, PPDet achieves the best performance among anchor-free top-down detectors and performs on-par with the other state-of-the-art methods. It also outperforms all major one-stage and two-stage methods in small object detection (APs 31.4). Code is available at https://github.com/nerminsamet/ppdet."
slides-id: 38934023
channel-id: "paper_177_P4_id_0737"
---
