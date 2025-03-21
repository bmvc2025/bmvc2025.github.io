---
layout: default_paper
id: 16
order: 11
poster_session: 1
session_id: 2
title: "CornerNet-Lite: Efficient Keypoint based Object Detection"
authors:
  - author: "Hei Law (Princeton University)"
  - author: "Yun Teng (Princeton University)"
  - author: "Olga Russakovsky (Princeton University)"
  - author: "Jia Deng (Princeton University)"
all_authors: "Hei Law, Yun Teng, Olga Russakovsky and Jia Deng"
code: "https://github.com/princeton-vl/CornerNet-Lite"
keywords:
  - word: "detection"
  - word: "objects"
  - word: "efficiency"
  - word: "efficient"
  - word: "keypoint"
  - word: "real-time"
paper: "papers/0016.pdf"
supp: ""
abstract: "Keypoint-based methods are a relatively new paradigm in object detection, eliminating the need for anchor boxes and offering a simplified detection framework. Keypoint-based CornerNet achieves state of the art accuracy among single-stage detectors. However, this accuracy comes at high processing cost. In this work, we tackle the problem of efficient keypoint-based object detection and introduce CornerNet-Lite. CornerNet-Lite is a combination of two efficient variants of CornerNet: CornerNet-Saccade, which uses an attention mechanism to eliminate the need for exhaustively processing all pixels of the image, and CornerNet-Squeeze, which introduces a new compact backbone architecture. Together these two variants address the two critical use cases in efficient object detection: improving efficiency without sacrificing accuracy, and improving accuracy at real-time efficiency. CornerNet-Saccade is suitable for offline processing, improving the efficiency of CornerNet by 6.0x and the AP by 1.0% on COCO. CornerNet-Squeeze is suitable for real-time detection, improving both the efficiency and accuracy of the popular real-time detector YOLOv3 (34.4% AP at 30ms for CornerNet-Squeeze compared to 33.0% AP at 39ms for YOLOv3 on COCO). Together these contributions for the first time reveal the potential of keypoint-based detection to be useful for applications requiring processing efficiency."
slides-id: 38933866
channel-id: "paper_011_P1_id_0016"
---
