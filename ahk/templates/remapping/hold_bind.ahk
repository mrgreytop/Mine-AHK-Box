{% extends "base.ahk" %}
{% block body %}
{% for key, value in  bindings.items() %}
{{key}}::
Send {{{value}} down}  ; Hold down the left-arrow key.
KeyWait {{key}}  ; Wait for the user to release the joystick button.
Send {{{value}} up}  ; Release the left-arrow key.
return
{% endfor %}
{% endblock body  %}