---
layout: default_paper
id: 796
order: 89
poster_session: 2
session_id: 5
title: "Synchronous Bidirectional Learning for Multilingual Lip Reading"
authors:
  - author: "Mingshuang Luo (Institute of Computing Technology, Chinese Academy of Sciences, University of Chinese Academy of Science)"
  - author: "Shuang Yang (ICT, CAS)"
  - author: "Xilin Chen (Institute of Computing Technology, Chinese Academy of Sciences)"
  - author: "Zitao Liu (TAL AI Lab)"
  - author: "Shiguang Shan (Institute of Computing Technology, Chinese Academy of Sciences)"
all_authors: "Mingshuang Luo, Shuang Yang, Xilin Chen, Zitao Liu and Shiguang Shan"
code: ""
keywords:
  - word: "lip reading"
  - word: "multilingual"
  - word: "synchronous bidirectional learning"
  - word: "transformer"
paper: "papers/0796.pdf"
supp: ""
abstract: "Lip reading has received increasing attention in recent years. This paper focuses on the synergy of multilingual lip reading. There are about as many as 7,000 languages in the world, which implies that it is impractical to train separate lip reading models with large-scale data for each language. Although each language has its own linguistic and pronunciation rules, the lip movements of all languages share similar patterns due to the common structures of human organs. Based on this idea,  we try to explore the synergized learning of multilingual lip reading in this paper, and further propose a synchronous bidirectional learning (SBL) framework for effective synergy of multilingual lip reading. We firstly introduce phonemes as our modeling units for the multilingual setting here. Phonemes are more closely related with the lip movements than the alphabet letters. At the same time, similar phonemes always lead to similar visual patterns no matter which type the target language is. Then, a novel SBL block is proposed to learn the rules for each language in a fill-in-the-blank way. Specifically, the model has to learn to infer the target unit given its bidirectional context, which could represent the composition rules of phonemes for each language. To make the learning process more targeted at each particular language, an extra task of predicting the language identity is introduced in the learning process. Finally, a thorough comparison on LRW (English) and LRW-1000 (Mandarin) is performed, which shows the promising benefits from the synergized learning of different languages and also reports a new state-of-the-art result on both datasets."
slides-id: 38934034
channel-id: "paper_089_P2_id_0796"
---
