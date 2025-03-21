---
layout: default_paper
id: 294
order: 146
poster_session: 3
session_id: 8
title: "3D-GMNet: Single-View 3D Shape Recovery as A Gaussian Mixture"
authors:
  - author: "Kohei Yamashita (Kyoto University)"
  - author: "Shohei Nobuhara (Kyoto University)"
  - author: "Ko Nishino (Kyoto University)"
all_authors: "Kohei Yamashita, Shohei Nobuhara and Ko Nishino"
code: ""
keywords:
  - word: "single image 3D reconstruction"
  - word: "3D shape representation"
  - word: "Gaussian mixture model"
paper: "papers/0294.pdf"
supp: "supp/0294_supp.zip"
abstract: "In this paper, we introduce 3D-GMNet, a deep neural network for single-image 3D shape recovery. As the name suggests, 3D-GMNet recovers 3D shape as a Gaussian mixture model. In contrast to voxels, point clouds, or meshes, a Gaussian mixture representation requires a much smaller footprint for representing 3D shapes and, at the same time, offers a number of additional advantages including instant pose estimation, automatic level-of-detail computation, and a distance measure. The proposed 3D-GMNet is trained end-to-end with single input images and corresponding 3D models by using two novel loss functions: a 3D Gaussian mixture loss and a multi-view 2D loss. The first maximizes the likelihood of the Gaussian mixture shape representation by considering the target point cloud as samples from the true distribution, and the latter improves the consistency between the input silhouette and the projection of the Gaussian mixture shape model. Extensive quantitative evaluations with synthesized and real images demonstrate the effectiveness of the proposed method."
slides-id: 38933943
channel-id: "paper_146_P3_id_0294"
---
