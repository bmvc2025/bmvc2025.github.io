---
layout: default_paper
id: 401
order: 128
poster_session: 3
session_id: 8
title: "RankPose: Learning Generalised Feature with Rank Supervision for Head Pose Estimation"
authors:
  - author: "donggen dai (None)"
  - author: "Wangkit Wong (PingAn Tech.)"
  - author: "Zhuojun Chen (Baidu Inc.)"
all_authors: "Donggen Dai, Wangkit Wong and Zhuojun Chen"
code: "https://github.com/seathiefwang/RankPose"
keywords:
  - word: "head pose estimation"
  - word: "rank supervision"
  - word: "arccos transformation"
  - word: "ranking loss"
paper: "papers/0401.pdf"
supp: ""
abstract: "We address the challenging problem of RGB image-based head pose estimation. We first reformulate head pose representation learning to constrain it to a bounded space. Head pose represented as vector projection or vector angles shows helpful to improving performance. Further, a ranking loss combined with MSE regression loss is proposed. The ranking loss supervises a neural network with paired samples of the same person and penalises incorrect ordering of pose prediction. Analysis on this new loss function suggests it contributes to a better local feature extractor, where features are generalised to Abstract Landmarks which are pose-related features instead of pose-irrelevant information such as identity, age, and lighting. Extensive experiments show that our method significantly outperforms the current state-of-the-art schemes on public datasets: AFLW2000 and BIWI. Our model achieves significant improvements over previous SOTA MAE on AFLW2000 and BIWI from 4.50 [11] to 3.66 and from 4.0 [24] to 3.71 respectively. Source code is available at: https://github.com/seathiefwang/RankHeadPose."
slides-id: 38933966
channel-id: "paper_128_P3_id_0401"
---
