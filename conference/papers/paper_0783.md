---
layout: default_paper
id: 783
order: 72
poster_session: 2
session_id: 5
title: "Not all points are created equal - an anisotropic cost function for facial landmark location"
authors:
  - author: "Farshid Rayhan (The University of Manchester)"
  - author: "Aphrodite Galata (The University of Manchester)"
  - author: "Timothy Cootes (University of Manchester)"
all_authors: "Farshid Rayhan, Aphrodite Galata and Timothy Cootes"
code: "https://github.com/farshidrayhan-uom/ananisotropic_loss"
keywords:
  - word: "face allignment"
  - word: "facial landmark detection"
  - word: "facial keypoint detection"
paper: "papers/0783.pdf"
supp: "supp/0783_supp.pdf"
abstract: "An effective approach to locating facial landmarks is to train a CNN to predict their positions directly from an image patch cropped around the face. Earlier work has shown that the choice of cost function comparing predicted with target points is important, but have tended to use the same weighting for each individual point. Since some points, such as those on boundaries, are less clearly defined than those at obvious corners, we propose an alternative cost function which uses anisotropic weights.  This penalises movement away from feature boundaries more than that along them. We demonstrate that using this cost function improves location performance and training convergence. We also address the problem of pose imbalance in datasets, suggesting a way of balancing the poses in the training samples. State of the art results on three public datasets (AFLW, WFLW and 300W) demonstrate the effectiveness of these techniques"
slides-id: 38934031
channel-id: "paper_072_P2_id_0783"
---
