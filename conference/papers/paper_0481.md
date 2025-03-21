---
layout: default_paper
id: 481
order: 22
poster_session: 1
session_id: 2
title: "Learning 3D Global Human Motion Estimation from Unpaired, Disjoint Datasets"
authors:
  - author: "Julian Habekost (University of Edinburgh)"
  - author: "Takaaki Shiratori (Facebook Reality Labs)"
  - author: "Yuting Ye (Facebook Reality Labs)"
  - author: "Taku Komura (University of Edinburgh)"
all_authors: "Julian Habekost, Takaaki Shiratori, Yuting Ye and Taku Komura"
code: ""
keywords:
  - word: "3D human pose estimation"
  - word: "3D global motion estimation"
  - word: "unpaired training"
  - word: "2d to 3d pose regression"
  - word: "monocular motion capture"
  - word: "human time sequence modeling"
  - word: ""
paper: "papers/0481.pdf"
supp: "supp/0481_supp.mp4"
abstract: "We propose a novel method to compute both the local and global 3D motion of the human body from a 2D monocular video. Our approach only uses unpaired sets of 2D keypoints from target videos and 3D motion capture data for training. The estimation target video dataset is assumed to lack any ground truth and thus our supervision signal comes from motion datasets that are fully disjoint from the target datasets. For each time step, a temporal convolutional generator configures the human pose in the global space to satisfy both a reprojection loss and an adversarial loss. The translational and rotational global motion is then derived and converted into the egocentric representation in a differentiable manner for adversarial learning. We compare our system to state-of-the-art architectures that use the Human3.6M dataset for paired training, and demonstrate comparable precision even though our system is never trained on the ground truth Human3.6M 3D motion capture data. Due to its unpaired and disjoint nature in the training data, our system can be trained on a large set of videos and 3D motion capture data, which can considerably expand the domain of the applicable motion data types."
slides-id: 38933986
channel-id: "paper_022_P1_id_0481"
---
