---
layout: default_paper
id: 400
order: 124
poster_session: 3
session_id: 8
title: "From Quantized DNNs to Quantizable DNNs"
authors:
  - author: "Kunyuan Du (Cooperative Medianet Innovation Center, Shang hai Jiao Tong University)"
  - author: "Ya Zhang (Cooperative Medianet Innovation Center, Shang hai Jiao Tong University)"
  - author: "Haibing Guan (Shanghai Jiao Tong University)"
all_authors: "Kunyuan Du, Ya Zhang and Haibing Guan"
code: ""
keywords:
  - word: "Quantized DNNs"
  - word: "Dynamic Bit-width"
paper: "papers/0400.pdf"
supp: ""
abstract: "This paper proposes Quantizable DNNs, a special type of DNNs that can flexibly quantize its bit-width (denoted as `bit modes' thereafter) during execution without further re-training. To simultaneously optimize all bit modes, a combinational loss of all bit modes is proposed, which enforces consistent predictions ranging from low-bit mode to 32-bit mode. This consistency-based loss may also be viewed as certain form of regularization during training. Because outputs of matrix multiplication in different bit modes have different distributions, we introduce Bit-Specific Batch Normalization so as to reduce conflicts among different bit modes. Experiments on CIFAR100 and ImageNet have shown that compared to quantized DNNs, quantizable DNNs not only have much better flexibility, but also achieve even higher classification accuracy. Ablation studies further verify that the regularization through the consistency-based loss indeed improves the model's generalization performance. Source codes will be released in the future."
slides-id: 38933965
channel-id: "paper_124_P3_id_0400"
---
