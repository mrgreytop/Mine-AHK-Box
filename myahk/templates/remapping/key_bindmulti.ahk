{% extends base.ahk %}
{% block body %}
{% for key, value in  bindings.items() %}
    {{key}}::{{value}}
{% endfor %}
{% endblock body  %}