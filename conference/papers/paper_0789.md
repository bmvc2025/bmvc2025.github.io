---
layout: default_paper
id: 789
order: 25
poster_session: 1
session_id: 2
title: "LiPo-LCD: Combining Lines and Points for Appearance-based Loop Closure Detection"
authors:
  - author: "Joan Pep Company-Corcoles (University of the Balearic Islands)"
  - author: "Emilio Garcia-Fidalgo (University of the Balearic Islands)"
  - author: "Alberto Ortiz (University of the Balearic Islands, Spain)"
all_authors: "Joan Pep Company-Corcoles, Emilio Garcia-Fidalgo and Alberto Ortiz"
code: ""
keywords:
  - word: "loop closure"
  - word: "SLAM"
  - word: "incremental bag of words"
  - word: "visual place recognition"
  - word: "BoW"
  - word: "robot vision"
  - word: "localisation"
  - word: "mapping"
  - word: ""
paper: "papers/0789.pdf"
supp: ""
abstract: "Visual SLAM approaches typically depend on loop closure detection to correct the inconsistencies that may arise during the map and camera trajectory calculations, typically making use of point features for detecting and closing the existing loops. In low-textured scenarios, however, it is difficult to find enough point features and, hence, the performance of these solutions drops drastically. An alternative for human-made scenarios, due to their structural regularity, is the use of geometrical cues such as straight segments, frequently present within these environments. Under this context, in this paper we introduce LiPo-LCD, a novel appearance-based loop closure detection method that integrates lines and points. Adopting the idea of incremental Bag-of-Binary-Words schemes, we build separate BoW models for each feature, and use them to retrieve previously seen images using a late fusion strategy. Additionally, a simple but effective mechanism, based on the concept of island, groups similar images close in time to reduce the image candidate search effort. A final step validates geometrically the loop candidates by incorporating the detected lines by means of a process comprising a line feature matching stage, followed by a robust spatial verification stage, now combining both lines and points. As it is reported in the paper, LiPo-LCD compares well with several state-of-the-art solutions for a number of datasets involving different environmental conditions."
slides-id: 38934032
channel-id: "paper_025_P1_id_0789"
---
