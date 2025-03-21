---
layout: default_paper
id: 90
order: 132
poster_session: 3
session_id: 8
title: "Transferring Pretrained Networks to Small Data via Category Decorrelation"
authors:
  - author: "Ying Jin (Tsinghua University)"
  - author: "Zhangjie Cao (Tsinghua University)"
  - author: "Mingsheng Long (Tsinghua University)"
  - author: "Jianmin Wang (Tsinghua University, China)"
all_authors: "Ying Jin, Zhangjie Cao, Mingsheng Long and Jianmin Wang"
code: ""
keywords:
  - word: "Category Decorrelation"
  - word: "Under Transfer"
paper: "papers/0090.pdf"
supp: ""
abstract: "Transfer learning by fine-tuning neural networks pre-trained on large-scale datasets excels at accelerating the training process and improving the model performance for the target task. Previous works have unveiled catastrophic forgetting in fine-tuning, where the model is over-transferred thus losing pre-trained knowledge, especially facing large target datasets. However, when fine-tuning pre-trained networks to small data, under transfer emerges instead, where the model sticks to the pre-trained model and learns little target knowledge. Under transfer severely restricts the wide use of fine-tuning but is still under-investigated. In this paper, we conduct an in-depth study of under transfer problem in fine-tuning and observe that when we finetune model to small data, redundant category correlation becomes stronger in the model prediction, which is a potential cause of under transfer. Based on the observation, we propose a novel regularization approach, Category Decorrelation (CatDec), to minimize category correlation in the model, which introduces a new inductive bias to strengthen the model transfer. CatDec is orthogonal to existing fine-tuning approaches and can collaborate with them to address the dilemma of catastrophic forgetting and under transfer. Experiment results demonstrate that the proposed approach can consistently improve the fine-tuning performance of various mainstream methods. Further analyses prove that CatDec alleviates redundant category correlation and helps transfer."
slides-id: 38933884
channel-id: "paper_132_P3_id_0090"
---
