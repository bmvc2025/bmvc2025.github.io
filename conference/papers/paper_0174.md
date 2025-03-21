---
layout: default_paper
id: 174
order: 46
poster_session: 1
session_id: 2
title: "Boosting Image and Video Compression via Learning Latent Residual Patterns"
authors:
  - author: "Yen-Chung Chen (National Chiao Tung University)"
  - author: "Keng-Jui Chang (National Chiao Tung University)"
  - author: "Yi-Hsuan Tsai (NEC Labs America)"
  - author: "Wei-Chen Chiu (National Chiao Tung University)"
all_authors: "Yen-Chung Chen, Keng-Jui Chang, Yi-Hsuan Tsai and Wei-Chen Chiu"
code: ""
keywords:
  - word: "compression artifacts"
  - word: "image compression"
  - word: "video compression"
  - word: "latent residual"
  - word: ""
paper: "papers/0174.pdf"
supp: ""
abstract: "Reducing compression artifacts is essential for streaming videos with a better quality under a limited bandwidth. To tackle this problem, existing methods aim to directly recover details from the compressed video but do not consider learning rich information in uncompressed videos to aid this process. In this paper, we focus on utilizing the residual information, which is the difference between a compressed video and its corresponding original/uncompressed one, and propose a fairly efficient way to transmit the residual with the compressed video in order to boost the quality of video compression. Our proposed method is realized by learning to discover the patterns in the residual and storing them offline as dictionary-like patterns. During the testing stage, e.g., for video streaming, the residual is transmitted in the form of pattern indexes to reduce the cost of communication, and thus the original residual information can be easily retrieved back from the dictionary of learned residual patterns. We show the effectiveness of our framework on numerous datasets under various video compression coding methods. In addition, the proposed pipeline can be widely applied to the image compression task and reduce artifacts produced from conventional and CNN-based compression algorithms."
slides-id: 38933909
channel-id: "paper_046_P1_id_0174"
---
