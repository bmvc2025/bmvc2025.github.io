---
layout: default_paper
id: 906
order: 18
poster_session: 1
session_id: 2
title: "Intrinsic Decomposition of Document Images In-the-Wild"
authors:
  - author: "Sagnik Das (Stony Brook University)"
  - author: "Hassan Sial (Computer Vision Center)"
  - author: "Ke Ma (Stony Brook University)"
  - author: "Ramón Baldrich (Computer Vision Center (Ph.D.))"
  - author: "Maria Vanrell (Computer Vision Center (Ph.D.))"
  - author: "Dimitris   Samaras (Stony Brook University)"
all_authors: "Sagnik Das, Hassan Sial, Ke Ma, Ramón Baldrich, Maria Vanrell and Dimitris   Samaras"
code: "https://github.com/cvlab-stonybrook/DocIIW"
keywords:
  - word: "Intrinsic"
  - word: "Shading Removal"
  - word: "Shadows"
  - word: "Documents"
  - word: "OCR"
paper: "papers/0906.pdf"
supp: ""
abstract: "Automatic document content processing is affected by artifacts caused by the shape of the paper, non-uniform and diverse color of lighting conditions. Fully-supervised methods on real data are impossible due to the large amount of data needed. Hence, the current state of the art deep learning models are trained on fully or partially synthetic images. However, document shadow or shading removal results still suffer because: (a) prior methods rely on uniformity of local color statistics, which limit their application on real-scenarios with complex document shapes and textures and; (b) synthetic or hybrid datasets with non-realistic, simulated lighting conditions are used to train the models.  In this paper we tackle these problems with our two main contributions. First, a physically constrained learning-based method that directly estimates document reflectance based on intrinsic image formation which generalizes to challenging illumination conditions. Second, a new dataset that clearly  improves previous synthetic ones, by adding a large range of realistic shading and diverse multi-illuminant conditions, uniquely customized to deal with documents in-the-wild.
The proposed architecture works in two steps. First, a white balancing module neutralizes the color of the illumination on the input image. Based on the proposed multi-illuminant dataset we achieve a good white-balancing in really difficult conditions. Second, the shading separation module accurately disentangles the shading and paper material in a self-supervised manner where only the synthetic texture is used as a weak training signal (obviating the need for very costly ground truth with disentangled  versions of shading and reflectance). The proposed approach leads to significant generalization of document reflectance estimation in real scenes with challenging illumination. We extensively evaluate on the real benchmark datasets available for intrinsic image decomposition and document shadow removal tasks. Our reflectance estimation scheme, when used as a pre-processing step of an OCR pipeline, shows a 21 % improvement of character error rate (CER), thus, proving the practical applicability."
slides-id: 38934049
channel-id: "paper_018_P1_id_0906"
---
