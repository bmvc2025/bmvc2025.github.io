---
layout: default_paper
id: 378
order: 167
poster_session: 4
session_id: 11
title: "Graph Density-Aware Losses for Novel Compositions in Scene Graph Generation"
authors:
  - author: "Boris Knyazev (University of Guelph)"
  - author: "Harm De Vries (Element AI)"
  - author: "Cătălina Cangea (University of Cambridge)"
  - author: "Graham Taylor (University of Guelph)"
  - author: "Aaron Courville (Universite de Montreal)"
  - author: "Eugene Belilovsky (Mila, University of Montreal)"
all_authors: "Boris Knyazev, Harm De Vries, Cătălina Cangea, Graham Taylor, Aaron Courville and Eugene Belilovsky"
code: "https://github.com/bknyaz/sgg"
keywords:
  - word: "scene graphs"
  - word: "scene graph generation"
  - word: "graph density"
  - word: "compositional generalization"
  - word: "visual genome"
  - word: "gqa"
  - word: "message passing"
paper: "papers/0378.pdf"
supp: "supp/0378_supp.pdf"
abstract: "Scene graph generation (SGG) aims to predict graph-structured descriptions of input images, in the form of objects and relationships between them. This task is becoming increasingly useful for progress at the interface of vision and language. Here, it is important—yet challenging—to perform well on novel (zero shot) or rare (few shot) compositions of objects and relationships. In this paper, we identify two key issues that limit such generalization. Firstly, we show that the standard loss used in this task is unintentionally a function of scene graph density. This leads to the neglect of individual edges in large sparse graphs during training, even though these contain diverse few shot examples that are important for generalization. Secondly, the frequency of relationships can create a strong bias in this task, such that a ``blind'' model predicting the most frequent relationship achieves good performance. Consequently, some state-of-the-art models exploit this bias to improve results. We show that such models can suffer the most in their ability to generalize to rare compositions, evaluating two different models on the Visual Genome dataset and its more recent, improved version, GQA. To address these issues, we introduce a density-normalized edge loss, which provides more than a two-fold improvement in certain generalization metrics. Compared to other works in this direction, our enhancements require only a few lines of code and no added computational cost. We also highlight the difficulty of accurately evaluating models using existing metrics, especially on zero/few shots, and introduce a novel weighted metric."
slides-id: 38933960
channel-id: "paper_167_P4_id_0378"
---
