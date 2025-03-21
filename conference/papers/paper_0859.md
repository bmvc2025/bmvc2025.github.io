---
layout: default_paper
id: 859
order: 145
poster_session: 3
session_id: 8
title: "Adversarial Concurrent Training: Optimizing Robustness and Accuracy Trade-off of Deep Neural Networks"
authors:
  - author: "Elahe Arani (Navinfo Europe )"
  - author: "Fahad Sarfraz (Navinfo Europe)"
  - author: "Bahram Zonooz (Navinfo Europe)"
all_authors: "Elahe Arani, Fahad Sarfraz and Bahram Zonooz"
code: ""
keywords:
  - word: "Adversarial Robustness"
  - word: "Generalization"
  - word: "Adversarial Training"
  - word: "Deep Learning"
  - word: "Collaborative Learning"
paper: "papers/0859.pdf"
supp: ""
abstract: "Adversarial training has been proven to be an effective technique for improving the adversarial robustness of models.  However, there seems to be an inherent trade-off be-tween optimizing the model for accuracy and robustness. To this end, we propose Adversarial Concurrent Training (ACT), which employs adversarial training in a collaborative learning framework whereby we train a robust model in conjunction with a natural model in a minimax game. ACT encourages the two models to align their feature space by using the task-specific decision boundaries and explore the input space more broadly. Furthermore, the natural model acts as a regularizer, enforcing priors on features that the robust model should learn.  Our analyses on the behavior of the models show that ACT leads to a robust model with lower model complexity, higher information compression in the learned representations, and high posterior entropy solutions indicative of convergence to a flatter minima.  We demonstrate the effectiveness of the proposed approach across different datasets and network architectures. On ImageNet, ACT achieves 68.20% standard accuracy and 44.29% robustness accuracy under a 100-iteration untargeted attack, improving upon the standard adversarial training method’s 65.70% standard accuracy and 42.36% robustness."
slides-id: 38934040
channel-id: "paper_145_P3_id_0859"
---
