---
layout: default_paper
id: 962
order: 139
poster_session: 3
session_id: 8
title: "Thoracic Disease Identification and Localization using Distance Learning and Region Verification"
authors:
  - author: "Cheng Zhang (The Ohio State University)"
  - author: "Francine Chen (FX Palo Alto Laboratory)"
  - author: "Yan-Ying Chen (FX Pal)"
all_authors: "Cheng Zhang, Francine Chen and Yan-Ying Chen"
code: ""
keywords:
  - word: "Chest X-ray analysis"
  - word: "disease classification"
  - word: "disease localization"
  - word: "triplet learning"
  - word: "region verification"
  - word: "multi-class activation map."
paper: "papers/0962.pdf"
supp: ""
abstract: "The identification and localization of diseases in medical images using deep learning models have recently attracted significant interest. Existing methods only consider training the networks with each image independently and most leverage an activation map for disease localization. In this paper, we propose an alternative approach that learns discriminative features among triplets of images and cyclically trains on region features to verify whether attentive regions contain information indicative of a disease. Concretely, we adapt a distance learning framework for multi-label disease classification to differentiate subtle disease features. Additionally, we feed back the features of the predicted class-specific regions to a separate classifier during training to better verify the localized diseases. Our model can achieve state-of-the-art classification performance on the challenging Chest-Xray14 dataset, and our ablation studies indicate that both distance learning and region verification contribute to overall classification performance. Moreover, the distance learning and region verification modules can capture essential information for better localization than baseline models without these modules. "
slides-id: 38934053
channel-id: "paper_139_P3_id_0962"
---
