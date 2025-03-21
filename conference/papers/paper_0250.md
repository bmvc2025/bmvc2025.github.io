---
layout: default_paper
id: 250
order: 187
poster_session: 4
session_id: 11
title: "BiHand: Recovering Hand Mesh with Multi-stage Bisected Hourglass Networks"
authors:
  - author: "Lixin Yang (Shanghai Jiao Tong University)"
  - author: "Jiasen Li (Shanghai Jiao Tong University)"
  - author: "Wenqiang Xu (Shanghai Jiao Tong University)"
  - author: "Yiqun Diao (Shanghai Jiao Tong University)"
  - author: "Cewu Lu (Shanghai Jiao Tong University)"
all_authors: "Lixin Yang, Jiasen Li, Wenqiang Xu, Yiqun Diao and Cewu Lu"
code: "https://github.com/lixiny/bihand"
keywords:
  - word: "hand pose estimation"
  - word: "3d hand"
  - word: "hand reconstruction"
  - word: "hand mesh"
  - word: ""
paper: "papers/0250.pdf"
supp: ""
abstract: "3D hand estimation has been a long-standing research topic in computer vision. A recent trend aims not only to estimate the 3D hand joint locations but also to recover the mesh model. However, achieving those goals from a single RGB image remains challenging. In this paper, we introduce an end-to-end learnable model, BiHand, which consists of three cascaded stages, namely 2D seeding stage, 3D lifting stage, and mesh generation stage. At the output of BiHand, the full hand mesh will be recovered using the joint rotations and shape parameters predicted from the network. Inside each stage, BiHand adopts a novel bisecting design which allows the networks to encapsulate two closely related information (e.g. 2D keypoints and silhouette in 2D seeding stage, 3D joints, and depth map in 3D lifting stage, joint rotations and shape parameters in the mesh generation stage) in a single forward pass. As the information represents different geometry or structure details, bisecting the data flow can facilitate optimization and increase robustness. For quantitative evaluation, we conduct experiments on two public benchmarks, namely the Rendered Hand Dataset (RHD) and the Stereo Hand Pose Tracking Benchmark (STB). Extensive experiments show that our model can achieve superior accuracy in comparison with state-of-the-art methods, and can produce appealing 3D hand meshes in several severe conditions. The training codes, model and dataset are publicly available at https://github.com/lixiny/bihand."
slides-id: 38933932
channel-id: "paper_187_P4_id_0250"
---
