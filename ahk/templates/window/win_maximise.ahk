{% extends "base.ahk" %}
{% block body %}
WinActivate, ahk_id {{ win.id }}
WinMaximize, A
{% endblock body %}