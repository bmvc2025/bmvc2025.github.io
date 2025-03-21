---
layout: default_paper
id: 549
order: 110
poster_session: 3
session_id: 8
title: "Tripping through time: Efficient Localization of Activities in Videos"
authors:
  - author: "Meera Hahn (Georgia Institute of Technology)"
  - author: "Asim Kadav (NEC Labs)"
  - author: "James Rehg (Georgia Institute of Technology)"
  - author: "Hans Peter Graf (NEC Labs)"
all_authors: "Meera Hahn, Asim Kadav, James Rehg and Hans Peter Graf"
code: ""
keywords:
  - word: "Activity Localization"
  - word: "Reinforcement learning"
  - word: "Vision and Language"
paper: "papers/0549.pdf"
supp: "supp/0549_supp.pdf"
abstract: "Localizing moments in untrimmed videos via language queries is a new and interesting task that requires the ability to accurately ground language into video. Previous works have approached this task by processing the entire video, often more than once, to localize relevant activities. In the real world applications that this task lends itself to, such as surveillance, efficiency is a pivotal trait of a system. In this paper, we present TripNet, an end-to-end system that uses a gated attention architecture to model fine-grained textual and visual representations in order to align text and video content. Furthermore, TripNet uses reinforcement learning to efficiently localize relevant activity clips in long videos, by learning how to intelligently skip around the video. It extracts visual features for few frames to perform activity classification. In our evaluation over Charades-STA, ActivityNet Captions and the TACoS dataset, we find that TripNet achieves high accuracy and saves process- ing time by only looking at 32-41% of the entire video. "
slides-id: 38933997
channel-id: "paper_110_P3_id_0549"
---
