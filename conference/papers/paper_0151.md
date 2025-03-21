---
layout: default_paper
id: 151
order: 112
poster_session: 3
session_id: 8
title: "Explicit Residual Descent for 3D Human Pose Estimation from 2D Joint Locations"
authors:
  - author: "Yangyuxuan Kang (Institute of Software Chinese Academy of Sciences)"
  - author: "Anbang Yao (Intel Labs China)"
  - author: "Shandong Wang (Intel Labs China)"
  - author: "Ming Lu (Intel Labs China)"
  - author: "Yurong Chen (Intel Labs China)"
  - author: "Enhua Wu (CAS)"
all_authors: "Yangyuxuan Kang, Anbang Yao, Shandong Wang, Ming Lu, Yurong Chen and Enhua Wu"
code: "Code will be made publicly available later."
keywords:
  - word: "3D human pose estimation"
  - word: "pose lifting network"
  - word: "feedback optimization"
  - word: "deep neural network"
  - word: "supervised learning"
paper: "papers/0151.pdf"
supp: ""
abstract: "Recent studies show that the end-to-end learning paradigm based on well-designed lifting networks merely using 2D joint locations as the input can achieve impressive performance in handling 3D human pose estimation problem. However, in the viewpoint of optimization design, existing methods of this category have two drawbacks: (1) The inherent feature relation between the 2D pose input and the corresponding 3D pose estimate is not sufficiently explored. (2) The regression procedure is usually performed in a one-step manner. To address these two issues, this paper proposes an efficient yet accurate method called Explicit Residual Descent (ERD). Given an arbitrary lifting network which takes 2D joint locations in a single image as the input and generates an initial 3D pose estimate, our ERD learns a sequence of descent directions encoded with a shared lightweight differentiable structure, progressively refining the previous 3D pose estimate via adding in a 3D increment obtained from projecting the reconstructed 2D pose features onto each learnt descent direction. Extensive experiments on public benchmarks including Human3.6M dataset validate the superior performance of the proposed method against state-of-the-art methods. Code will be made publicly available."
slides-id: 38933903
channel-id: "paper_112_P3_id_0151"
---
