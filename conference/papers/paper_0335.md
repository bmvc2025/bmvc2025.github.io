---
layout: default_paper
id: 335
order: 164
poster_session: 4
session_id: 11
title: "Learning To Pay Attention To Mistakes"
authors:
  - author: "Moucheng Xu (UCL)"
  - author: "Neil Oxtoby (University College London)"
  - author: "Daniel Alexander (University College London)"
  - author: "Joseph Jacob (University College London)"
all_authors: "Moucheng Xu, Neil Oxtoby, Daniel Alexander and Joseph Jacob"
code: ""
keywords:
  - word: "attention"
  - word: "effective receptive field"
  - word: "segmentation"
  - word: "medical image"
  - word: "inductive bias"
paper: "papers/0335.pdf"
supp: ""
abstract: "In Convolutional Neural Network based medical image segmentation, the periphery of foreground regions representing malignant tissues may be disproportionately assigned as belonging to the background class as healthy tissues. As evidenced in visual results in [18][21][24][12][4], misclassification of foreground pixels as the background class can lead to high False Negative detection rates. In this paper, we propose a novel attention mechanism to directly address such high false negative rates, called Paying Attention to False Positives. Our attention mechanism attempts to steer the models towards false positive identification, thereby addressing the bias towards high false negative rates in segmentation outcomes. The proposed mechanism has two complementary implementations: (a) “explicit” steering of the model to attend to the “enlarged” Effective Receptive Field on the foreground areas; (b) “implicit” learning towards false positives, by attending to the “shrunken” Effective Receptive Field on the background areas. We first compare our models with state-of-the-art attention baselines in medical imaging, on a binary
dense prediction task between vehicles and the background using CityScapes. We then perform a second task which is to segment Enhanced Tumour Core areas in multi-modal MRI scans from the BRATS2018 datast, under 5-fold cross validation. In the second task, we include more baselines including self-attention, spatial attention and spatial-channel mixed attention. Additionally, we conduct comprehensive ablation studies on our models. Lastly, we evaluate our proposed mechanism against another brain lesion segmentation task, using ultrasound images from the ISLES2018 dataset. Across all of the three different tasks, our models consistently outperform the baseline models in terms of Hausdorff Distance (HD) or/and Intersection Over Union (IoU). For instance, in the second task, the “explicit” implementation of our mechanism reduces the HD of the best baseline by more than 26%, whilst improving the IoU by more than 3%. We believe our proposed attention mechanism can provide safer computer-aided-detection in a wide range of medical applications. The link to our codes on GitHub is hidden to maintain anonymity during the review period."
slides-id: 38933950
channel-id: "paper_164_P4_id_0335"
---
