---
layout: default_paper
id: 744
order: 179
poster_session: 4
session_id: 11
title: "HASTE: multi-Hypothesis Asynchronous Speeded-up Tracking of Events"
authors:
  - author: "Ignacio Alzugaray (ETH Zurich)"
  - author: "Margarita Chli (ETH Zurich)"
all_authors: "Ignacio Alzugaray and Margarita Chli"
code: ""
keywords:
  - word: "event camera"
  - word: "event-driven"
  - word: "feature tracking"
  - word: "multi-hypothesis tracking"
  - word: "dynamic vision sensor"
  - word: "asynchronous optimization"
  - word: ""
paper: "papers/0744.pdf"
supp: "supp/0744_supp.zip"
abstract: "Feature tracking using event cameras has experienced significant progress lately, with methods achieving comparable performance to feature trackers using traditional frame-based cameras, even outperforming them on certain challenging scenarios. Most of the event-based trackers, however, still operate on intermediate, frame-like representations generated from accumulated events, on which traditional frame-based techniques can be adopted. Attempting to harness the sparsity and asynchronicity of the event stream, other approaches have emerged to process each event individually, but they lack both in accuracy and efficiency in comparison to the event-based, frame-like alternatives.

Aiming to address this shortcoming of asynchronous approaches, in this paper, we propose an asynchronous patch-feature tracker that relies solely on events and processes each event individually as soon as it gets generated. We report significant improvements in tracking quality over the state of the art in publicly available datasets, while performing an order of magnitude more efficiently than similar asynchronous tracking approaches."
slides-id: 38934026
channel-id: "paper_179_P4_id_0744"
---
