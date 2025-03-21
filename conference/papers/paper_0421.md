---
layout: default_paper
id: 421
order: 57
oral_session: 4
poster_session: 2
session_id: 4
title: "Visibility-aware Multi-view Stereo Network"
authors:
  - author: "Jingyang Zhang (The Hong Kong University of Science and Technology)"
  - author: "Yao Yao (The Hong Kong University of Science and Technology)"
  - author: "Shiwei Li (Altizure)"
  - author: "Zixin Luo (HKUST)"
  - author: "Tian Fang (Altizure)"
all_authors: "Jingyang Zhang, Yao Yao, Shiwei Li, Zixin Luo and Tian Fang"
code: "https://github.com/jzhangbs/Vis-MVSNet"
keywords:
  - word: "multiview stereo"
  - word: "3d reconstruction"
paper: "papers/0421.pdf"
supp: "supp/0421_supp.pdf"
abstract: "Learning-based multi-view stereo (MVS) methods have demonstrated promising results. However, very few existing networks explicitly take the pixel-wise visibility into consideration, resulting in erroneous cost aggregation from occluded pixels. In this paper, we explicitly infer and integrate the pixel-wise occlusion information in the MVS network via the matching uncertainty estimation. The pair-wise uncertainty map is jointly inferred with the pair-wise depth map, which is further used as weighting guidance during the multi-view cost volume fusion. As such, the adverse influence of occluded pixels is suppressed in the cost fusion. The proposed framework Vis-MVSNet significantly improves depth accuracies in the scenes with severe occlusion. Extensive experiments are performed on DTU, BlendedMVS, and Tanks and Temples datasets to justify the effectiveness of the proposed framework."
slides-id: 38933970
channel-id: "paper_057_P2_id_0421"
---
