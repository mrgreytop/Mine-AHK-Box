{% extends "base.ahk" %}
{% block body %}
global KeysToHoldDown := []
{% for mod,map in modifiers.items() %}
{% if mod[1] == "T" %}
global {{mod[0]}}flag := False
{% endif %}
{% endfor %}
SetTimer, WatchAxis, {{timer}}
return

GetDirection(X, Y)
{
    if (X<30)
    {
        if (Y<30){
            direction := ["{{keys['Up']}}","{{keys['Left']}}"]
        }else if (Y > 70){
            direction := ["{{keys['Down']}}","{{keys['Left']}}"]
        }else{
            direction := ["{{keys['Left']}}"]
        }
    }else if (X>70)
    {
        if (Y<30){
            direction := ["{{keys['Up']}}","{{keys['Right']}}"]
        }else if (Y > 70){
            direction := ["{{keys['Down']}}","{{keys['Right']}}"]
        }else{
            direction := ["{{keys['Right']}}"]
        }
    }else{
        if (Y<30){
            direction := ["{{keys['Up']}}"]
        }else if (Y > 70){
            direction := ["{{keys['Down']}}"]
        }else{
            direction := []
        }
    }
    return %direction%
}

WatchAxis(){
    JoyX := GetKeyState("{{axes['X']}}")  
    JoyY := GetKeyState("{{axes['Y']}}") 
    KeysDown := KeysToHoldDown

    KeysToHoldDown := GetDirection(JoyX, JoyY)

    {% for mod,map in modifiers.items() %}
    {% if mod[1] == "T" %}
    if (GetKeyState("{{mod[0]}}")){
        if ({{mod[0]}}flag){
            Send, { {{map}} Up}
            {{mod[0]}}flag := False
        }else{
            Send, { {{map}} Down}
            {{mod[0]}}flag := True
        }
    }
    {% else %}
    if (GetKeyState("{{mod[0]}}")){
        Send, { {{map}} Down}
    }else{
        Send, { {{map}} Up}
    }
    {% endif %}
    {% endfor %}

    SetKeyDelay -1  ; Avoid delays between keystrokes.
    {% raw %}
    if (KeysToHoldDown = KeysDown){
        return
    }else{
        for index, key in KeysDown
            Send {%key% Up}
        for index, key in KeysToHoldDown
            Send {%key% Down}
    }
    {% endraw %}
    return
}
{% endblock body %}