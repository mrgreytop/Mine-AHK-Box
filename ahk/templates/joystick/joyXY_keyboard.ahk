{% extends "base.ahk" %}
{% block body %}
KeysDown := []
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

WatchAxis:
JoyX := GetKeyState("{{axes['X']}}")  
JoyY := GetKeyState("{{axes['Y']}}") 
KeysDown := KeysToHoldDown

KeysToHoldDown := GetDirection(JoyX, JoyY)

{% raw %}
SetKeyDelay -1  ; Avoid delays between keystrokes.
if (KeysToHoldDown = KeysDown){
    return
}else{
    for index, key in KeysDown
        Send {%key% Up}
    for index, key in KeysToHoldDown
        Send {%key% Down}
}
return
{% endraw %}
{% endblock body %}