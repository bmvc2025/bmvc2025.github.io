---
layout: default_paper
id: 275
order: 83
poster_session: 2
session_id: 5
title: "Superpixel Masking and Inpainting for Self-Supervised Anomaly Detection"
authors:
  - author: "Zhenyu Li (Xi’an Jiaotong University(XJTU))"
  - author: "Ning Li (Xi'an Jiaotong University)"
  - author: "Kaitao Jiang (Xi'an Jiaotong University)"
  - author: "Zhiheng Ma (Xi'an Jiaotong University)"
  - author: "Xing Wei (Xi'an Jiaotong University)"
  - author: "Xiaopeng Hong (Xi'an Jiaotong University)"
  - author: "Yihong Gong (Xi'an Jiaotong University)"
all_authors: "Zhenyu Li, Ning Li, Kaitao Jiang, Zhiheng Ma, Xing Wei, Xiaopeng Hong and Yihong Gong"
code: ""
keywords:
  - word: "Anomaly Detection"
  - word: "Self-supervise"
  - word: "Inpainting"
  - word: "Superpixel"
paper: "papers/0275.pdf"
supp: ""
abstract: "Anomaly detection aims at identifying abnormal samples from the normal ones. Existing methods are usually supervised or detect anomalies at the instance level without localization. In this work, we propose an unsupervised method called Superpixel Masking And Inpainting (SMAI) to identify and locate anomalies in images. Specifically, superpixel segmentation is first performed on the images. Then an inpainting module is trained to learn the spatial and texture information of the normal samples through random superpixel masking and restoration. Therefore, the model can reconstruct the superpixel mask with normal content. At the inference stage, we mask the image using superpixels and restore them one by one. By comparing the mask areas of the original image and its reconstruction, we can identify and locate the abnormal regions. We conducted a comprehensive evaluation of SMAI on the latest MVTec anomaly detection dataset, and it shows that SMAI plays favorably against state-of-the-art methods."
slides-id: 38933938
channel-id: "paper_083_P2_id_0275"
---
