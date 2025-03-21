---
layout: default_miniconf
title: Keynote Archive
permalink: /conference/keynotes/
index: 9
---

<!--
<div class="container mb-3 pb-3">
	<div class="tabs">

		<ul class="nav nav-pills justify-content-center">
			<li class="nav-item">
				<a class="nav-link text-muted" href="{{site.baseurl}}/conference/schedule/">Schedule</a>
			</li>
			<li class="nav-item active">
				<a
				class="nav-link text-muted active"
				data-toggle="tab"
				href="#tab-livestream"
				role="tab"
				aria-controls="nav-home"
				aria-selected="true"
				>Livestream</a>
			</li>
			<li class="nav-item">
				<a class="nav-link text-muted" href="{{site.baseurl}}/conference/papers/">Papers</a>
			</li>
			<li class="nav-item">
				<a class="nav-link text-muted" href="{{site.baseurl}}/conference/papers-visualisation/">Visualization</a>
			</li>
			<li class="nav-item">
				<a class="nav-link text-muted" href="{{site.baseurl}}/conference/chat/">Discussion</a>
			</li>
		</ul>
	</div>
</div>
-->

Keynotes from previous days will be archived below. To watch the keynote sessions live please go to the [livestream]({{site.baseurl}}/conference/livestream/).


{% assign sorted_keynotes = site.data.programme.keynotes | sort: "id" %}

{% for person in sorted_keynotes %}

{% if person.slides-id %}

<div class="row justify-content-around pl-4 pr-4">
	{% capture keynote_day %}
		{% for day in site.data.schedule.schedule %}
			{% for session in day.contents %}
				{% if session.keynote-id == person.id %}
					{{ day.day }}
					{% assign details = session %}
				{% endif %}
			{% endfor %}
		{% endfor %}
	{% endcapture %}
	<div class="col-12"><div class="row pt-2 pb-2 align-items-center">
	    <div class="col-12 col-md-4 col-lg-3"><a class="anchor" id="{{ person.id }}"></a>
	        <div class="text-center">
	            <img src="{{ site.baseurl }}{{ person.img }}" class="rounded-circle img-fluid" style="max-width: 125px;">
	            <h4 class="pt-2"><a href="{{ person.url }}">{{ person.name }}</a></h4>
	            <p class=""><!--<span><b>{{ person.title }}</b></span><br/>-->
	            <span class=""><small>{{ person.job }}</small></span></p>
	        </div>
	    </div>
	    <div class="col-12 col-md-8 col-lg-9">
	        <div class="">
	            <h4 class="pt-1 text-center">{{ person.title }}</h4>
	            <p class="text-center mb-1"><small >({{keynote_day | strip}}: {{details.start-time}} - {{details.end-time}} BST)</small></p>
	            <p class="pb-2">{{ person.abstract }}</p>
	        </div>
	    </div>
	</div></div>
</div>

<div class="pb-3" id="presentation-embed-{{person.slides-id}}"></div>
<script src='https://slideslive.com/embed_presentation.js'></script>
<script>
  embed = new SlidesLiveEmbed('presentation-embed-{{person.slides-id}}', {
      presentationId: '{{person.slides-id}}',
      autoPlay: false, // change to true to autoplay the embedded presentation
      verticalEnabled: true
  });
</script> 
	
{% endif %}

{% endfor %}
