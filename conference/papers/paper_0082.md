---
layout: default_paper
id: 82
order: 33
poster_session: 1
session_id: 2
title: "Cross-dataset Color Constancy Revisited Using Sensor-to-Sensor Transfer"
authors:
  - author: "Samu Koskinen (Huawei Technologies Oy (Finland) Co. Ltd)"
  - author: "Dan Yang (Tampere University)"
  - author: "Joni-Kristian Kamarainen (Tampere University)"
all_authors: "Samu Koskinen, Dan Yang and Joni-Kristian Kamarainen"
code: ""
keywords:
  - word: "color constancy"
  - word: "white balance"
  - word: "sensor-to-sensor transfer"
  - word: "illuminant augmentation"
  - word: "cross-dataset benchmark"
  - word: "raw to spectral image"
paper: "papers/0082.pdf"
supp: ""
abstract: "Color constancy is required for camera captured images and therefore all digital camera imaging pipelines include an Auto White Balance (AWB) algorithm. An intrinsic problem of AWB is that it is sensor specific and therefore developers need to repeatedly collect new in-house datasets to adjust their methods for new sensors. In literature, the best learning-based methods achieve state-of-the-art performance with clear margin on all available datasets, but performance significantly degrades in cross-dataset experiments due to the aforementioned reason. In this work, we introduce a sensor-to-sensor transfer model that can be used to map datasets with known cameras to any other known camera. The only requirement is that spectral characterizations of the camera models are available. In our experiments, we demonstrate improvements in cross-dataset settings using the proposed sensor-to-sensor transfer model. In addition, for the first time we are able to analyze the characteristics of existing datasets in the common standard observer space and our analysis reveals that certain datasets contain images which are not suitable for color constancy. We introduce a unified cross-dataset color constancy benchmark dataset, compare two state-of-the-art learning-based AWB methods and show superior performance of the proposed sensor-to-sensor model."
slides-id: 38933882
channel-id: "paper_033_P1_id_0082"
---
