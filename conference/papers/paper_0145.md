---
layout: default_paper
id: 145
order: 95
poster_session: 2
session_id: 5
title: "Towards Fast and Light-Weight Restoration of Dark Images"
authors:
  - author: "mohit lamba (Indian Institute of Technology Madras)"
  - author: "Atul Balaji (Indian Institute of Technology Madras)"
  - author: "Kaushik Mitra (IIT Madras)"
all_authors: "Mohit Lamba, Atul Balaji and Kaushik Mitra"
code: "https://github.com/MohitLamba94/LLPackNet"
keywords:
  - word: "low light"
  - word: "low-light"
  - word: "dark image"
  - word: "image enhancement"
  - word: "low level"
  - word: "fast"
  - word: "image restoration"
  - word: ""
paper: "papers/0145.pdf"
supp: "supp/0145_supp.zip"
abstract: "The ability to capture good quality images in the dark and textit{near-zero lux} conditions has been a long-standing pursuit of the computer vision community. The seminal work by Chen etal cite{chen2018learning} has especially caused renewed interest in this area, resulting in methods that build on top of their work in a bid to improve the reconstruction. However, for practical utility and deployment of low-light enhancement algorithms on edge devices such as embedded systems, surveillance cameras, autonomous robots and smartphones, the solution must respect additional constraints such as limited GPU memory and processing power. With this in mind, we propose a deep neural network architecture that aims to strike a balance between the network latency, memory utilization, model parameters, and reconstruction quality. 
The key idea is to forbid any computation in the High-Resolution (HR) space and instead restrict most of the computations to Low-Resolution (LR) space. However, doing the bulk of computations in the LR space causes a lot of artifacts in the restored image. 
We propose textit{Pack} and textit{UnPack} operations, which allow us to effectively transit between the HR and LR spaces without incurring much artifacts in the restored image.
Most of the state-of-the-art algorithms on dark image enhancement need to pre-amplify the image before processing it. However, they generally use ground truth information to find the amplification factor even during inference,  
which restricts their applicability for unknown scenes. In contrast, we propose a simple yet effective light-weight mechanism for automatically determining the amplification factor from the input image itself.
We show that we can enhance a full resolution, $2848 times 4256$, extremely dark single-image in the ballpark of $3$ seconds even on a CPU. We achieve this with $2-7times$ fewer model parameters, $2-3times$ lower memory utilization, $5-20times$ speed up and yet maintain a competitive image reconstruction quality compared to the current state-of-the-art algorithms."
slides-id: 38933901
channel-id: "paper_095_P2_id_0145"
---
