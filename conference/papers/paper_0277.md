---
layout: default_paper
id: 277
order: 55
oral_session: 4
poster_session: 2
session_id: 4
title: "A CNN Based Approach for the Near-Field Photometric Stereo Problem"
authors:
  - author: "Fotios Logothetis (Toshiba research)"
  - author: "Ignas Budvytis (Department of Engineering, University of Cambridge)"
  - author: "Roberto Mecca (cambridge university)"
  - author: "Roberto Cipolla (University of Cambridge)"
all_authors: "Fotios Logothetis, Ignas Budvytis, Roberto Mecca and Roberto Cipolla"
code: ""
keywords:
  - word: "Photometric Stereo"
  - word: "BRDF"
  - word: "Rendering"
paper: "papers/0277.pdf"
supp: ""
abstract: "Reconstructing the 3D shape of an object using several images under different light sources is a very challenging task, especially when realistic assumptions such as light propagation and attenuation, perspective viewing geometry and specular light reflection are considered. Many of works tackling Photometric Stereo (PS) problems often relax most of the aforementioned assumptions. Especially they ignore specular reflection and global illumination effects. In this work, we propose the first CNN based approach capable of handling these realistic assumptions in Photometric Stereo. We leverage recent improvements of deep neural networks for far-field Photometric Stereo and adapt them to near field setup. We achieve this by employing an iterative procedure for shape estimation which has two main steps. Firstly we train a per-pixel CNN to predict surface normals from reflectance samples. Secondly, we compute the depth by integrating the normal field in order to iteratively estimate light directions and attenuation which is used to compensate the input images to compute reflectance samples for the next iteration. To the best of our knowledge this is the first near-field framework which is able to accurately predict 3D shape from highly specular objects. Our method outperforms competing state-of-the-art near-field Photometric Stereo approaches on both synthetic and real experiments."
slides-id: 38933939
channel-id: "paper_055_P2_id_0277"
---
