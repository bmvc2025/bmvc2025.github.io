---
layout: default_paper
id: 130
order: 153
oral_session: 8
poster_session: 4
session_id: 10
title: "Procedure Completion by Learning from Partial Summaries"
authors:
  - author: "Ehsan Elhamifar (Northeastern University)"
  - author: "Zwe Naing (Northeastern University)"
all_authors: "Ehsan Elhamifar and Zwe Naing"
code: ""
keywords:
  - word: "procedure learning"
  - word: "instructional videos"
  - word: "summarization"
  - word: "subset selection"
  - word: "representation learning"
  - word: "partial summaries"
paper: "papers/0130.pdf"
supp: ""
abstract: "We address the problem of procedure completion in videos, which is to find and localize all key-steps of a task given only a small observed subset of key-steps. We cast the problem as learning summarization from partial summaries that allows to incorporate prior knowledge and learn from incomplete key-steps. Given multiple pairs of (video, subset of key-steps), we address the problem by learning representations of input data and finding the remaining key-steps that generalizes well to key-step discovery in new videos. We propose a loss function on the parameters of a network that promotes to recover unseen key-steps that together with the observed key-steps optimize a desired subset selection criterion. To tackle the highly non-convex learning problem, involving both discrete and continuous variables, we develop an efficient learning algorithm that alternates between representation learning and recovering unseen key-steps while incorporating prior knowledge, via a greedy algorithm. By extensive experiments on two instructional video datasets, we show the effectiveness of our framework."
slides-id: 38933898
channel-id: "paper_153_P4_id_0130"
---
