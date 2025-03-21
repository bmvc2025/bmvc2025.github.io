---
layout: default_paper
id: 209
order: 94
poster_session: 2
session_id: 5
title: "When Humans Meet Machines: Towards Efficient Segmentation Networks"
authors:
  - author: "Peike Li (UTS)"
  - author: "Xuanyi Dong (University of Technology Sydney)"
  - author: "Xin Yu (University of Technology Sydney)"
  - author: "Yi Yang (UTS)"
all_authors: "Peike Li, Xuanyi Dong, Xin Yu and Yi Yang"
code: ""
keywords:
  - word: "semantic segmentation"
  - word: "efficient network"
  - word: "neural architecture search"
  - word: "network design"
  - word: ""
paper: "papers/0209.pdf"
supp: "supp/0209_supp.zip"
abstract: "In this paper, we investigate how to achieve a high-performance yet lightweight segmentation network for real-time applications. By analyzing three typical segmentation networks, we observe that the segmentation backbones and heads are often imbalanced which restricts network efficiency. Thus, we develop a lightweight context fusion (LCF) module and a lightweight global enhancement (LGE) module to construct our lightweight segmentation head. Specifically, LCF fuses multi-resolution features to capture image details and LGE is designed to enhance feature representations. In this manner, our lightweight head facilities network efficiency and significantly reduces network parameters. Furthermore, we design a Multi-Resolution Macro Segmentation structure (MRMS) to incorporate human knowledge into our network architecture composition. Given the resource-aware constraint (e.g., latency time), we optimize our network with network architecture search while considering the relationships among atomic operators, network depth and feature resolution in segmentation tasks. Since MRMS embeds the segmentation-specific knowledge, it also provides a better architecture search space. Our Human-Machine collaboratively designed Segmentation network (HMSeg) achieves better performance and faster inference speed. Experiments demonstrate that our network achieves 71.4% mean intersection over union (mIOU) on Cityscapes with only 0.7M parameters at 172.4 FPS on NVIDIA GTX1080Ti."
slides-id: 38933918
channel-id: "paper_094_P2_id_0209"
---
