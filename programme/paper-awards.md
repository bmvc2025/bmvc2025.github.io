---
layout: default_sparse
title: Paper Awards
permalink: /programme/paper-awards/
index: 25
---

We are delighted to announce the following paper awards. Papers were nominated by (non-conflicted) area chairs and programme chairs to create a shortlist. This shortlist was then sent to an independent awards committee who made the final recommendations.

<h3 class="mt-3 mb-2">Best Paper Award</h3>

<p class="pb-3"><strong><a href="https://bmvc2022.mpi-inf.mpg.de/470">Trans2k: Unlocking the Power of Deep Models for Transparent Object Tracking</a></strong><br>Alan Lukezic (University of Ljubljana); Žiga Trojer (University of Ljubljana); Jiri Matas (Czech Technical University, Prague); Matej Kristan (University of Ljubljana)<br>
</p>

<h3 class="mt-3 mb-2">Best Paper Award Honourable Mention</h3>

<p class="pb-3"><strong><a href="https://bmvc2022.mpi-inf.mpg.de/708">VoRF: Volumetric Relightable Faces</a></strong><br>Pramod Rao (Max Planck Institute for Informatics); Mallikarjun B R (Max Planck Institute for Informatics); Gereon Fox (Max Planck Institute for Informatics); Tim Weyrich (Friedrich-Alexander Universität Erlangen-Nürnberg); Bernd Bickel (IST Austria); Hanspeter Pfister (Harvard University); Wojciech Matusik (MIT); Ayush Tewari (MIT); Christian Theobalt (Max Planck Institute for Informatics); Mohamed Elgharib (Max Planck Institute for Informatics)<br>
</p>

<h3 class="mt-3 mb-2">Best Student Paper Award</h3>

<p class="pb-3"><strong><a href="https://bmvc2022.mpi-inf.mpg.de/78">Event-based Non-Rigid Reconstruction from Contours</a></strong><br>Yuxuan Xue (Max Planck Institute for Intelligent Systems); Haolong Li (Max Planck Institute for Intelligent Systems); Stefan Leutenegger (TU Munich); Joerg Stueckler (Max Planck Institute for Intelligent Systems)<br>
</p>

<p class="pb-3"><strong><a href="https://bmvc2022.mpi-inf.mpg.de/227">In the Eye of Transformer: Global-Local Correlation for Egocentric Gaze Estimation</a></strong><br>Bolin Lai (Georgia Institute of Technology); Miao Liu (Georgia Institute of Technology); Fiona Ryan (Georgia Institute of Technology); James Rehg
(Georgia Institute of Technology)<br>
</p>

<h3 class="mt-3 mb-2">Best Student Paper Award Honourable Mention</h3>

<p class="pb-3"><strong><a href="https://bmvc2022.mpi-inf.mpg.de/893">Copy-Pasting Coherent Depth Regions Improves Contrastive Learning for Urban-Scene Segmentation</a></strong><br>Liang Zeng (Delft University of Technology); Attila Lengyel (Delft University of Technology); Nergis Tomen (Delft University of Technology); Jan C van Gemert (Delft University of Technology)<br>
</p>



### Sponsors

<p class="mb-3" align="center"><strong>We are very grateful to our sponsors for supporting the conference and awards this year:</strong></p>

{% assign grouped_sponsors = site.data.sponsors.sponsors | group_by:"type" %}
<!--<div class="container mb-3">-->
{% for group in grouped_sponsors %}
<div class="row mt-1 mb-1 justify-content-around align-items-center">
{% for item in group.items %}
  <div class="col mb-1 text-center">
    <a href="{{item.url}}"><img src="{{ site.baseurl }}/assets/images/sponsors/{{item.logo}}" class="img-fluid" alt="{{ item.id }}" style="max-height: 100px;"></a>
  </div>
{% endfor %}
</div>
{% endfor %}
<!--</div>-->

