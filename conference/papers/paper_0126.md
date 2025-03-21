---
layout: default_paper
id: 126
order: 12
poster_session: 1
session_id: 2
title: "High-speed Light-weight CNN Inference via Strided Convolutions on a Pixel Processor Array"
authors:
  - author: "Yanan Liu (University of Bristol)"
  - author: "Laurie Bose (University of Bristol)"
  - author: "Jianing Chen (The University of Manchester)"
  - author: "Stephen Carey (The University of Manchester)"
  - author: "Piotr Dudek (School of Electrical and Electronic Engineering, The University of Manchester, UK)"
  - author: "Walterio Mayol-Cuevas (Bristol University)"
all_authors: "Yanan Liu, Laurie Bose, Jianing Chen, Stephen Carey, Piotr Dudek and Walterio Mayol-Cuevas"
code: "https://github.com/yananliusdu/scamp/tree/master"
keywords:
  - word: "Binary CNN"
  - word: "CNN on embedded system"
  - word: "Pixel Processor Array"
  - word: "SCAMP"
  - word: "high-speed CNN"
  - word: "Light-weight CNN"
paper: "papers/0126.pdf"
supp: ""
abstract: "Performance, storage, and power consumption are three major factors that restrict the use of machine learning algorithms on embedded systems. However, new hardware architectures designed with visual computation in mind may hold the key to solving these bottlenecks. This work makes use of a novel visual device: the pixel processor array (PPA), to embed a convolutional neural network (CNN) onto the focal plane. We present a new high-speed implementation of strided convolutions using binary weights for the CNN on PPA devices, allowing all multiplications to be replaced by more efficient addition/subtraction operations. Image convolutions, ReLU activation functions, max-pooling and a fully-connected layer are all performed directly on the PPA’s imaging plane, exploiting its massive parallel computing capabilities. We demonstrate CNN inference across 4 different applications, running between 2,000 and 17,500 fps with power consumption lower than 1.5W. These tasks include identifying 8 classes of plankton, hand gesture classification and digit recognition."
slides-id: 38933896
channel-id: "paper_012_P1_id_0126"
---
