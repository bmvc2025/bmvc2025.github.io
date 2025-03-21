---
layout: default_paper
id: 634
order: 78
poster_session: 2
session_id: 5
title: "Neural Network Quantization with Scale-Adjusted Training"
authors:
  - author: "Qing Jin (Bytedance, Inc. & Texas A&M University)"
  - author: "Linjie Yang (ByteDance AI Lab)"
  - author: "Zhenyu Liao (Kwai Inc)"
  - author: "Xiaoning Qian (Texas A&M University)"
all_authors: "Qing Jin, Linjie Yang, Zhenyu Liao and Xiaoning Qian"
code: ""
keywords:
  - word: "neural network quantization"
  - word: "over-fitting"
  - word: "regularization"
paper: "papers/0634.pdf"
supp: "supp/0634_supp.pdf"
abstract: "Quantization has long been studied as a compression and accelerating technique for deep neural networks due to its potential on reducing model size and computational costs, for both general hardware, such as DSP, CPU or GPU, and customized devices with flexible bit-width configurations, including FPGA and ASIC. However, previous works generally achieve network quantization by sacrificing on prediction accuracy with respect to their full-precision counterparts. In this paper, we investigate the underlying mechanism of such performance degeneration based on previous work of parameterized clipping activation (PACT). We find that the key factor is the weight scale in the last layer. Instead of aligning weight distributions of quantized and full-precision models, as generally suggested in the literature, the main issue is that large scale can cause over-fitting problem. We propose a technique called scale-adjusted training (SAT) by directly scaling down weights in the last layer to alleviate such over-fitting. With the proposed technique, quantized networks can demonstrate better performance than their full-precision counter-parts, and we achieve state-of-the-art accuracy with consistent improvement over previous quantization methods for light weight models including MobileNet V1/V2 on ImageNet classification."
slides-id: 38934009
channel-id: "paper_078_P2_id_0634"
---
