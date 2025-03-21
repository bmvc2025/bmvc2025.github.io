---
layout: default_paper
id: 680
order: 30
poster_session: 1
session_id: 2
title: "Semi-supervised semantic segmentation needs strong, varied perturbations"
authors:
  - author: "Geoffrey French (University of East Anglia)"
  - author: "Samuli Laine (NVIDIA)"
  - author: "Timo Aila (NVIDIA)"
  - author: "Michal Mackiewicz (University of East Anglia)"
  - author: "Graham Finlayson (University of East Anglia)"
all_authors: "Geoffrey French, Samuli Laine, Timo Aila, Michal Mackiewicz and Graham Finlayson"
code: "https://github.com/Britefury/cutmix-semisup-seg"
keywords:
  - word: "semantic segmentation"
  - word: "semi-supervised"
  - word: "deep learning"
  - word: "consistency regularization"
  - word: "data augmentation"
  - word: "deep learning"
  - word: "cluster assumption"
paper: "papers/0680.pdf"
supp: "supp/0680_supp.pdf"
abstract: "Consistency regularization describes a class of approaches that have yielded ground breaking results in semi-supervised classification problems. Prior work has established the cluster assumption - under which the data distribution consists of uniform class clusters of samples separated by low density regions - as important to its success. We analyze the problem of semantic segmentation and find that its' distribution does not exhibit low density regions separating classes and offer this as an explanation for why semi-supervised segmentation is a challenging problem, with only a few reports of success.
We then identify choice of augmentation as key to obtaining reliable performance without such low-density regions.
We find that adapted variants of the recently proposed CutOut and CutMix augmentation techniques
yield state-of-the-art semi-supervised semantic segmentation results in standard datasets.
Furthermore, given its challenging nature we propose that semantic segmentation acts as an effective acid test for evaluating semi-supervised regularizers.
Implementation at: https://github.com/Britefury/cutmix-semisup-seg."
slides-id: 38934016
channel-id: "paper_030_P1_id_0680"
---
