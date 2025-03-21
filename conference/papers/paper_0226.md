---
layout: default_paper
id: 226
order: 111
poster_session: 3
session_id: 8
title: "ALBA: Reinforcement Learning for Video Object Segmentation"
authors:
  - author: "Shreyank Gowda (University of Edinburgh)"
  - author: "Panagiotis Eustratiadis (The University of Edinburgh)"
  - author: "Timothy Hospedales (Edinburgh University)"
  - author: "Laura Sevilla-Lara (Facebook)"
all_authors: "Shreyank Gowda, Panagiotis Eustratiadis, Timothy Hospedales and Laura Sevilla-Lara"
code: ""
keywords:
  - word: "video object segmentation"
  - word: "tracking"
  - word: ""
paper: "papers/0226.pdf"
supp: ""
abstract: "We consider the challenging problem of zero-shot video object segmentation (VOS). That is, segmenting and tracking multiple moving objects within a video fully automatically, without any manual initialization. We treat this as a grouping problem by exploiting object proposals and making a joint inference about grouping over both space and time. We propose a network architecture for tractably performing proposal selection and joint grouping. Crucially, we then show how to train this network with reinforcement learning so that it learns to perform the optimal non-myopic sequence of grouping decisions to segment the whole video. Unlike standard supervised techniques, this also enables us to directly optimize for the non-differentiable overlap-based metrics used to evaluate VOS. We show state-of-the-art results on DAVIS-2017 and Youtube-VOS benchmarks."
slides-id: 38933925
channel-id: "paper_111_P3_id_0226"
---
