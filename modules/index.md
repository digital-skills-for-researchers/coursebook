---
title: Digital Skills for Researchers
layout: module
---

# Modules

<ul>
{% for module in site.data.modules %}

	<li>
		<a href="{{ site.baseurl }}/modules/{{ module.slug }}"
		   class="">
			{{ module.name }}
		</a>
	</li>

{% endfor %}
</ul>