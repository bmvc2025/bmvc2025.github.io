---
layout: default_miniconf
title: Browse Papers
permalink: /conference/papers/
index: 10
---










<!-- User Overrides -->
 

<div class="container">
  <!-- Tabs -->
  <div class="tabs">
    
	<ul class="nav nav-pills justify-content-center">
	<li class="nav-item">
    <a class="nav-link text-muted" href="{{site.baseurl}}/conference/schedule/">Schedule</a>
    </li>
    <li class="nav-item">
	    <a class="nav-link text-muted" href="{{site.baseurl}}/conference/announcements/">Announcements</a>
	</li>
    <li class="nav-item">
        <a class="nav-link text-muted" href="{{site.baseurl}}/conference/livestream/">Livestream</a>
    </li>
	<li class="nav-item active">
	<a
	  class="nav-link text-muted active"
	  data-toggle="tab"
	  href="#tab-browse"
	  role="tab"
	  aria-controls="nav-home"
	  aria-selected="true"
	  >Papers
	</a>
	</li>
	<li class="nav-item">
	<a class="nav-link text-muted" href="{{site.baseurl}}/conference/papers-visualisation/">Visualization</a>
	</li>
	<li class="nav-item">
	<a class="nav-link text-muted" href="{{site.baseurl}}/conference/chat/">Discussion</a>
	</li>

	<!--<li class="nav-item">
		<div class="float-right">
			<div class="btn-group">
			    <button type="button" class="btn btn-secondary">All Sessions</button>
			    <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" id="dropdownMenuReference" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" data-reference="parent">
			      <span class="sr-only">Toggle Dropdown</span>
			    </button>
			    <div class="dropdown-menu" aria-labelledby="dropdownMenuReference">
			      <a class="dropdown-item" href="#?session=">All Sessions</a>
				  <div class="dropdown-divider"></div>
			      <a class="dropdown-item" href="{{site.baseurl}}/conference/papers/?session=O1&filter=keywords">Oral 1</a>
			      <a class="dropdown-item" href="{{site.baseurl}}/conference/papers/?session=O2&filter=keywords">Oral 2</a>
			      <a class="dropdown-item" href="{{site.baseurl}}/conference/papers/?session=P1S1&filter=keywords">Poster 1</a>
			      <a class="dropdown-item" href="#">Oral 3</a>
			      <a class="dropdown-item" href="#">Oral 4</a>
			      <a class="dropdown-item" href="#">Poster 2</a>
			      <a class="dropdown-item" href="#">Oral 5</a>
			      <a class="dropdown-item" href="#">Oral 6</a>
			      <a class="dropdown-item" href="#">Poster 3</a>
			      <a class="dropdown-item" href="#">Oral 7</a>
			      <a class="dropdown-item" href="#">Oral 8</a>
			      <a class="dropdown-item" href="#">Poster 4</a>
			    </div>
			  </div>
		</div>
	</li>-->

	</ul>


	  </div>
	  <!-- Content -->
	  <div class="content">
	    
	<div class="row p-3"></div>

	<!-- Session -->
	<div class="row d-none session_notice">
	<div
	class="alert alert-warning alert-dismissible fade show col-12"
	role="alert"
	>
	Showing papers for
	<span id="session_name" style="font-weight: bold;"></span>.
	<button
	  type="button"
	  class="close remove_session"
	  data-dismiss="alert"
	  aria-label="Close"
	>
	  <span aria-hidden="true">&times;</span>
	</button>
	</div>
</div>

<!-- Buttons -->
<div class="row">

<div class="col-12 col-sm-12 col-md-6 col-lg-4">
	<div class="input-group mb-3">
	  <input
	    type="text"
	    class="form-control typeahead_all"
	    placeholder="Search"
	  />
	  <div class="input-group-append">
	    <button
	      class="btn btn-outline-secondary typeahead_all_clear"
	      type="button"
	    >
	      &times;
	    </button>
	  </div>
	</div>
</div>

<div
class="col-12 col-sm-6 col-md-6 col-lg-4 text-center"
style="margin-bottom: 10px;"
>
<div class="btn-group btn-group-toggle filter_option">
  <label
    class="btn btn-outline-secondary"
    data-tippy-content="Search for papers titles"
  >
    <input
      type="radio"
      name="options"
      value="titles"
      autocomplete="off"
      checked
    />
    title
  </label>
  <label
    class="btn btn-outline-secondary"
    data-tippy-content="Search for papers with specific keywords"
  >
    <input
      type="radio"
      name="options"
      value="keywords"
      autocomplete="off"
    />
    keyword
  </label>
  <label
    class="btn btn-outline-secondary active"
    data-tippy-content="Search for papers from specific authors"
  >
    <input type="radio" name="options" value="authors" autocomplete="off" />
    author
  </label>
</div>
</div>
<div class="col-12 col-lg-4">
<button class="btn btn-outline-secondary reshuffle">shuffle</button>
<div class="float-right">
  <div
    class="btn-group btn-group-toggle render_option"
    data-toggle="buttons"
  >
    <label class="btn btn-outline-secondary active">
      <input type="radio" name="options" value="list" autocomplete="off" />
      list
    </label>
    <label class="btn btn-outline-secondary active">
      <input
        type="radio"
        name="options"
        value="compact"
        autocomplete="off"
        checked
      />
      compact
    </label>
    <label class="btn btn-outline-secondary">
      <input
        type="radio"
        name="options"
        value="detail"
        autocomplete="off"
      />
      detail
    </label>
  </div>
</div>
</div>
</div>

<!-- Cards -->
<div class="cards row"></div>
<script src="{{site.baseurl}}/static/js/little_helpers.js"></script>
<script src="{{site.baseurl}}/static/js/lazy_load.js"></script>
<script src="{{site.baseurl}}/static/js/persistor.js"></script>
<script src="{{site.baseurl}}/static/js/papers.js"></script>
<script>
$(document).ready(function () {
tippy("[data-tippy-content]", { trigger: "mouseenter focus" });
start();
});
</script>


  </div>
</div>
    
    

<div
  class="gdpr bg-dark text-light"
  style="padding: 10pt; position: fixed; bottom: 0; display: none;"
>
  We use cookies to store which papers have been visited.
  <div class="gdpr-btn btn btn-sm btn-info" style="margin-left: 15pt;">
    I agree
  </div>
</div>
<script src="{{site.baseurl}}/static/js/gdpr_cookies.js"></script>







