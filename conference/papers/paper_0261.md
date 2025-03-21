---
layout: default_paper
id: 261
order: 27
poster_session: 1
session_id: 2
title: "Bias-Awareness for Zero-Shot Learning the Seen and Unseen"
authors:
  - author: "William Thong (University of Amsterdam)"
  - author: "Cees Snoek (University of Amsterdam)"
all_authors: "William Thong and Cees Snoek"
code: "https://github.com/twuilliam/bias-gzsl"
keywords:
  - word: "generalized zero-shot learning"
  - word: "classifier bias"
  - word: "temperature calibration"
  - word: "entropy regularization"
  - word: ""
paper: "papers/0261.pdf"
supp: ""
abstract: "Generalized zero-shot learning recognizes inputs from both seen and unseen classes. Yet, existing methods tend to be biased towards the classes seen during training. In this paper, we strive to mitigate this bias. We propose a bias-aware learner to map inputs to a semantic embedding space for generalized zero-shot learning. During training, the model learns to regress to real-valued class prototypes in the embedding space with temperature scaling, while a margin-based bidirectional entropy term regularizes seen and unseen probabilities. Relying on a real-valued semantic embedding space provides a versatile approach, as the model can operate on different types of semantic information for both seen and unseen classes. Experiments are carried out on four benchmarks for generalized zero-shot learning and demonstrate the benefits of the proposed bias-aware classifier, both as a stand-alone method or in combination with generated features."
slides-id: 38933934
channel-id: "paper_027_P1_id_0261"
---
