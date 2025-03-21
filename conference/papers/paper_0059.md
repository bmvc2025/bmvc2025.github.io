---
layout: default_paper
id: 59
order: 64
poster_session: 2
session_id: 5
title: "Improved Trainable Calibration Method for Neural Networks"
authors:
  - author: "Gongbo Liang (University of Kentucky)"
  - author: "Yu Zhang (University of Kentucky)"
  - author: "Xiaoqing Wang (University of Kentucky)"
  - author: "Nathan Jacobs (University of Kentucky)"
all_authors: "Gongbo Liang, Yu Zhang, Xiaoqing Wang and Nathan Jacobs"
code: ""
keywords:
  - word: "medical imaging"
  - word: "neural network calibration"
  - word: "trainable"
paper: "papers/0059.pdf"
supp: "supp/0059_supp.pdf"
abstract: "Recent works have shown that modern neural networks can achieve super-human performance in a wide range of image classification tasks. However, these works have primarily focused on classification accuracy, ignoring the important role of uncertainty quantification in medical decision-making. Empirically, neural networks are often miscalibrated and dramatically overconfident in their predictions. This miscalibration could be problematic in any automatic decision-making system, but we focus on the medical field in which neural network miscalibration has the potential to lead to significant treatment errors. We propose a novel approach to neural network calibration that maintains the overall classification accuracy while significantly improving model calibration. The proposed approach is based on ECE, which is a standard metric for quantifying model calibration error. As such, it is a natural and empirical way of assessing model calibration. Our approach can be easily integrated into any classification task as an auxiliary loss term, thus not requiring an explicit training round for calibration. We show that our approach reduces calibration error significantly across various architectures and datasets and that it performs better than temperature scaling, the current state-of-the-art approach."
slides-id: 38933877
channel-id: "paper_064_P2_id_0059"
---
