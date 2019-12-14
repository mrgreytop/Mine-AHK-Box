{% extends "base.ahk" %}
{% block body %}
{% for binding, timer in bindings_timer %}
{{binding[0]}}::
{{binding[1]["down"]}}
SetTimer, WaitFor{{binding[0]}}Up, {{timer}}
return

WaitFor{{binding[0]}}Up(){
    if (GetKeyState("{{binding[0]}}")){
        {{binding[1]["held"]}}
    }else{
        {{binding[1]["up"]}}
        SetTimer, WaitFor{{binding[0]}}Up, Off
    }
    return
}
{% endfor %}
{% endblock body %}