---
layout: default_paper
id: 129
order: 28
poster_session: 1
session_id: 2
title: "ASAP-Net: Attention and Structure Aware Point Cloud Sequence Segmentation"
authors:
  - author: "Hanwen Cao (Shanghai Jiao Tong University)"
  - author: "Yongyi Lu (Johns Hopkins University)"
  - author: "Bo Pang (Shanghai Jiao Tong University)"
  - author: "Cewu Lu (Shanghai Jiao Tong University)"
  - author: "Alan Yuille (Johns Hopkins University)"
  - author: "Gongshen Liu (Shanghai Jiao Tong University)"
all_authors: "Hanwen Cao, Yongyi Lu, Bo Pang, Cewu Lu, Alan Yuille and Gongshen Liu"
code: "https://github.com/intrepidChw/ASAP-Net"
keywords:
  - word: "Point Cloud Sequence"
  - word: "Semantic Segmentation"
paper: "papers/0129.pdf"
supp: ""
abstract: "Recent works of point clouds show that mulit-frame spatio-temporal modeling outperforms single-frame versions by utilizing cross-frame information. In this paper, we further improve spatio-temporal point cloud feature learning with a flexible module called ASAP considering both attention and structure information across frames, which we find as two important factors for successful segmentation in dynamic point clouds. Firstly, our ASAP module contains a novel attentive temporal embedding layer to fuse the relatively informative local features across frames in a recurrent fashion. Secondly, an efficient spatio-temporal correlation method is proposed to exploit more local structure for embedding, meanwhile enforcing temporal consistency and reducing computation complexity. Finally, we show the generalization ability of the proposed ASAP module with different backbone networks for point cloud sequence segmentation. Our ASAP-Net (backbone plus ASAP module) outperforms baselines and previous methods on both Synthia and SemanticKITTI datasets (+3.4 to +15.2 mIoU points with different backbones). The source codes will be made publicly available."
slides-id: 38933897
channel-id: "paper_028_P1_id_0129"
---
