{% block directives %}
#NoEnv
{% for directive in directives %}
{{ directive }}
{% endfor %}
{% endblock directives %}

{% block body %}

While True{
    
}
{% endblock body %}

{% block exit %}
ExitApp
{% endblock exit %}