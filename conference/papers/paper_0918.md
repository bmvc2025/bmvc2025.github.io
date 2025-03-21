---
layout: default_paper
id: 918
order: 184
poster_session: 4
session_id: 11
title: "POMP: Pomcp-based Online Motion Planning for active visual search in indoor environments"
authors:
  - author: "Yiming Wang (IIT)"
  - author: "Francesco  Giuliari (University of Verona)"
  - author: "Riccardo Berra (University of Verona)"
  - author: "Alberto Castellini (University of Verona)"
  - author: "Alessio Del Bue (Istituto Italiano di Tecnologia (IIT))"
  - author: "Alessandro Farinelli (University of Verona, Italy)"
  - author: "Marco Cristani (University of Verona)"
  - author: "Francesco Setti (University of Verona)"
all_authors: "Yiming Wang, Francesco  Giuliari, Riccardo Berra, Alberto Castellini, Alessio Del Bue, Alessandro Farinelli, Marco Cristani and Francesco Setti"
code: ""
keywords:
  - word: "Object Recognition Active Visual Search Partially Observable Markov Decision Process Monte Carlo Tree Search"
paper: "papers/0918.pdf"
supp: ""
abstract: "In this paper we focus on the problem of learning an optimal policy for Active Visual Search (AVS) of objects in known indoor environments with an online setup. Our POMP method uses as input the current pose of an agent (e.g. a robot) and a RGB-D frame. The task is to plan the next move that brings the agent closer to the target object. We model this problem as a Partially Observable Markov Decision Process solved by a Monte-Carlo planning approach. This allows us to make decisions on the next moves by iterating over the known scenario at hand, exploring the environment and searching for the object at the same time.  Differently from the current state of the art in Reinforcement Learning, POMP does not require extensive and expensive (in time and computation) labelled data so being very agile in solving AVS in small and medium real scenarios. We only require the information of the floormap of the environment, an information usually available or that can be easily extracted from an a priori single exploration run. We validate our method on the publicly available AVD benchmark, achieving an average success rate of 0.76 with an average path length of 17.1, performing close to the state of the art but without any training needed. Additionally, we show experimentally the robustness of our method when the quality of the object detection goes from ideal to faulty."
slides-id: 38934051
channel-id: "paper_184_P4_id_0918"
---
