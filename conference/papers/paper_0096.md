---
layout: default_paper
id: 96
order: 99
oral_session: 5
poster_session: 3
session_id: 6
title: "EPI-based Oriented Relation Networks for Light Field Depth Estimation"
authors:
  - author: "Kunyuan Li (Hefei University of Technology)"
  - author: "Jun Zhang (Hefei University of Technology)"
  - author: "Rui Sun (Hefei University of Technology)"
  - author: "Xudong Zhang (Hefei University of Technology)"
  - author: "Jun Gao (Hefei University of Technology)"
all_authors: "Kunyuan Li, Jun Zhang, Rui Sun, Xudong Zhang and Jun Gao"
code: "https://github.com/lkyahpu/EPI_ORM.git"
keywords:
  - word: "depth estimation"
  - word: "light field"
  - word: "relation modeling"
  - word: "epipolar plane image"
  - word: "refocusing"
  - word: "Siamese network"
  - word: ""
paper: "papers/0096.pdf"
supp: ""
abstract: "Light field cameras record not only the spatial information of observed scenes but also the directions of all incoming light rays. The spatial and angular information implicitly contain geometrical characteristics such as multi-view or epipolar geometry, which can be exploited to improve the performance of depth estimation. An Epipolar Plane Image (EPI), the unique 2D spatial-angular slice of the light field, contains patterns of oriented lines. The slope of these lines is associated with the disparity. Benefiting from this property of EPIs, some representative methods estimate depth maps by analyzing the disparity of each line in EPIs. However, these methods often extract the optimal slope of the lines from EPIs while ignoring the relationship between neighboring pix- els, which leads to inaccurate depth map predictions. Based on the observation that an oriented line and its neighboring pixels in an EPI share a similar linear structure, we propose an end-to-end fully convolutional network (FCN) to estimate the depth value of the intersection point on the horizontal and vertical EPIs. Specifically, we present a new feature-extraction module, called Oriented Relation Module (ORM), that constructs the relationship between the line orientations. To facilitate training, we also propose a refocusing-based data augmentation method to obtain different slopes from EPIs of the same scene point. Extensive experiments verify the efficacy of learning relations and show that our approach is competitive to other state-of-the-art methods. The code and the trained models are available at https://github.com/lkyahpu/EPI_ORM.git."
slides-id: 38933885
channel-id: "paper_099_P3_id_0096"
---
