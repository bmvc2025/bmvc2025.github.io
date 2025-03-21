---
layout: default_paper
id: 711
order: 151
oral_session: 7
poster_session: 4
session_id: 9
title: "SketchHealer: A Graph-to-Sequence Network for Recreating Partial Human Sketches"
authors:
  - author: "Guoyao Su (Beijing University of Posts and Telecommunications)"
  - author: "Yonggang Qi (Beijing University of Posts and Telecommunications)"
  - author: "Kaiyue Pang (Queen Mary University of London)"
  - author: "Jie Yang (BUPT)"
  - author: "Yi-Zhe Song (University of Surrey)"
all_authors: "Guoyao Su, Yonggang Qi, Kaiyue Pang, Jie Yang and Yi-Zhe Song"
code: "https://github.com/sgybupt/SketchHealer"
keywords:
  - word: "sketch healing"
  - word: "sketch synthesis"
  - word: "graph-to-sequence network"
  - word: "GCN"
  - word: ""
paper: "papers/0711.pdf"
supp: ""
abstract: "To perceive and create a whole from parts is a prime trait of the human visual system. In this paper, we teach machines to perform a similar task by recreating a vectorised human sketch from its incomplete parts. This is fundamentally different to prior work on image completion (i) sketches exhibit a severe lack of visual cue and are of a sequential nature, and more importantly (ii) we ask for an agent that does not just fill in a missing part, but to recreate a novel sketch that closely resembles the partial input from scratch. Central to our contribution is a graph model that encodes both the visual and structural features over multiple categories. A novel sketch graph construction module is proposed that leverages the sequential nature of sketches to associate key parts centred around stroke junctions. The intuition is then that message passing within the said graph will naturally provide the healing power when it comes to missing parts (nodes). Finally, an off-the-shelf LSTM-based decoder is employed to decode sketches in a vectorised fashion. Both qualitative and quantitative results show that the proposed model significantly outperforms state-of-the-art alternatives."
slides-id: 38934021
channel-id: "paper_151_P4_id_0711"
---
