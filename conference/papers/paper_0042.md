---
layout: default_paper
id: 42
order: 69
poster_session: 2
session_id: 5
title: "Meta-RetinaNet for Few-shot Object Detection"
authors:
  - author: "Shaoqi Li (Beihang University)"
  - author: "Wenfeng Song (BeihangUniversity)"
  - author: "Shuai Li (BeihangUniversity)"
  - author: "Aimin Hao (BeihangUniversity)"
  - author: "Hong Qin (Stony Brook University)"
all_authors: "Shaoqi Li, Wenfeng Song, Shuai Li, Aimin Hao and Hong Qin"
code: ""
keywords:
  - word: "Few shot"
  - word: "object detection"
  - word: "meta-learning"
  - word: "Meta-RetinaNet"
  - word: "Balanced Loss"
  - word: "coefficient vector"
  - word: ""
paper: "papers/0042.pdf"
supp: ""
abstract: "Few shot object detection (FSD) is gaining popularity, enhanced by the deep learning methods in recent years. Meanwhile, meta-learning has achieved great success in few-shot image classification benefitting from its adaptive capability corresponding to a suite of tasks. Yet, most object detection models are based on deep neural networks (DNNs), and they are prone to the overfitting problem due to limited samples available during training. To adapt the learned prior knowledge more effectively to new tasks, this paper proposes a novel Meta-RetinaNet for FSD, which avoids a biased meta-learner and improves its generalization ability. It employs a Meta Coefficient Learner (MCL) trained by the Balanced Loss (BL) to augment the DNNs. Specifically, the MCL adapts to tasks by the product of pre-trained convolution weights and coefficient vectors densely for all the convolutional layers, such that it could adequately transfer the learned knowledge to new tasks (while overcoming the overfitting problem) by training fewer parameters. In addition, the BL expedites the training of a Meta-RetinaNet by balancing the performance of a host of tasks, and it also retains stable performance for new tasks. Our experiments showcase the effectiveness of our method, which achieves the state-of-the-art performance on the multiple settings of Pascal VOC and COCO datasets."
slides-id: 38933870
channel-id: "paper_069_P2_id_0042"
---
