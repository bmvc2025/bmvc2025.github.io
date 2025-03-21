---
layout: default_paper
id: 816
order: 92
poster_session: 2
session_id: 5
title: "LaDDer: Latent Data Distribution Modelling with a Generative Prior"
authors:
  - author: "Shuyu Lin (University of Oxford)"
  - author: "Ronald Clark (Imperial College London)"
all_authors: "Shuyu Lin and Ronald Clark"
code: "https://github.com/lin-shuyu/ladder-latent-data-distribution-modelling"
keywords:
  - word: "variational autoencoder"
  - word: "generative model"
  - word: "variational inference"
  - word: "representation learning"
  - word: "unsupervised learning"
  - word: "latent space interpolation"
paper: "papers/0816.pdf"
supp: "supp/0816_supp.pdf"
abstract: "In this paper, we show that the performance of a learnt generative model is closely related to the model's ability to accurately represent the inferred latent data distribution, i.e. its topology and structural properties. We propose LaDDer to achieve accurate modelling of the latent data distribution in a variational autoencoder framework and to facilitate better representation learning. The central idea of LaDDer is a meta-embedding concept, which uses multiple VAE models to learn an embedding of the embeddings, forming a ladder of encodings. We use a non-parametric mixture as the hyper prior for the innermost VAE and learn all the parameters in a unified variational framework. From extensive experiments, we show that our LaDDer model is able to accurately estimate complex latent distribution and results in improvement in the representation quality. We also propose a novel latent space interpolation method that utilises the derived data distribution. The code and demos are available at https://github.com/lin-shuyu/ladder-latent-data-distribution-modelling."
slides-id: 38934037
channel-id: "paper_092_P2_id_0816"
---
