---
layout: default_paper
id: 213
order: 79
poster_session: 2
session_id: 5
title: "Branched Multi-Task Networks: Deciding what layers to share"
authors:
  - author: "Simon Vandenhende (KU Leuven)"
  - author: "Stamatios Georgoulis (ETH Zurich)"
  - author: "Luc Van Gool (ETH Zurich)"
  - author: "Bert De Brabandere (KU Leuven)"
all_authors: "Simon Vandenhende, Stamatios Georgoulis, Luc Van Gool and Bert De Brabandere"
code: ""
keywords:
  - word: "multi-task learning"
  - word: "neural architecture search"
  - word: "scene understanding"
  - word: "MTL"
  - word: "efficient"
  - word: "NAS"
  - word: "transfer learning"
  - word: "taskonomy"
  - word: "task affinity"
paper: "papers/0213.pdf"
supp: "supp/0213_supp.zip"
abstract: "In the context of multi-task learning, neural networks with branched architectures have often been employed to jointly tackle the tasks at hand. Such ramified networks typically start with a number of shared layers, after which different tasks branch out into their own sequence of layers. Understandably, as the number of possible network configurations is combinatorially large, deciding what layers to share and where to branch out becomes cumbersome. Prior works have either relied on ad hoc methods to determine the level of layer sharing, which is suboptimal, or utilized neural architecture search techniques to establish the network design, which is considerably expensive. In this paper, we go beyond these limitations and propose an approach to automatically construct branched multi-task networks, by leveraging the employed tasks' affinities. Given a specific budget, i.e. number of learnable parameters, the proposed approach generates architectures, in which shallow layers are task-agnostic, whereas deeper ones gradually grow more task-specific. Extensive experimental analysis across numerous, diverse multi-tasking datasets shows that, for a given budget, our method consistently yields networks with the highest performance, while for a certain performance threshold it requires the least amount of learnable parameters."
slides-id: 38933920
channel-id: "paper_079_P2_id_0213"
---
