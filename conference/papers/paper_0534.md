---
layout: default_paper
id: 534
order: 80
poster_session: 2
session_id: 5
title: "Anchor-free Small-scale Multispectral Pedestrian Detection"
authors:
  - author: "Alexander Wolpert ( Karlsruhe Institute of Technology)"
  - author: "Michael Teutsch (Hensoldt Optronics)"
  - author: "Saquib Sarfraz (Karlsruhe Institute of Technology)"
  - author: "Rainer Stiefelhagen (Karlsruhe Institute of Technology)"
all_authors: "Alexander Wolpert, Michael Teutsch, Saquib Sarfraz and Rainer Stiefelhagen"
code: "https://github.com/HensoldtOptronicsCV/MultispectralPedestrianDetection"
keywords:
  - word: "pedestrian detection"
  - word: "human recognition"
  - word: "multi-modal"
  - word: "thermal infrared"
  - word: "multispectral fusion"
  - word: "low object resolution"
  - word: "multispectral data augmentation"
  - word: "box-less object detection"
  - word: ""
paper: "papers/0534.pdf"
supp: "supp/0534_supp.pdf"
abstract: "Multispectral images consisting of aligned visual-optical (VIS) and thermal infrared (IR) image pairs are well-suited for practical applications like autonomous driving or visual surveillance. Such data can be used to increase the performance of pedestrian detection especially for weakly illuminated, small-scaled, or partially occluded instances. The current state-of-the-art is based on variants of Faster R-CNN and thus passes through two stages: a proposal generator network with handcrafted anchor boxes for object localization and a classification network for verifying the object category. In this paper we propose a method for effective and efficient multispectral fusion of the two modalities in an adapted single-stage anchor box free base architecture. We aim at learning pedestrian representations based on object center and scale rather than direct bounding box predictions. In this way, we can both simplify the network architecture and achieve higher detection performance, especially for pedestrians under occlusion or at low object resolution. In addition, we provide a study on well-suited multispectral data augmentation techniques that improve the commonly used augmentations. The results show our method's effectiveness in detecting small-scaled pedestrians. We achieve 5.68 % log-average miss rate in comparison to the best current state-of-the-art of 7.49 % (~25 % improvement) on the challenging KAIST Multispectral Pedestrian Benchmark."
slides-id: 38933993
channel-id: "paper_080_P2_id_0534"
---
