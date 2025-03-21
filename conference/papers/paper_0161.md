---
layout: default_paper
id: 161
order: 40
poster_session: 1
session_id: 2
title: "Visualizing point cloud classifiers by curvature smoothing"
authors:
  - author: "Chen Ziwen (Grinnell College)"
  - author: "Wenxuan Wu (Oregon State University)"
  - author: "Zhongang Qi (Tencent)"
  - author: "Li Fuxin (Oregon State University)"
all_authors: "Chen Ziwen, Wenxuan Wu, Zhongang Qi and Li Fuxin"
code: "https://github.com/arthurhero/PC-IGOS"
keywords:
  - word: "point cloud"
  - word: "visualization"
  - word: "explainable AI"
  - word: "pointconv"
  - word: ""
paper: "papers/0161.pdf"
supp: "supp/0161_supp.pdf"
abstract: "Recently, several networks that operate directly on point clouds have been proposed. There is significant utility in understanding their mechanisms to classify point clouds, which can potentially help diagnosing them and designing better architectures.  In this paper, we propose a novel learning-based approach to visualize features important to the point cloud classifiers. Our approach is based on deleting and inserting curvatures on a point cloud. The resulting point cloud is then evaluated on the original point cloud network to assess the importance of the feature. A technical contribution of the paper is an approximated curvature smoothing algorithm, which can smoothly transition from the original point cloud to one of constant curvature, such as a uniform sphere. We propose PCI-GOS (Point Cloud Integrated-Gradients Optimized Saliency), a visualization technique that can automatically find the minimal saliency map that covers the most important features on a shape. Experiment results revealed insights into those classifiers."
slides-id: 38933906
channel-id: "paper_040_P1_id_0161"
---
