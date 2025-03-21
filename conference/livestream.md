---
layout: default_miniconf
title: Livestream
permalink: /conference/livestream/
index: 7
---

<div class="container mb-3 pb-3">
	<div class="tabs">

		<ul class="nav nav-pills justify-content-center">
			<li class="nav-item">
				<a class="nav-link text-muted" href="{{site.baseurl}}/conference/schedule/">Schedule</a>
			</li>
			<li class="nav-item">
		        <a class="nav-link text-muted" href="{{site.baseurl}}/conference/announcements/">Announcements</a>
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

<h3 class="mt-2">Livestream</h3>

{% assign livestream-id = site.data.livestream.day-four %}

<div id="presentation-embed-{{livestream-id}}"></div>
<script src='https://slideslive.com/embed_presentation.js'></script>
<script>
  embed = new SlidesLiveEmbed('presentation-embed-{{livestream-id}}', {
      presentationId: '{{livestream-id}}',
      autoPlay: false, // change to true to autoplay the embedded presentation
      verticalEnabled: true
  });
</script> 

<h3 class="mt-3 pb-2">Discussion</h3>

<p>In order to partake in the live discussion below you need to pay to register and use the login details emailed to you. For registration information, please consult the <a href="{{site.baseurl}}{% link attending/registration.md %}">registration page</a>.</p>

<div style="border: 1px solid #ced4da; border-radius: .25rem;" class="m-1 p-1">
<iframe src="https://chat.bmvc2020-conference.com/channel/livestream?layout=embedded" width="100%" height="700px" frameborder="0"></iframe>
</div>