---
layout: default_paper
id: 193
order: 15
poster_session: 1
session_id: 2
title: "FairFaceGAN: Fairness-aware Facial Image-to-Image Translation"
authors:
  - author: "sunhee hwang (Yonsei university)"
  - author: "Sungho Park (Yonsei University)"
  - author: "Dohyung Kim (Yonsei University)"
  - author: "Mirae Do (Yonsei University)"
  - author: "Hyeran Byun (Yonsei University)"
all_authors: "Sunhee Hwang, Sungho Park, Dohyung Kim, Mirae Do and Hyeran Byun"
code: ""
keywords:
  - word: "fairness in computer vision"
  - word: "image-to-image translation"
  - word: "equality of opportunity"
  - word: "equalized odds"
paper: "papers/0193.pdf"
supp: "supp/0193_supp.pdf"
abstract: "In this paper, we introduce FairFaceGAN, a fairness-aware facial Image-to-Image translation model, mitigating the problem of unwanted translation in protected attributes (e.g., gender, age, race) during facial attributes editing. Unlike existing models, FairFaceGAN learns fair representations with two separate latents - one related to the target attributes to translate, and the other unrelated to them. This strategy enables FairFaceGAN to separate the information about protected attributes and that of target attributes. It also prevents unwanted translation in protected attributes while target attributes editing. To evaluate the degree of fairness, we perform two types of experiments on CelebA dataset. First, we compare the fairness-aware classification performances when augmenting data by existing image translation methods and FairFaceGAN respectively. Moreover, we propose a new fairness metric, namely Fréchet Protected Attribute Distance (FPAD), which measures how well protected attributes are preserved. Experimental results demonstrate that FairFaceGAN shows consistent improvements in terms of fairness over the existing image translation models. Further, we also evaluate image translation performances, where FairFaceGAN shows competitive results, compared to those of existing methods.
"
slides-id: 38933915
channel-id: "paper_015_P1_id_0193"
---
