---
layout: default_paper
id: 977
order: 159
poster_session: 4
session_id: 11
title: "Robust Unsupervised Cleaning of Underwater Bathymetric Point Cloud Data"
authors:
  - author: "Cong Chen (908945500)"
  - author: "Abel  Gawel (ETH Zurich)"
  - author: "Stephen Krauss (Virginia Tech)"
  - author: "Yuliang Zou (Virginia Tech)"
  - author: "Amos Abbott (Virginia Tech)"
  - author: "Daniel Stilwell (Virginia Tech.)"
all_authors: "Cong Chen, Abel  Gawel, Stephen Krauss, Yuliang Zou, Amos Abbott and Daniel Stilwell"
code: ""
keywords:
  - word: "Point cloud cleaning"
  - word: "underwater bathymetric data"
  - word: "point cloud tensorization"
  - word: "variational Bayesian inference"
  - word: ""
paper: "papers/0977.pdf"
supp: ""
abstract: "This paper presents a novel unified one-stage unsupervised learning framework forpoint cloud cleaning of noisy partial data from underwater side-scan sonars. By combining a swath-based point cloud tensor representation, an adaptive multi-scale feature encoder, and a generative Bayesian framework, the proposed method provides robust sonarpoint cloud denoising, completion, and outlier removal simultaneously. The condensed swath-based tensor representation preserves point cloud of underlying three-dimensionalgeometry of point cloud by reconstructing spatial and temporal correlation of sonar data.The adaptive multi-scale feature encoder distinguishes noisy  partial  tensor  data without handcrafted feature labeling by utilizing CANDECOMP/PARAFAC tensor factorization. Each local embedded outlier feature under various scales is aggregated into aglobal context by a generative Bayesian framework. The model is automatically inferredby a variational Bayesian, without parameter tuning and model pre-training. Extensive experiments on large scale synthetic and real data demonstrates the robustness against environmental perturbation. The proposed algorithm compares favourably with existing methods."
slides-id: 38934055
channel-id: "paper_159_P4_id_0977"
---
