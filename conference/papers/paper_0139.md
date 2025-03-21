---
layout: default_paper
id: 139
order: 103
oral_session: 6
poster_session: 3
session_id: 7
title: "BriNet: Towards Bridging the Intra-class and Inter-class Gaps in One-Shot Segmentation"
authors:
  - author: "Xianghui Yang (The University of Sydney)"
  - author: "Bairun Wang (SenseTime Group Limited)"
  - author: "Xinchi Zhou (The University of Sydney)"
  - author: "Kaige Chen (SenseTime Group Limited)"
  - author: "Shuai Yi (SenseTime Group Limited)"
  - author: "Wanli Ouyang (The University of Sydney)"
  - author: "Luping Zhou (University of Sydney)"
all_authors: "Xianghui Yang, Bairun Wang, Xinchi Zhou, Kaige Chen, Shuai Yi, Wanli Ouyang and Luping Zhou"
code: "https://github.com/Wi-sc/BriNet"
keywords:
  - word: "Few-shot Semantic Segmentation"
  - word: "Few-shot learning"
  - word: "Semantic Segmentation"
paper: "papers/0139.pdf"
supp: ""
abstract: "Few-shot segmentation focuses on the generalization of models to segment unseen object instances with limited training samples. Although tremendous improvements have been achieved, existing methods are still constrained by two factors. (1) The information interaction between query and support images is not adequate, leaving intra-class gap. (2) The object categories at the training and inference stages have no overlap, leaving the inter-class gap. Thus, we propose a framework, BriNet, to bridge these gaps. First, more information interactions are encouraged between the extracted features of the query and support images, i.e., using an Information Exchange Module to emphasize the common objects. Furthermore, to precisely localize the query objects, we design a multi-path fine-grained strategy which is able to make better use of the support feature representations. Second, a new online refinement strategy is proposed to help the trained model adapt to unseen classes, achieved by switching the roles of the query and the support images at the inference stage. The effectiveness of our framework is demonstrated by experimental results, which outperforms other competitive methods and leads to a new state-of-the-art on both PASCAL VOC and MSCOCO dataset."
slides-id: 38933900
channel-id: "paper_103_P3_id_0139"
---
