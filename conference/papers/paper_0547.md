---
layout: default_paper
id: 547
order: 54
oral_session: 3
poster_session: 2
session_id: 3
title: "Delving Deeper into Anti-aliasing in ConvNets"
authors:
  - author: "Xueyan Zou (university of california, davis)"
  - author: "Fanyi Xiao (University of California Davis)"
  - author: "Zhiding Yu (NVIDIA)"
  - author: "Yong Jae Lee (University of California, Davis)"
all_authors: "Xueyan Zou, Fanyi Xiao, Zhiding Yu and Yong Jae Lee"
code: "https://maureenzou.github.io/ddac/"
keywords:
  - word: "anti-aliasing"
  - word: "image classification"
  - word: "semantic segmentation"
  - word: "instance segmentation"
  - word: "consistency"
  - word: "shift consistency"
paper: "papers/0547.pdf"
supp: ""
abstract: "Aliasing refers to the phenomenon that high frequency signals degenerate into completely different ones after sampling. It arises as a problem in the context of deep learning as downsampling layers are widely adopted in deep architectures to reduce parameters and computation. The standard solution is to apply a low-pass filter (e.g., Gaussian blur) before downsampling [Zhang.]. However, it can be suboptimal to apply the same filter across the entire content, as the frequency of feature maps can vary across both spatial locations and feature channels. To tackle this, we propose an adaptive content-aware low-pass filtering layer, which predicts separate filter weights for each spatial location and channel group of the input feature maps. We investigate the effectiveness and generalization of the proposed method across multiple tasks including ImageNet classification, COCO instance segmentation, and Cityscapes semantic segmentation. Qualitative and quantitative results demonstrate that our approach effectively adapts to the different feature frequencies to avoid aliasing while preserving useful information for recognition. "
slides-id: 38933996
channel-id: "paper_054_P2_id_0547"
---
