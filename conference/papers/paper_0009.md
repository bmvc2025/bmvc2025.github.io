---
layout: default_paper
id: 9
order: 75
poster_session: 2
session_id: 5
title: "ViewSynth: Learning Local Features from Depth using View Synthesis"
authors:
  - author: "Jisan Mahmud (University of North Carolina at Chapel Hill)"
  - author: "Rajat Vikram Singh (Siemens Corporation)"
  - author: "Peri Akiva (Rutgers University)"
  - author: "Spondon Kundu (SIemens Corporate Technology)"
  - author: "Kuan-Chuan Peng (Mitsubishi Electric Research Laboratories)"
  - author: "Jan-Michael  Frahm (UNC-Chapel Hill)"
all_authors: "Jisan Mahmud, Rajat Vikram Singh, Peri Akiva, Spondon Kundu, Kuan-Chuan Peng and Jan-Michael  Frahm"
code: ""
keywords:
  - word: "viewpoint invariant representation learning"
  - word: "depth representation learning"
  - word: "view synthesis"
  - word: "correspondence learning"
paper: "papers/0009.pdf"
supp: "supp/0009_supp.zip"
abstract: "The rapid development of inexpensive commodity depth sensors has made keypoint detection and matching in the depth image modality an important problem in computer vision. Despite great improvements in recent RGB local feature learning methods, adapting them directly in the depth modality leads to unsatisfactory performance. Most of these methods do not explicitly reason beyond the visible pixels in the images. To address the limitations of these methods, we propose a framework ViewSynth, to jointly learn: (1) viewpoint invariant keypoint-descriptor from depth images using a proposed Contrastive Matching Loss, and (2) view synthesis of depth images from different viewpoints using the proposed View Synthesis Module and View Synthesis Loss. By learning view synthesis, we explicitly encourage the feature extractor to encode information about not only the visible, but also the occluded parts of the scene. We demonstrate that in the depth modality, ViewSynth outperforms the state-of-the-art depth and RGB local feature extraction techniques in the 3D keypoint matching and camera localization tasks on the RGB-D datasets 7-Scenes, TUM RGBD and CoRBS in most scenarios. We also show the generalizability of ViewSynth in 3D keypoint matching across different datasets."
slides-id: 38933863
channel-id: "paper_075_P2_id_0009"
---
