---
layout: default_paper
id: 243
order: 16
poster_session: 1
session_id: 2
title: "Annealing Genetic GAN for Minority Oversampling"
authors:
  - author: "Jingyu Hao (Sun Yat-sen University)"
  - author: "Chengjia Wang (University of Edinburgh)"
  - author: "Heye Zhang (Sun Yat-sen University )"
  - author: "Guang Yang (Imperial College London)"
all_authors: "Jingyu Hao, Chengjia Wang, Heye Zhang and Guang Yang"
code: "https://github.com/Heye-SYSU/AGGAN"
keywords:
  - word: "annealing genetic algorithm"
  - word: "generative adversarial networks"
  - word: "class imbalance problem"
  - word: "mode collapse"
paper: "papers/0243.pdf"
supp: ""
abstract: "The key to overcome class imbalance problems is to capture the distribution of minority class accurately. Generative Adversarial Networks (GANs) have shown some potentials to tackle class imbalance problems due to their capability of reproducing data distributions given ample training data samples. However, the scarce samples of one or more classes still pose a great challenge for GANs to learn accurate distributions for the minority classes. In this work, we propose an Annealing Genetic GAN (AGGAN) method, which aims to reproduce the distributions closest to the ones of the minority classes using only limited data samples. Our AGGAN renovates the training of GANs as an evolutionary process that incorporates the mechanism of simulated annealing. In particular, the generator uses different training strategies to generate multiple offspring and retain the best. Then, we use the Metropolis criterion in the simulated annealing to decide whether we should update the best offspring for the generator. As the Metropolis criterion allows a certain chance to accept the worse solutions, it enables our AGGAN steering away from the local optimum. According to both theoretical analysis and experimental studies on multiple imbalanced image datasets, we prove that the proposed training strategy can enable our AGGAN to reproduce the distributions of minority classes from scarce samples and provide an effective and robust solution for the class imbalance problem."
slides-id: 38933930
channel-id: "paper_016_P1_id_0243"
---
