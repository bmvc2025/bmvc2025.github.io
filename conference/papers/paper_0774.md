---
layout: default_paper
id: 774
order: 127
poster_session: 3
session_id: 8
title: "Imitating Unknown Policies via Exploration"
authors:
  - author: "Nathan Gavenski (PUCRS)"
  - author: "Juarez Monteiro (PUCRS)"
  - author: "Roger Granada (PUCRS)"
  - author: "Felipe Meneguzzi (PUCRS)"
  - author: "Rodrigo Barros (PUCRS)"
all_authors: "Nathan Gavenski, Juarez Monteiro, Roger Granada, Felipe Meneguzzi and Rodrigo Barros"
code: "https://github.com/NathanGavenski/IUPE"
keywords:
  - word: "imitation learning"
  - word: "learning from demonstration"
  - word: "behavioral cloning"
paper: "papers/0774.pdf"
supp: "supp/0774_supp.zip"
abstract: "Behavioral cloning is an imitation learning technique that teaches an agent how to behave through expert demonstrations. Recent approaches use self-supervision of fully-observable unlabeled snapshots of the states to decode state-pairs into actions.
However, the iterative learning scheme from these techniques are prone to getting stuck into bad local minima. We address these limitations incorporating a two-phase model into the original framework, which learns from unlabeled observations via exploration, substantially improving traditional behavioral cloning by exploiting (i) a sampling mechanism to prevent bad local minima, (ii) a sampling mechanism to improve exploration, and (iii) self-attention modules to capture global features. The resulting technique outperforms the previous state-of-the-art in four different environments by a large margin. "
slides-id: 38934029
channel-id: "paper_127_P3_id_0774"
---
