---
layout: default_paper
id: 688
order: 106
oral_session: 6
poster_session: 3
session_id: 7
title: "Marginalized Graph Attention Hashing for Zero-Shot Image Retrieval"
authors:
  - author: "Meixue Huang (Institute of Information Engineering, Chinese Academy of Sciences)"
  - author: "Dayan Wu (Institute of Information Engineering, Chinese Academy of Sciences)"
  - author: "Wanqian Zhang (Institute of Information Engineering, Chinese Academy of Sciences)"
  - author: "Zhi Xiong (Institute of Information Engineering, Chinese Academy of Sciences)"
  - author: "Bo Li (	Institute of Information Engineering, Chinese Academy of Sciences)"
  - author: "Weiping Wang (Institute of Information Engineering, CAS, China)"
all_authors: "Meixue Huang, Dayan Wu, Wanqian Zhang, Zhi Xiong, Bo Li and Weiping Wang"
code: ""
keywords:
  - word: "zero-shot hashing"
  - word: "image retrieval"
  - word: "attention mechanism"
  - word: "marginalized strategy"
paper: "papers/0688.pdf"
supp: ""
abstract: "Zero-shot image retrieval allows to precisely retrieve candidates relevant to unobserved queries, of which categories have never been seen during training. Recently, research interests arise in exploring hashing methods to solve this problem due to its storage and computational efficiency. However, existing methods only focus on leveraging semantic information, but omit to exploit the similarity structure of visual feature space for knowledge transfer. Besides, the domain shift problem across seen and unseen classes further degrades the performance. To tackle these issues, in this paper, we propose a novel deep zero-shot hashing method, named Marginalized Graph Attention Hashing (MGAH). MGAH introduces the masked attention mechanism to construct a joint-semantics similarity graph, which captures the intrinsic relationship from different metric spaces, making it competent to transfer knowledge from seen classes into unseen classes. Furthermore, we elaborately design an Energy Magnified Softmax (EM-Softmax) loss, which is capable to alleviate the domain shift problem and encourage the generalization ability of hash codes. By using marginalized strategy, EM-Softmax produces the shared decision margin for hard samples, thus can avoid overfitting on seen classes and meanwhile cover more knowledge for the unseen ones. Extensive experiments demonstrate that MGAH delivers superior performance over the state-of-the-art zero-shot hashing methods.
"
slides-id: 38934017
channel-id: "paper_106_P3_id_0688"
---
