---
layout: default_paper
id: 512
order: 161
poster_session: 4
session_id: 11
title: "Real-time screen reading: reducing domain shift for one-shot learning"
authors:
  - author: "James Charles (Cambridge University)"
  - author: "Stefano Bucciarelli (Cambridge University)"
  - author: "Roberto Cipolla (University of Cambridge)"
all_authors: "James Charles, Stefano Bucciarelli and Roberto Cipolla"
code: ""
keywords:
  - word: "one shot learning"
  - word: "domain adaptation"
  - word: "domain transfer"
  - word: "domain shift"
  - word: "text recognition"
  - word: "word spotting"
  - word: "meter reading"
  - word: ""
paper: "papers/0512.pdf"
supp: "supp/0512_supp.pdf"
supp2: "supp/0512_supp2.mp4"
abstract: "Many digital meters such as those used for home health (e.g. blood pressure meters) or meters monitoring industrial equipment do not contain wireless connectivity. Hence, connecting these devices to phone tracking apps or control centres either requires cumbersome manual transcription or is not plausible due to costs. Our motivation is to cheaply retro-fit these types of meters with `smart' data transfer capabilities using a mobile phone app and limited training data. We demonstrate how one can use single training images of meter screens to build efficient custom meter readers targeted to chosen devices. To this end, we build a CNN based system which runs in real-time on mobile device with very high read accuracy (close to 100%). Our contributions include (i) introduction of an exciting new application domain, (ii) a method of training from purely synthetic data by reducing domain shift using a surprisingly simple approach which unlike adversarial training based methods does not even require unlabelled data; (iii) a highly accurate system for parsing digital meter screens and (iv) release of a new screen reading dataset. 
The system, although trained solely on synthetic data, transfers very well to the real-world. Our method of screen detection and text recognition also improves over the state of the art on our dataset."
slides-id: 38933988
channel-id: "paper_161_P4_id_0512"
---
