---
layout: default_paper
id: 694
order: 51
oral_session: 3
poster_session: 2
session_id: 3
title: "Fast Convex Relaxations using Graph Discretizations"
authors:
  - author: "Jonas Geiping (University of Siegen)"
  - author: "Fjedor Gaede (Westfälische Wilhelms Universität Münster)"
  - author: "Hartmut Bauermeister (University of Siegen)"
  - author: "Michael Moeller (University of Siegen)"
all_authors: "Jonas Geiping, Fjedor Gaede, Hartmut Bauermeister and Michael Moeller"
code: ""
keywords:
  - word: "Minimal Partitions"
  - word: "Convex Relaxation"
  - word: "Mumford-Shah"
  - word: "Matching"
  - word: "Segmentation"
  - word: "Stereo Estimation"
  - word: "Superpixels"
  - word: ""
paper: "papers/0694.pdf"
supp: ""
abstract: "   Matching and partitioning problems are fundamentals of computer vision applications with examples in multilabel segmentation, stereo estimation and optical-flow computation. These tasks can be posed as non-convex energy minimization problems and solved near-globally optimal by recent convex lifting approaches. Yet, applying these techniques comes with a significant computational effort, reducing their feasibility in practical applications. We discuss spatial discretization of continuous partitioning problems into a graph structure, generalizing discretization onto a Cartesian grid. This setup allows us to faithfully work on super-pixel graphs constructed by SLIC or Cut-Pursuit,
    massively decreasing the computational effort for lifted partitioning problems compared to a Cartesian grid, while optimal energy values remain similar: The global matching is still solved near-globally optimal.
   We discuss this methodology in detail and show examples in multi-label segmentation by minimal partitions and stereo estimation, where we demonstrate that the proposed graph discretization can reduce runtime as well as memory consumption of convex relaxations of matching problems by up to a factor of 10. "
slides-id: 38934019
channel-id: "paper_051_P2_id_0694"
---
