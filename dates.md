---
layout: date_sparse
title: Dates
permalink: /dates/
---

<p align="center"><strong>
    Please note all deadlines are at 23:59 UK Time.
</strong></p>


<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-center">
<table class="table table-striped table-bordered" style="max-width: 750px;">
  <tbody>
    <tr><th scope="row">Subject</th>
        <th scope="row">Date (all deadlines {{site.deadline-time}})</th></tr>
    {% for item in site.data.timeline.deadlines %}
        <tr>
          {% if item.title == 'Workshop Submission Deadline' or item.title == 'Paper Submission Deadline' or item.title == 'Supplementary Material Submission' or item.title == 'Workshop Acceptance Notification' or item.title == 'Review Period Starts' or item.title == 'Reviews Submitted' or item.title == 'Doctoral Consortium Submission Deadline' or item.title == 'Start of Rebuttal Period' or item.title == 'End of Rebuttal Period' or item.title == 'Reviewer Discussion & Final Revs' or item.title == 'Meta-Reviews Submitted' or item.title == 'Paper Decisions & Meta-Rev Consolidation' or item.title == 'Author Notifications' or item.title == 'Camera Ready' or item.title == 'Camera Ready for Workshops' or item.title == 'Poster Submissions' or item.title == 'Video Submissions'%} 
            <td><s>{{item.title}}</s>&nbsp;
                {% for tag in item.tags %}
                {% case tag.key %}
                  {% when "Authors" %}
                     {% assign badge-color = "badge-success" %}
                  {% when "Reviewers" %}
                     {% assign badge-color = "badge-primary" %}
                  {% when "AC" %}
                     {% assign badge-color = "badge-info" %}
                  {% when "AC Buddies" %}
                     {% assign badge-color = "badge-info" %}
                  {% when "Everyone" %}
                     {% assign badge-color = "badge-dark" %}
                  {% else %}
                     {% assign badge-color = "badge-secondary" %}
                {% endcase %}
                  <span class="badge {{badge-color}} mt-2 mb-2" style="font-weight: normal;">{{ tag.key }}</span>
                {% endfor %}
            </td>                
            <td><s>{{item.date | date: '%A, %e %B %Y'}}</s></td>
          {% else %}
            <td>{{item.title}}&nbsp;
                {% for tag in item.tags %}
                {% case tag.key %}
                  {% when "Authors" %}
                     {% assign badge-color = "badge-success" %}
                  {% when "Reviewers" %}
                     {% assign badge-color = "badge-primary" %}
                  {% when "AC" %}
                     {% assign badge-color = "badge-info" %}
                  {% when "AC Buddies" %}
                     {% assign badge-color = "badge-info" %}
                  {% when "Everyone" %}
                     {% assign badge-color = "badge-dark" %}
                  {% else %}
                     {% assign badge-color = "badge-secondary" %}
                {% endcase %}
                  <span class="badge {{badge-color}} mt-2 mb-2" style="font-weight: normal;">{{ tag.key }}</span>
                {% endfor %}
            </td>
            <td>{{item.date | date: '%A, %e %B %Y'}}</td>
          {% endif %}
            
        </tr>
    {% endfor %}
  </tbody>
</table>
</div>

{% comment %}

<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-center">
<table class="table table-striped table-bordered" style="max-width: 750px;">
  <!--<thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>-->
  <tbody>
    <tr><th scope="row">Deadline</th>
        <th scope="row">Date (all deadlines {{site.deadline-time}})</th></tr>

            <tr>
                <td>Paper Abstracts</td>
                <td>Friday 18th June 2021</td>
            </tr>
            <tr>
                <td>Paper Submission</td>
                <td>Friday 25th June 2021</td>
            </tr>
            <tr>
                <td>Paper Submission</td>
                <td>Friday 25th June 2021</td>
            </tr>
            <tr>
                <td><strong>Virtual Conference</strong></td>
                <td><strong>Monday 22nd &#8211; Thursday 25th November 2021</strong></td>
            </tr>
        </tbody>
    </table>
</div>

<!--<tr>
    <td>Reviews Submitted</td>
    <td>Thursday 18th June 2020</td>
</tr>
<tr>
    <td>Reviews to Authors,<br>Start of Rebuttal Period</td>
    <td>Friday 26th June 2020</td>
</tr>
<tr>
    <td>Author Rebuttals Submitted</td>
    <td>Thursday 2nd July 2020</td>
</tr>
<tr>
    <td>Area Chair Decisions</td>
    <td>Thursday 23rd July 2020</td>
</tr>
<tr>
    <td>Author Notification</td>
    <td>Wednesday 29th July 2020</td>
</tr>
<tr>
    <td>Camera Ready Submission (PDF and Supplementary Material)</td>
    <td>Thursday 13th August 2020</td>
</tr>
<tr>
    <td>Virtual Conference Video Submissions</td>
    <td>Thursday 20th August 2020</td>
</tr>
<tr>
    <td>Deadline for payment of per paper event enabling fee</td>
    <td>Thursday 27th August 2020</td>
</tr>-->

{% endcomment %}
