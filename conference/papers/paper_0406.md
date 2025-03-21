---
layout: default_paper
id: 406
order: 143
poster_session: 3
session_id: 8
title: "Loss Functions for Person Image Generation"
authors:
  - author: "Haoyue Shi (Xi’an Jiaotong University)"
  - author: "Le Wang (Xi'an Jiaotong University)"
  - author: "Wei Tang (University of Illinois at Chicago)"
  - author: "Nanning Zheng (Xi'an Jiaotong University)"
  - author: "Gang Hua (Wormpex AI Research)"
all_authors: "Haoyue Shi, Le Wang, Wei Tang, Nanning Zheng and Gang Hua"
code: ""
keywords:
  - word: "person image generation"
  - word: "pose transfer"
  - word: "generative adversarial networks"
  - word: "structural similarity loss"
paper: "papers/0406.pdf"
supp: ""
abstract: "Pose-guided person image generation aims to transform a source person image to a target pose. It is an ill-posed problem as we often need to generate pixels that are invisible in the source image. Recent works focus on designing new architectures of deep neural networks and have shown promising results. However, they simply adopt the loss functions commonly used for generic image synthesis and restoration, e.g., L1 loss, adversarial loss, and perceptual loss. This can be suboptimal due to the unique appearance and structure patterns of person images. In this paper, we first have a comprehensive study of the strengths and weaknesses of these prior loss functions for person image generation. We also consider the structural similarity index (SSIM) as a loss function since it is widely used as the evaluation metric and can capture the perceptual quality of generated images. Moreover, motivated by the observation that a person can be divided into part regions with homogeneous pixel values or textures, we extend the SSIM into a novel part-based similarity loss to explicitly account for the articulated body structure. Quantitative and qualitative results indicate that (1) using different loss functions significantly impacts the generated person images and (2) the proposed part-based loss is complementary to the prior losses and helps improve the performance."
slides-id: 38933967
channel-id: "paper_143_P3_id_0406"
---
