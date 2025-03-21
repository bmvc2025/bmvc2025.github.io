---
layout: default_paper
id: 861
order: 193
poster_session: 4
session_id: 11
title: "Self-Supervised Learning for Facial Action Unit Recognition through Temporal Consistency"
authors:
  - author: "Liupei Lu (University of Southern California)"
  - author: "Leili Tavabi (University of Southern California)"
  - author: "Mohammad Soleymani (University of Southern California)"
all_authors: "Liupei Lu, Leili Tavabi and Mohammad Soleymani"
code: " https://git.io/JJSI6"
keywords:
  - word: "self-supervised learning"
  - word: "facial action unit detection"
  - word: "temporal consistency"
  - word: "metric learning"
  - word: "representation learning"
  - word: "facial expression analysis"
paper: "papers/0861.pdf"
supp: "supp/0861_supp.pdf"
abstract: "Facial expressions have inherent temporal dependencies that can be leveraged in automatic facial expression analysis from videos. In this paper, we propose a self-supervised representation learning method for facial Action Unit (AU) recognition through learning temporal consistencies in videos. To this end, we use a triplet-based ranking approach that learns to rank the frames based on their temporal distance from an anchor frame. Instead of manually labeling informative triplets, we randomly select an anchor frame along with two additional frames with predefined distances from the anchor as positive and negative. To develop an effective metric learning approach, we introduce an aggregate ranking loss by taking the sum of multiple triplet losses to allow pairwise comparisons between adjacent frames. A Convolutional Neural Network (CNN) is used as encoder to learn representations by minimizing the objective loss. We demonstrate that our encoder learns meaningful representations for AU recognition with no labels. The encoder is evaluated for AU detection on various detasets including BP4D, EmotioNet and DISFA. Our results are comparable or superior to the state-of-the-art AU recognition through self-supervised learning. "
slides-id: 38934041
channel-id: "paper_193_P4_id_0861"
---
