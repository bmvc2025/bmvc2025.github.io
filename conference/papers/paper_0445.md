---
layout: default_paper
id: 445
order: 21
poster_session: 1
session_id: 2
title: "Physics-informed detection and segmentation of type II solar radio bursts"
authors:
  - author: "Joseph Jenkins (Swansea University)"
  - author: "Adeline Paiement (Université de Toulon)"
  - author: "Jean Aboudarham (Swansea University)"
  - author: "Xavier Bonnin (Swansea University)"
all_authors: "Joseph Jenkins, Adeline Paiement, Jean Aboudarham and Xavier Bonnin"
code: ""
keywords:
  - word: "physics-informed machine learning"
  - word: "domain knowledge"
  - word: "detection"
  - word: "segmentation"
  - word: "applied computer vision"
  - word: "solar spectrogram"
  - word: "astrophysics data"
paper: "papers/0445.pdf"
supp: "supp/0445_supp.pdf"
abstract: "Type II solar radio bursts have proven to be a useful tool for gaining insights into the behaviour of complex solar events and for forecasting and mitigating their damages on Earth. In this work, we detect and segment the occurrence of type II bursts in solar radio spectrograms, thereby facilitating the extraction of parameters needed to gain insight into solar events. We utilise prior knowledge of how type II bursts drift through frequencies over time to assist with these tasks of detection and segmentation. A new adaptive Region of Interest (ROI) is proposed, to constrain the search to regions that follow the burst curvature at a given frequency. It comes with an implicit data normalisation that reduces the variance of burst appearance in the data, hence simplifying the learning process from small datasets. We demonstrate the effectiveness of our methodology using a simple and popular HOG and logistic regression detector and basic segmentation based on voting and background subtraction. On a custom dataset representative of different levels of solar activity, at a wavelength range where no other detection algorithm currently operates, our adaptive ROI significantly improves over traditional sliding windows. In future work, it may be applied to other, state-of-the-art, machine learning algorithms."
slides-id: 38933976
channel-id: "paper_021_P1_id_0445"
---
