---
layout: default_sparse
title: Sponsors
permalink: /sponsors/
---

<style>
.list-inline-item:not(:last-child) {
  margin-right: 15px;
}

/* .image-block {
  padding: 30px 0;
  background: #fff;
  width: 300px;
  cursor: pointer;
  transition: all .3s ease;
  border: 1px solid transparent;
  margin-bottom: 10px;
} */

/* .image-block img {
  height: 80px;
} */

.image-block {
  padding: 30px 0;
  background: #fff;
  width: 300px;
  height: 100px; /* Fixed height for consistent row */
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all .3s ease;
  border: 1px solid transparent;
  margin-bottom: 10px;
}

.image-block img {
  max-height: 80px;
  max-width: 100%;
  object-fit: contain;
}

.image-block:hover {
  border: 1px solid #103a6b;
}
</style>

<p class="mb-3" align="center"><strong>We are very grateful to our sponsors for supporting the conference this year. We hope to announce more sponsors soon.</strong></p>

{% assign grouped_sponsors = site.data.sponsors.sponsors | group_by:"type" -%}

<section class="sponsors section" align="center">
{% for group in grouped_sponsors %}
    {% if group.name == 'Gold' or group.name == 'Platinum' or group.name == 'Silver'%} 
        <h3 align="left">{{-group.name-}}&nbsp;Sponsors:</h3>
        {% else %}
        <!-- <h3>{{-group.name-}}&nbsp;:</h3> -->
        <h3>{{-group.name-}}:</h3>
    {% endif %}
    {% for item in group.items %}
        <li class="list-inline-item">
            <div class="image-block text-center">
                <a href="{{item.url}}" target="_blank" >
                    <img src="{{ site.baseurl }}/imgs_2025/sponsors_logo/{{ item.logo }}" alt="sponsors-logo" class="img-fluid" style="max-height: 300px;">
                </a>
            </div>
        </li>
    {% endfor %}
{% endfor %}
</section><br>

<div class="align-items-center mb-3">
    <div class="col-xs-12 mx-auto">
        <h2 style="text-align: center;">Sponsoring BMVC</h2>
    </div>
</div>

<div class='text-justify'>
    <!-- <p>If you are interested in sponsoring BMVC 2024, please email <a href="mailto:sponsors@bmvc2024.org">sponsors@bmvc2024.org</a> 
      for more information. The deadline for expressing interest in sponsoring BMVC is <b>30th Septemeber 2024</b>. Thank you so much! -->
    <p>Sponsoring BMVC2025 is the perfect opportunity to showcase your company's excellent work throughout the conference. As a sponsor, you will be provided with an exhibition stand to promote your business and work, and numerous opportunities will be available to engage with academic and industrial researchers in the field to explore potential future collaborations. We are open to customising the sponsorship package to best suit your needs, e.g. an industrial paper track to demonstrate select BMVC papers and an industrial night to socialise and forge new partnerships.</p>
    <p>If you are interested in sponsoring BMVC 2025, please email <a href="mailto:{{ site.email }}"> {{ site.email }}</a>. The deadline for expressing interest in sponsoring BMVC is <b>29 September 2025</b>.</p>
</div>

<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-center">
    <table class="table table-striped table-bordered" style="max-width: 750px;">
        <tbody>
            <tr>
                <th style="text-align: center">PACKAGE OFFERS</th>
                <th style="text-align: center">PLATINUM + Reception Sponsor £9000</th>
                <th style="text-align: center">PLATINUM £5000</th>
                <th style="text-align: center">GOLD £3000</th>
                <th style="text-align: center">SILVER £2000</th>
            </tr>
            <tr>
                <td>Company logo and link on the conference website</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
            </tr>
            <tr>
                <td>Company logo on conference programme</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
            </tr>
            <tr>
                <td>1 Free registration</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
            </tr>
            <tr>
                <td>1 Exhibition stand</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>1 Additional free registration</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Acknowledgment in the opening address</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>A Young Researcher attendance bursary named after the company</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Company names associated with invited talks, tutorials or prizes</td>
                <td align="center">✔</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
            <tr>
                <td>Exclusive promotion opportunity at the Welcome Reception</td>
                <td align="center">✔</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
                <td align="center">✘</td>
            </tr>
        </tbody>
    </table>
</div>
