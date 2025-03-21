---
layout: default_paper
id: 51
order: 107
poster_session: 3
session_id: 8
title: "Novel View Synthesis from Single Images via Point Cloud Transformation"
authors:
  - author: "Hoang-An Le (University of Amsterdam)"
  - author: "Thomas Mensink (Google Research / University of Amsterdam)"
  - author: "Partha Das (University of Amsterdam)"
  - author: "Theo Gevers (University of Amsterdam)"
all_authors: "Hoang-An Le, Thomas Mensink, Partha Das and Theo Gevers"
code: "https://github.com/lhoangan/pc4novis"
keywords:
  - word: "novel view synthesis single images self-supervised depth estimation point cloud construction"
paper: "papers/0051.pdf"
supp: ""
abstract: "In this paper the argument is made that for true novel view synthesis of objects, where the object can be synthesized from any viewpoint, an explicit 3D shape representation is desired. Our method estimates point clouds to capture the geometry of the object, which can be freely rotated into the desired view and then projected into a new image. This image, however, is sparse by nature and hence this coarse view is used as the input of an image completion network to obtain the dense target view. The point cloud is obtained using the predicted pixel-wise depth map, estimated from a single RGB input image, combined with the camera intrinsics. By using forward warping and backward warping between the input view and the target view, the network can be trained end-to-end without supervision on depth. The benefit of using point clouds as an explicit 3D shape for novel view synthesis is experimentally validated on the 3D ShapeNet benchmark."
slides-id: 38933874
channel-id: "paper_107_P3_id_0051"
---
