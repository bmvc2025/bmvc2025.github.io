---
layout: default_paper
id: 525
order: 142
poster_session: 3
session_id: 8
title: "Cascaded channel pruning using hierarchical self-distillation"
authors:
  - author: "Roy Miles (Imperial College London)"
  - author: "Krystian Mikolajczyk (Imperial College London)"
all_authors: "Roy Miles and Krystian Mikolajczyk"
code: "https://github.com/roymiles/cascaded-channel-pruning"
keywords:
  - word: "pruning"
  - word: "knowledge distillation"
  - word: "image classification"
  - word: ""
paper: "papers/0525.pdf"
supp: "supp/0525_supp.zip"
abstract: "In this paper, we propose an approach for filter-level pruning with hierarchical knowledge distillation based on the teacher, teaching-assistant, and student framework.  Our method makes use of teaching assistants at intermediate pruning levels that share the same architecture and weights as the target student.  We propose to prune each model independently using the gradient information from its corresponding teacher. By considering the relative sizes of each student-teacher pair, this formulation provides a natural trade-off between the capacity gap for knowledge distillation and the bias of the filter saliency updates.  Our results show improvements in the attainable accuracy and model compression across the CIFAR10 and ImageNet classification tasks using the VGG16 and ResNet50 architectures.  We provide an extensive evaluation that demonstrates the benefits of using a varying number of teaching assistant models at different sizes."
slides-id: 38933989
channel-id: "paper_142_P3_id_0525"
---
