---
layout: default_paper
id: 448
order: 34
poster_session: 1
session_id: 2
title: "SD-MTCNN: Self-Distilled Multi-Task CNN"
authors:
  - author: "Ankit Jha (IIT Bombay)"
  - author: "Awanish Kumar (Indian Institute of Technology Bombay)"
  - author: "Biplab Banerjee (Indian Institute of Technology, Bombay)"
  - author: "Vinay Namboodiri (IIT Kanpur)"
all_authors: "Ankit Jha, Awanish Kumar, Biplab Banerjee and Vinay Namboodiri"
code: ""
keywords:
  - word: "self-distillation"
  - word: "multi-task learning"
paper: "papers/0448.pdf"
supp: "supp/0448_supp.pdf"
abstract: "Multi-task learning (MTL) using convolutional neural networks (CNN) deals with training the network for multiple correlated tasks in concert.
For accuracy-critical applications, there are endeavors to boost the model performance by resorting to a deeper network, which also increases the model complexity. However, such burdensome models are difficult to be deployed on mobile or edge devices.
To ensure a trade-off between performance and complexity of CNNs in the context of MTL, we introduce the novel paradigm of self-distillation within the network. Different from traditional knowledge distillation (KD), which trains the Student in accordance with a cumbersome Teacher, our self-distilled multi-task CNN model: SD-MTCNN aims at distilling knowledge from deeper CNN layers into the shallow layers. Precisely, we follow a hard-sharing based MTL setup where all the tasks share a generic feature-encoder on top of which separate task-specific decoders are enacted. Under this premise, SD-MTCNN distills the more abstract features from the decoders to the encoded feature space, which guarantees improved multi-task performance from different parts of the network.
We validate SD-MTCNN on three benchmark datasets: CityScapes, NYUv2, and Mini-Taskonomy, and results confirm the improved generalization capability of self-distilled multi-task CNNs in comparison to the literature and baselines."
slides-id: 38933977
channel-id: "paper_034_P1_id_0448"
---
