---
layout: default_paper
id: 395
order: 166
poster_session: 4
session_id: 11
title: "View-consistent 4D Light Field Depth Estimation"
authors:
  - author: "Numair Khan (Brown University)"
  - author: "Min H. Kim (KAIST)"
  - author: "James Tompkin (Brown University)"
all_authors: "Numair Khan, Min H. Kim and James Tompkin"
code: "http://visual.cs.brown.edu/lightfielddepth"
keywords:
  - word: "light fields"
  - word: "depth estimation"
  - word: "angular consistency"
  - word: "epipolar plane images"
  - word: "depth inpainting"
  - word: "diffusion"
  - word: "light field editing"
paper: "papers/0395.pdf"
supp: "supp/0395_supp.mp4"
abstract: "We propose a method to compute depth maps for every sub-aperture image in a light field in a view consistent way. Previous light field depth estimation methods typically estimate a depth map only for the central sub-aperture view, and struggle with view consistent estimation. Our method precisely defines depth edges via EPIs, then we diffuse these edges spatially within the central view. These depth estimates are then propagated to all other views in an occlusion-aware way. Finally, disoccluded regions are completed by diffusion in EPI space. Our method runs efficiently with respect to both other classical and deep learning-based approaches, and achieves competitive quantitative metrics and qualitative performance on both synthetic and real-world light fields."
slides-id: 38933964
channel-id: "paper_166_P4_id_0395"
---
