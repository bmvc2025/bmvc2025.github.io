---
layout: default_paper
id: 803
order: 191
poster_session: 4
session_id: 11
title: "Robust Image Matching By Dynamic Feature Selection"
authors:
  - author: "Hao Huang (New York University)"
  - author: "Jianchun Chen (New York University)"
  - author: "Xiang Li (New York University)"
  - author: "Lingjing Wang (New York University)"
  - author: "Yi Fang (New York University)"
all_authors: "Hao Huang, Jianchun Chen, Xiang Li, Lingjing Wang and Yi Fang"
code: ""
keywords:
  - word: "image matching"
  - word: "feature selection"
  - word: "reinforcement learning"
paper: "papers/0803.pdf"
supp: ""
abstract: "Estimating dense correspondences between images is a long-standing image understanding task. Most recent works introduce convolutional neural networks to extract high-level feature maps and find correspondences through feature matching. However, high-level feature maps are in low spatial resolution and therefore insufficient to provide accurate and fine-grained features to distinguish intra-class variations for correspondence matching.  To address this problem, we generate robust features by selecting and combining convolutional features at different levels/scales.  To resolve two critical issues in feature selection, i.e., how many and which levels of features to be selected, we frame the feature selection process as a sequential Markov decision-making process (MDP)and introduce an optimal selection strategy using reinforcement learning (RL) to select features.  Particularly, we define an RL environment for image matching in which individual actions are either requests for new features or terminate the selection episode by referring a matching score.  Deep neural networks are incorporated into our method and trained for decision making.  Experimental results show that our method achieves com-parable/superior performance with state-of-the-art methods on three public benchmarks, demonstrating the effectiveness of our proposed feature selection strategy."
slides-id: 38934035
channel-id: "paper_191_P4_id_0803"
---
