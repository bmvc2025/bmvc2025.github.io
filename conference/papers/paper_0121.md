---
layout: default_paper
id: 121
order: 140
poster_session: 3
session_id: 8
title: "Image Harmonization with Attention-based Deep Feature Modulation"
authors:
  - author: "Guoqing Hao (University of Tsukuba)"
  - author: "Satoshi Iizuka (University of Tsukuba)"
  - author: "Kazuhiro Fukui (University of Tsukuba)"
all_authors: "Guoqing Hao, Satoshi Iizuka and Kazuhiro Fukui"
code: "https://github.com/Dominoer/bmvc2020_image_harmonization"
keywords:
  - word: "image harmonization"
  - word: "feature map modulation"
  - word: "attention"
paper: "papers/0121.pdf"
supp: "supp/0121_supp.zip"
abstract: "We present a learning-based approach for image harmonization, which allows for adjusting the appearance of the foreground to make it compatible with background. We consider improving the realism by adjusting the high-level feature statistics of the foreground according to those of the background, which is motivated by the fact that specific image statistics between the foreground and background typically match in realistic composite images. Based on a fully convolutional network, we propose a novel attention-based module that aligns the standard deviation of the foreground features with that of the background features, capturing global dependencies in the entire image. This module is easily inserted into any convolutional neural networks, and allows improving the harmony of the composites with only a small additional computational cost. Experimental results on the image harmonization dataset and real composite images show that our method outperforms existing methods both quantitatively and qualitatively. Furthermore, in our experiment, our module is able to boost existing harmonization networks by simply inserting it into intermediate layers of those networks."
slides-id: 38933894
channel-id: "paper_140_P3_id_0121"
---
