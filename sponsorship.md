---
layout: default_sparse
title: Sponsors
permalink: /sponsors/
---

<style>

.list-inline-item:not(:last-child) {
  margin-right: 15px;
}

.image-block {
  padding: 35px 0;
  background: #fff;
  width: 300px;
  height: 120px;
  cursor: pointer;
  transition: all .3s ease;
  border: 1px solid transparent;
  margin-bottom: 10px;
}

.image-block img {
  height: 50px;
}

.image-block:hover {
  border: 1px solid #103a6b;
}
</style>

<p class="mb-3" align="center"><strong>We are very grateful to our sponsors for supporting the conference this year:</strong></p>

{% assign grouped_sponsors = site.data.sponsors.sponsors | group_by:"type" %}

<section class="sponsors section ">
{% for group in grouped_sponsors %}
<!--<h3>{{-group.name-}}&nbsp;Sponsor</h3>-->
{% for item in group.items %}
<li class="list-inline-item">
  <div class="col-12 mt-3 mb-3">
    <h3>{{-group.name-}}&nbsp;Sponsor</h3>
  </div>
    <div class="image-block text-center">
        <a href="{{item.url}}" target="_blank" >
            <img src="{{ site.baseurl }}/assets/images/sponsors/{{item.logo}}" alt="sponsors-logo" class="img-fluid" style="max-height: 300px;">
        </a>
    </div>
</li>
{% endfor %}
{% endfor %}
</section>

<br>
<br>
<br>


<center>
    <p>If you are interested in sponsoring BMVC 2023, please email <a href="mailto:sponsors@bmvc2023.org">sponsors@bmvc2023.org</a> 
      for more information. The deadline for expressing interest in sponsoring BMVC is <b>30th Septemeber 2023</b>. Thank you so much!</p>
</center>

<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-center">
    <table class="table table-striped table-bordered" style="max-width: 750px;">
        <tbody>
            <tr>
                <th style="text-align: center">PACKAGE OFFERS</th>
                <th style="text-align: center">PLATINUM £5000</th>
                <th style="text-align: center">GOLD £3000</th>
                <th style="text-align: center">SILVER £2000</th>
                <th style="text-align: center">Welcome Reception Sponsor £9000</th>
            </tr>
            <tr>
                <td>Company logo and link on the conference website</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Company logo on conference programmee</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>1 Free registration</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>1 Exhibition stand</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>1 Additional free registration</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Acknowledgment in the opening address</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>A Young Researcher attendance bursary named after the company</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Company names associated with invited talks, tutorials or prizes</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Exclusive promotion opportunity at the Welcome Reception</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✔</td>
            </tr>
        </tbody>
    </table>
</div>
