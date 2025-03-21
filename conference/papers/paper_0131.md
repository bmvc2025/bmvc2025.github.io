---
layout: default_paper
id: 131
order: 129
poster_session: 3
session_id: 8
title: "M2KD: Incremental Learning via Multi-model and Multi-level Knowledge Distillation"
authors:
  - author: "Peng Zhou (University of Maryland)"
  - author: "Long Mai (Adobe Research)"
  - author: "Jianming Zhang (Adobe Research)"
  - author: "Ning Xu (Adobe Research)"
  - author: "Zuxuan Wu (UMD)"
  - author: "Larry Davis (University of Maryland)"
all_authors: "Peng Zhou, Long Mai, Jianming Zhang, Ning Xu, Zuxuan Wu and Larry Davis"
code: ""
keywords:
  - word: "Incremental learning"
  - word: "Knowledge distillation"
  - word: "Pruning"
paper: "papers/0131.pdf"
supp: "supp/0131_supp.pdf"
abstract: "Incremental learning targets at achieving good performance on new categories without forgetting old ones. Knowledge distillation has been shown critical in preserving the performance on old classes. Conventional methods, however, sequentially distill knowledge only from the last model, leading to performance degradation on the old classes in later incremental learning steps. In this paper, we propose a multi-model and multi-level knowledge distillation strategy. Instead of sequentially distilling knowledge only from the last model, we directly leverage all previous model snapshots. In addition, we incorporate an auxiliary distillation to further preserve knowledge encoded at the intermediate feature levels. To make the model more memory efficient, we adapt mask based pruning to reconstruct all previous models with a small memory footprint. Experiments on standard incremental learning benchmarks show that our method improves the overall performance over standard distillation techniques."
slides-id: 38933899
channel-id: "paper_129_P3_id_0131"
---
