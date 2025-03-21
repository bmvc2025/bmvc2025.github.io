---
layout: default_paper
id: 287
order: 131
poster_session: 3
session_id: 8
title: "6DoF Object Pose Estimation via Differentiable Proxy Voting Regularizer"
authors:
  - author: "Xin Yu (University of Technology Sydney)"
  - author: "Zheyu Zhuang (Australian National University)"
  - author: "Piotr Koniusz (Data61/CSIRO, ANU)"
  - author: "HONGDONG LI (Australian National University, Australia)"
all_authors: "Xin Yu, Zheyu Zhuang, Piotr Koniusz and HONGDONG LI"
code: ""
keywords:
  - word: "Object pose estimation"
  - word: "6DOF pose estimation"
  - word: "differentiable voting"
  - word: ""
paper: "papers/0287.pdf"
supp: "supp/0287_supp.pdf"
abstract: "Estimating a 6DOF object pose from a single image is very challenging due to occlusions or textureless appearances. Vector-field based keypoint voting has demonstrated its effectiveness and superiority on tackling those issues. 
However, direct regression of vector-fields neglects that the distances between pixels and keypoints also affect the deviations of hypotheses dramatically. In other words, small errors in direction vectors may generate severely deviated hypotheses when pixels are far away from a keypoint. In this paper, we aim to reduce such errors by incorporating the distances between pixels and keypoints into our objective. To this end, we develop a simple yet effective differentiable proxy voting Regularizer (DPVR) which mimics the hypothesis selection in the voting procedure.
By exploiting our voting regularizer, we are able to train our network in an end-to-end manner. Experiments on widely used datasets, ie, LINEMOD and Occlusion LINEMOD, manifest that our DPVR improves pose estimation performance significantly and speeds up the training convergence. "
slides-id: 38933942
channel-id: "paper_131_P3_id_0287"
---
