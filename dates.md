---
layout: date_sparse
title: Dates
permalink: /dates/
---

<p align="center"><strong>
    Please note all deadlines are at {{ site.deadline-time }}.
</strong></p>

<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-center">
<table class="table table-striped table-bordered" style="max-width: 750px;">
  <tbody>
    <tr>
      <th scope="row">Subject</th>
      <th scope="row">Date (all deadlines {{site.deadline-time}})</th>
    </tr>
    {% for item in site.data.timeline.deadlines %}
    <tr>
      {% if item.title == 'Abstract Submission Deadline' or item.title == 'Workshop Submission Deadline' or item.title == 'Paper Submission Deadline' or item.title == 'Supplementary Material Submission'  or item.title == 'Review Period Starts' or item.title == 'Workshop Acceptance Notification' or item.title == 'Reviews Submitted' or item.title == 'Start of AC/reviewer Discussion Period' or item.title == 'End of AC/reviewer Discussion Period' or item.title == 'Reviewer Final Reviews' or item.title == 'Meta-Reviews Submitted' or item.title == 'Doctoral Consortium Submission Open' or item.title == 'Paper Decisions & Meta-Review Consolidation' or item.title == 'Author Notifications' or item.title == 'Doctoral Consortium Submission Close' or item.title == 'Camera Ready for Papers' or item.title == 'Doctoral Consortium Acceptance Notification'%}
      <td><del>{{ item.title }}</del>&nbsp;
          {% for tag in item.tags %}
            {% case tag.key %}
              {% when "Authors" %}
                  {% assign badge-color = "badge-success" %}
              {% when "Reviewers" %}
                  {% assign badge-color = "badge-primary" %}
              {% when "ACs" %}
                  {% assign badge-color = "badge-info" %}
              {% when "PCs" %}
                  {% assign badge-color = "badge-secondary" %}
              {% when "Everyone" %}
                  {% assign badge-color = "badge-dark" %}
              {% else %}
                  {% assign badge-color = "badge-secondary" %}
            {% endcase %}
            <span class="badge {{badge-color}} mt-2 mb-2" style="font-weight: normal;">{{ tag.key }}</span>
          {% endfor %}
      </td>
      <td>{{item.date | date: '%A, %e %B %Y'}}</td>
      {% else %}
      <td>{{item.title}}&nbsp;
        {% for tag in item.tags %}
          {% case tag.key %}
            {% when "Authors" %}
                {% assign badge-color = "badge-success" %}
            {% when "Reviewers" %}
                {% assign badge-color = "badge-primary" %}
            {% when "ACs" %}
                {% assign badge-color = "badge-info" %}
            {% when "PCs" %}
                {% assign badge-color = "badge-secondary" %}
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


<!-- 
or item.title == 'Reviewer Final Reviews' 
or item.title == 'Meta-Reviews Submitted' 
or item.title == 'Paper Decisions & Meta-Review Consolidation' 
or item.title == 'Doctoral Consortium Submission Open' 
or item.title == 'Author Notifications' 
or item.title == 'Doctoral Consortium Submission Close' 
or item.title == 'Camera Ready for Papers'       
or item.title == 'Doctoral Consortium Acceptance Notification' 
or item.title == 'Camera Ready for Workshops' 
or item.title == 'Poster Submissions' 
or item.title == 'Video Submissions' 
or item.title == 'Conference Starts' 
or item.title == 'Conference Ends' 
-->