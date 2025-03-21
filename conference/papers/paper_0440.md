---
layout: default_paper
id: 440
order: 85
poster_session: 2
session_id: 5
title: "Align-and-Attend Network for Globally and Locally Coherent Video Inpainting"
authors:
  - author: "Sanghyun Woo (KAIST)"
  - author: "Dahun Kim (KAIST)"
  - author: "KwanYong Park (KAIST)"
  - author: "Joon-Young Lee (Adobe Research)"
  - author: "In So Kweon (KAIST, Korea)"
all_authors: "Sanghyun Woo, Dahun Kim, KwanYong Park, Joon-Young Lee and In So Kweon"
code: ""
keywords:
  - word: "Video Inpainting"
  - word: "Video Processing"
  - word: "Spatio-Temporal Alignment"
  - word: "Spatio-Temporal Non-local Attention"
paper: "papers/0440.pdf"
supp: "supp/0440_supp.zip"
abstract: "Video inpainting is more challenging than image inpainting because of the extra temporal dimension. It requires inpainted contents to be globally coherent in both space and time. A natural solution for this problem is aggregating features from other frames, and thus, existing state-of-the-art methods rely heavily on 3D convolution or optical flow. However, these methods emphasize more on the temporally nearby frames, and long-term temporal information is not sufficiently stressed. In this work, we propose a novel two-stage alignment method. The first stage is an alignment module that uses computed homographies between the target frame and the reference frames. The visible patches are then aggregated based on the frame similarity to fill in the target holes roughly. Despite being able to model only global transformations, we empirically verify that homography-based alignment allows larger temporal window size than the flow-based counterpart. The second stage is an attention module that matches the generated patches with known reference patches in a non-local manner to refine the previous global alignment stage. Both stages consist of large spatial-temporal window size for the reference and thus enable modeling long-range correlations between distant information and the hole regions. Finally, even challenging scenes with large or slowly moving holes can be handled, which have been hardly modeled by existing approaches. Experiments on video object removal demonstrate that our method significantly outperforms previous state-of-the-art learning approaches."
slides-id: 38933974
channel-id: "paper_085_P2_id_0440"
---
