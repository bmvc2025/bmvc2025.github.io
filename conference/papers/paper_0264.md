---
layout: default_paper
id: 264
order: 19
poster_session: 1
session_id: 2
title: "Object Detection as a Positive-Unlabeled Problem"
authors:
  - author: "Yuewei Yang (Duke University)"
  - author: "Kevin Liang (Duke University)"
  - author: "Lawrence Carin Duke (CS)"
all_authors: "Yuewei Yang, Kevin Liang and Lawrence Carin Duke"
code: ""
keywords:
  - word: "object detections"
  - word: "positive unlabeled learning"
  - word: ""
paper: "papers/0264.pdf"
supp: "supp/0264_supp.pdf"
abstract: "As with other deep learning methods, label quality is important for learning modern convolutional object detectors. However, the potentially large number and wide diversity of object instances that can be found in complex image scenes makes constituting complete annotations a challenging task. Indeed, objects missing annotations can be observed in a variety of popular object detection datasets. These missing annotations can be problematic, as the standard cross-entropy loss employed to train object detection models treats classification as a positive-negative (PN) problem: unlabeled regions are implicitly assumed to be background. As such, any object missing a bounding box results in a confusing learning signal, the effects of which we observe empirically. To remedy this, we propose treating object detection as a positive-unlabeled (PU) problem, which removes the assumption that unlabeled regions must be negative. We demonstrate that our proposed PU classification loss outperforms the standard PN loss on PASCAL VOC and MS COCO across a range of label missingness, as well as on Visual Genome and DeepLesion with full labels."
slides-id: 38933935
channel-id: "paper_019_P1_id_0264"
---
