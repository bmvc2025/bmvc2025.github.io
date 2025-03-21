---
layout: default_paper
id: 149
order: 88
poster_session: 2
session_id: 5
title: "Inducing Predictive Uncertainty Estimation for Face Verification"
authors:
  - author: "Weidi Xie (University of Oxford)"
  - author: "Jeffrey Byrne (STR"
  - author: "Visym Labs)"
  - author: "Andrew Zisserman (University of Oxford)"
all_authors: "Weidi Xie, Jeffrey Byrne (STR, Visym Labs) and Andrew Zisserman"
code: ""
keywords:
  - word: "Face Recognition"
  - word: "Quality Estimation"
  - word: "Uncertainty Estimation"
  - word: "Explainable AI"
paper: "papers/0149.pdf"
supp: ""
abstract: "
Knowing when an output can be trusted is critical for reliably using face recognition systems. While there has been enormous effort in recent research on improving face verification performance, understanding when a model's predictions should or should not be trusted has received far less attention. 

Our goal is a method can predict a confidence score for a face image that reflects
its quality in terms of recognizable information.
To this end, we propose a method for generating image quality training data
automatically from `mated-pairs' of face images, and use the generated data to train a lightweight Predictive Confidence Network, termed as PCNet, 
for estimating the confidence score of a face image.
We systematically evaluate the usefulness of PCNet using its error versus reject performance, 
and demonstrate that it can be universally paired with and improve the robustness of any verification model.  
We describe three use cases on the public IJB-C face verification benchmark: 
(i) to  improve 1:1 image-based verification error rates by rejecting low-quality face
images; 
(ii) to improve quality score based fusion performance on the 1:1 set-based
verification benchmark; 
and (iii) its use as a quality measure for selecting high quality (unblurred, good lighting, 
more frontal) faces from a collection, e.g. for automatic enrolment or display."
slides-id: 38933902
channel-id: "paper_088_P2_id_0149"
---
