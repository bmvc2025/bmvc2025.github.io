---
layout: default_paper
id: 975
order: 181
poster_session: 4
session_id: 11
title: "Unsupervised Monocular Depth Estimation with Multi-Baseline Stereo"
authors:
  - author: "Saad Imran (Korea Advanced Institute of Science and Technology)"
  - author: "Muhammad Umar Karim Khan (Korea Advanced Institute of Science and Technology)"
  - author: "Sikander Mukaram (Korea Advanced Institute of Science and Technology (KAIST))"
  - author: "Chong-Min Kyung (Korea Advanced Institute of Science and Technology)"
all_authors: "Saad Imran, Muhammad Umar Karim Khan, Sikander Mukaram and Chong-Min Kyung"
code: "https://github.com/saadi297/MultiBaselineDepth"
keywords:
  - word: "Unsupervised Monocular Depth"
  - word: "Small-Baseline"
  - word: "Wide-Baseline"
  - word: "Multi-Baseline"
  - word: "Stereo"
  - word: ""
paper: "papers/0975.pdf"
supp: "supp/0975_supp.zip"
abstract: "Unsupervised deep learning methods have shown promising performance for single-image depth estimation. Since most of these methods use binocular stereo pairs for self-supervision, the depth range is generally limited. Small-baseline stereo pairs provide small depth range but handle occlusions well. On the other hand, stereo images acquired with a wide-baseline rig cause occlusions-related errors in the near range but estimate depth well in the far range. In this work, we propose to integrate the advantages of the small and wide baselines. By training the network using three horizontally aligned views, we obtain accurate depth predictions for both close and far ranges. Our strategy allows to infer multi-baseline depth from a single image. This is unlike previous multi-baseline systems which employ more than two cameras. The qualitative and quantitative results show the superior performance of multi-baseline approach over previous stereo-based monocular methods. For 0.1 to 80 meters depth range, our approach decreases the absolute relative error of depth by 24% compared to Monodepth2. Our approach provides 21 frames per second on a single Nvidia1080 GPU, making it useful for practical applications."
slides-id: 38934054
channel-id: "paper_181_P4_id_0975"
---
