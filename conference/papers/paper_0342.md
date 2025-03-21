---
layout: default_paper
id: 342
order: 174
poster_session: 4
session_id: 11
title: "Neighbours Matter: Image Captioning with Similar Images"
authors:
  - author: "Qingzhong Wang (Department of Computer Science, City University of Hong Kong)"
  - author: "Jiuniu Wang (City University of Hong Kong)"
  - author: "Antoni Chan (City University of Hong Kong, Hong, Kong)"
  - author: "Siyu Huang (Baidu Research)"
  - author: "Haoyi Xiong (Baidu Research)"
  - author: "Xingjian Li (Baidu Research)"
  - author: "Dejing Dou (Baidu)"
all_authors: "Qingzhong Wang, Jiuniu Wang, Antoni Chan, Siyu Huang, Haoyi Xiong, Xingjian Li and Dejing Dou"
code: ""
keywords:
  - word: "Image captioning"
  - word: "graph neural networks"
  - word: "attention mechanism"
paper: "papers/0342.pdf"
supp: ""
abstract: "Most image captioning models aim to generate captions based solely on the input image.  However images that are similar to the given input image  contain variations of the same or similar concepts as the input image. Thus, aggregating information over similar images could be used to improve image captioning models, by strengthening or inferring concepts that are in the input image. In this paper, we propose an image captioning model based on KNN graphs composed of the input image and its similar images, where each node denotes an image or a caption.  An attention-in-attention (AiA)  model is developed to refine the node representations. Using the refined features significantly improves the baseline performance, eg, CIDEr score obtained by Updown model increases from 120.1 to 125.6. Compared with the state-of-the-art performance, our proposed method obtains 129.3 of CIDEr and 22.6 of SPICE on Karpathy's test split, which is competitive with the models that employ fine-grained image features such as scene graphs and image parsing trees."
slides-id: 38933951
channel-id: "paper_174_P4_id_0342"
---
