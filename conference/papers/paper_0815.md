---
layout: default_paper
id: 815
order: 13
poster_session: 1
session_id: 2
title: "Text and Style Conditioned GAN for the Generation of Offline-Handwriting Lines"
authors:
  - author: "Brian Davis (Brigham Young University)"
  - author: "Bryan Morse (-)"
  - author: "Brian Price (Adobe)"
  - author: "Chris Tensmeyer (Adobe Research)"
  - author: "Curtis Wigington (Adobe Research)"
  - author: "Rajiv Jain (Adobe Research)"
all_authors: "Brian Davis, Bryan Morse, Brian Price, Chris Tensmeyer, Curtis Wigington and Rajiv Jain"
code: ""
keywords:
  - word: "handwriting generation"
  - word: "conditional GAN"
  - word: "conditional image generation"
  - word: "few-shot image generation"
  - word: "handwriting recognition"
paper: "papers/0815.pdf"
supp: "supp/0815_supp.pdf"
abstract: "This paper presents a GAN for generating images of handwritten lines 
conditioned on arbitrary text and latent style vectors. Unlike prior work, which produce stroke points or single-word images, this model generates entire lines of offline handwriting. The model produces variable-sized images by using style vectors to determine character widths. A generator network is trained with GAN and autoencoder techniques to learn style, and uses a pre-trained handwriting recognition network to induce legibility. A study using human evaluators demonstrates that the model produces images that appear to be written by a human. After training, the encoder network can extract a style vector from an image, allowing images in a similar style to be generated, but with arbitrary text."
slides-id: 38934036
channel-id: "paper_013_P1_id_0815"
---
