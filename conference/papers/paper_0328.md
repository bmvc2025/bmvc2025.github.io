---
layout: default_paper
id: 328
order: 61
poster_session: 2
session_id: 5
title: "Deep Metric Learning Meets Deep Clustering: An Novel Unsupervised Approach for Feature Embedding"
authors:
  - author: "Binh Nguyen (AIOZ)"
  - author: "Binh Nguyen (AIOZ)"
  - author: "Gustavo Carneiro (University of Adelaide)"
  - author: "Erman Tjiputra (AIOZ)"
  - author: "Quang Tran (AIOZ)"
  - author: "Thanh-Toan Do (The University of Liverpool)"
all_authors: "Binh Nguyen, Binh Nguyen, Gustavo Carneiro, Erman Tjiputra, Quang Tran and Thanh-Toan Do"
code: "https://github.com/aioz-ai/BMVC20_CBSwR"
keywords:
  - word: "unsupervised deep metric learning"
  - word: "unsupervised feature learning"
  - word: "unsupervised metric loss"
  - word: "negative mining"
  - word: "deep clustering"
  - word: "pseudo labels"
  - word: "reconstruction"
  - word: "centroid representations"
  - word: "retrieval"
  - word: "multi-task"
  - word: ""
paper: "papers/0328.pdf"
supp: ""
abstract: "Unsupervised Deep Distance Metric Learning (UDML) aims to learn sample similarities in the embedding space from an unlabeled dataset. Traditional UDML methods usually use the triplet loss or pairwise loss which requires the mining of positive and negative samples w.r.t. anchor data points. This is, however, challenging in an unsupervised setting as the label information is not available. In this paper, we propose a new UDML method that overcomes that challenge. In particular, we propose to use a deep clustering loss to learn centroids, i.e., pseudo labels, that represent semantic classes. During learning, these centroids are also used to reconstruct the input samples. It hence ensures the representativeness of centroids — each centroid represents visually similar samples. Therefore, the centroids give information about positive (visually similar) and negative (visually dissimilar) samples. Based on pseudo labels, we propose a novel unsupervised metric loss which enforces the positive concentration and negative separation of samples in the embedding space. Experimental results on benchmarking datasets show that the proposed approach outperforms other UDML methods."
slides-id: 38933948
channel-id: "paper_061_P2_id_0328"
---
