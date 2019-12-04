{% extends "base.ahk" %}
{% block body %}
{% for key,value in bindings.items() %}
{{key}}::
Send {{{value}} down}
SetTimer, WaitFor{{key}}Up, {{refresh}}
return

WaitFor{{key}}Up:
if GetKeyState("{{key}}")
    return
Send {{{value}} up}
SetTimer, WaitFor{{key}}Up, Off
return
{%endfor%}
{% endblock body %}