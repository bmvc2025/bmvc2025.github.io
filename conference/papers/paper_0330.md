---
layout: default_paper
id: 330
order: 9
poster_session: 1
session_id: 2
title: "Weakly Supervised Generative Network for Multiple 3D Human Pose Hypotheses"
authors:
  - author: "Chen Li  (National University of Singapore)"
  - author: "Gim Hee Lee (National University of Singapore)"
all_authors: "Chen Li and Gim Hee Lee"
code: "https://github.com/chaneyddtt/weakly-supervised-3d-pose-generator"
keywords:
  - word: "3d human pose"
  - word: "multiple hypotheses"
  - word: "weak supervision"
  - word: "generative model"
  - word: ""
paper: "papers/0330.pdf"
supp: ""
abstract: "3D human pose estimation from a single image is an inverse problem 
due to the inherent ambiguity of the missing depth. 
Some previous works addressed the inverse problem by generating multiple hypotheses. However, these works are strongly supervised and require ground truth 2D-to-3D correspondences which can be difficult to obtain. In this paper, we propose a weakly supervised deep generative network to address the inverse problem and circumvent the need for ground truth 2D-to-3D correspondences. To this end, we design our network to model a proposal distribution which we use to approximate the unknown multi-modal target posterior distribution. We achieve the approximation by minimizing the KL divergence between the proposal and target distributions, and this leads to a 2D reprojection error and a prior loss term that can be weakly supervised. Furthermore, we determine the most probable solution as the conditional mode of the samples using the mean-shift algorithm.
We evaluate our method on three benchmark datasets -- Human3.6M, MPII and MPI-INF-3DHP. Experimental results show that 
our approach is capable of generating multiple feasible hypotheses and achieves state-of-the-art results compared to existing weakly supervised approaches."
slides-id: 38933949
channel-id: "paper_009_P1_id_0330"
---
