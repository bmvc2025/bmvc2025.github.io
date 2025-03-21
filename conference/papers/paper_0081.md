---
layout: default_paper
id: 81
order: 169
poster_session: 4
session_id: 11
title: "Synthetic Training for Accurate 3D Human Pose and Shape Estimation in the Wild"
authors:
  - author: "Akash Sengupta (University of Cambridge)"
  - author: "Roberto Cipolla (University of Cambridge)"
  - author: "Ignas Budvytis (Department of Engineering, University of Cambridge)"
all_authors: "Akash Sengupta, Roberto Cipolla and Ignas Budvytis"
code: "https://github.com/akashsengupta1997/STRAPS-3DHumanShapePose"
keywords:
  - word: "3D human shape estimation"
  - word: "3D pose estimation"
  - word: "3D reconstruction"
  - word: "smpl"
  - word: "synthetic data"
  - word: "pose and shape optimisation"
  - word: "3D human dataset"
paper: "papers/0081.pdf"
supp: "supp/0081_supp.pdf"
abstract: "This paper addresses the problem of monocular 3D human shape and pose estimation from an RGB image. Despite great progress in this field in terms of pose prediction accuracy, state-of-the-art methods often predict inaccurate body shapes. We suggest that this is primarily due to the scarcity of in-the-wild training data with diverse and accurate body shape labels. Thus, we propose STRAPS (Synthetic Training for Real Accurate Pose and Shape), a system that utilises proxy representations (such as silhouettes and 2D joints) as inputs to a shape and pose regression neural network, which is trained with synthetic training data (generated using the SMPL statistical body model) to overcome data scarcity. We bridge the gap between synthetic training inputs and noisy real inputs, which are predicted by keypoint detection and segmentation CNNs at test-time, by using data augmentation and corruption during training. In order to evaluate our approach, we curate and provide a challenging evaluation dataset for monocular human shape estimation, Sports Shape and Pose 3D (SSP-3D). It consists of RGB images of tightly-clothed sports-persons with a variety of body shapes and corresponding pseudo-ground-truth SMPL shape and pose parameters, obtained via multi-frame optimisation. We show that STRAPS outperforms other state-of-the-art methods on SSP-3D in terms of shape prediction accuracy, while remaining competitive with the state-of-the-art on pose-centric datasets and metrics."
slides-id: 38933881
channel-id: "paper_169_P4_id_0081"
---
