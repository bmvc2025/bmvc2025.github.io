---
layout: default_paper
id: 303
order: 141
poster_session: 3
session_id: 8
title: "BCaR: Beginner Classifier as Regularization Towards Generalizable Re-ID"
authors:
  - author: "Masato Tamura (Hitachi, Ltd.)"
  - author: "Tomoaki Yoshinaga (Hitachi, Ltd.)"
all_authors: "Masato Tamura and Tomoaki Yoshinaga"
code: "https://github.com/hitachi-rd-cv/bcar"
keywords:
  - word: "person re-identification"
  - word: "generalizable"
  - word: "soft label"
  - word: "knowledge distillation"
  - word: "Re-ID"
  - word: "domain generalization"
paper: "papers/0303.pdf"
supp: ""
abstract: "In recent years, the performance of person re-identification has been dramatically improved by virtue of sophisticated training methods. However, most of the existing methods are based on the assumption that the statistics of a target domain can be utilized during training. This inevitably introduces huge costs for data collection each time a person re-identification system is deployed, which hinders the applicability to real-world scenarios. To mitigate this issue, we expand upon the concept of domain generalization. Typical person re-identification datasets are composed of a large amount of identities. However, examples for each identity are rather scarce. It is widely known that if examples are highly biased, over-fitting is likely to occur and degrade the performance. To alleviate this problem, we propose a novel soft-label regularization method that combines an expert feature extractor with a beginner classifier for generating soft labels. From a representation learning perspective, a convolutional neural network-based feature extractor is thought to prioritize common patterns. Therefore, the subsequent classifier typically fits common examples first, followed by rare ones. On the basis of this observation, we force the beginner classifier to remain uncertain towards rare examples by means of periodic initialization. Accordingly, the beginner classifier assigns highly confident labels to common examples and ambiguous labels to rare ones, thus enabling soft labels to mitigate over-fitting to biased examples (e.g., highly occluded ones). Extensive analysis shows that our method successfully assigns ambiguous labels to biased examples and thus increases the rank-1 accuracy by 3.4%, 1.6%, 0.9%, and 5.2% on the VIPeR, PRID, GRID, and i-LIDS datasets, respectively. To facilitate future research, the source codes will be released."
slides-id: 38933944
channel-id: "paper_141_P3_id_0303"
---
