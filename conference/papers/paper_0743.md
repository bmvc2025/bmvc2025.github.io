---
layout: default_paper
id: 743
order: 41
poster_session: 1
session_id: 2
title: "Initial Classifier Weights Replay for Memoryless Class Incremental Learning"
authors:
  - author: "Eden Belouadah (CEA LIST)"
  - author: "Adrian Popescu (CEA LIST)"
  - author: "Ioannis Kanellos (IMT Atlantique)"
all_authors: "Eden Belouadah, Adrian Popescu and Ioannis Kanellos"
code: "https://github.com/EdenBelouadah/class-incremental-learning/blob/master/siw/"
keywords:
  - word: "Memoryless Incremental Learning"
  - word: "Catastrophic Forgetting"
  - word: "Deep Learning"
  - word: "Image classification"
paper: "papers/0743.pdf"
supp: "supp/0743_supp.pdf"
abstract: "Incremental Learning (IL) is useful when artificial systems need to deal with streams of data and do not have access to all data at all times.
The most challenging setting requires a constant complexity of the deep model and an incremental model update without access to a bounded memory of past data.
Then, the representations of past classes are strongly affected by catastrophic forgetting.
To mitigate its negative effect, an adapted fine tuning which includes knowledge distillation is usually deployed.
We propose a different approach based on a vanilla fine tuning backbone.
It leverages initial classifier weights which provide a strong representation of past classes because they are trained with all class data.
However, the magnitude of classifiers learned in different states varies and normalization is needed for a fair handling of all classes.
Normalization is performed by standardizing the initial classifier weights, which are assumed to be normally distributed.
In addition, a calibration of prediction scores is done by using state level statistics to further improve classification fairness.
We conduct a thorough evaluation with four public datasets in a memoryless incremental learning setting. 
Results show that our method outperforms existing techniques by a large margin for large-scale datasets."
slides-id: 38934025
channel-id: "paper_041_P1_id_0743"
---
