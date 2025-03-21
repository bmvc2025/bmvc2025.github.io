---
layout: default_paper
id: 14
order: 157
poster_session: 4
session_id: 11
title: "Localizing Novel Attended Objects in Egocentric Views"
authors:
  - author: "Shujon Naha (Indiana University)"
  - author: "Md Reza (Indiana University)"
  - author: "Chen Yu (Indiana University)"
  - author: "David Crandall (Indiana University)"
all_authors: "Shujon Naha, Md Reza, Chen Yu and David Crandall"
code: ""
keywords:
  - word: "attended object localization"
  - word: "weakly supervised localization"
  - word: "generalized object localization"
  - word: "egocentric view understanding"
  - word: "knowledge distillation"
  - word: "feature disentanglement"
paper: "papers/0014.pdf"
supp: ""
abstract: "People have foveated vision and thus are generally able to attend to just a single object within their field of view at a time. Our goal is to learn a model that can automatically identify which object is being attended, given a person’s field of view captured by a first person camera. This problem is different from traditional salient object detection because our goal is not to identify all of the salient objects in the scene, but to identify the single object to which the camera wearer is attending. We present a model that learns based on very weak supervision, with just annotations of the label of the class that is attended in each frame, without bounding boxes or other spatial location information. We show that by learning disentangled representations for localization and classification, our model can effectively localize novel attended objects that were never seen during training. We propose a multi-stage knowledge distillation strategy to train our generalized localizer model.  To the best of our knowledge, our work is the first to explore the problem of learning generalized attended object localization models in egocentric views under weak supervision."
slides-id: 38933865
channel-id: "paper_157_P4_id_0014"
---
