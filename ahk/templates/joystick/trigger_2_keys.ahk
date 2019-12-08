{% extends "base.ahk" %}
{% block body %}
KeysDown := {}
SetTimer, WatchTrigger, {{timer}}
return

AddKeys(Z){

    if (Z > {{thresholds["Upper"]}}){
        KeysDown.Push("right":{{keys[1]}})
    }else if (Z < {{thresholds["Lower"]}}){
        KeysDown.Push("left":{{keys[0]}})
    }

    if KeysDown["right"]
    return
}

WatchTrigger{
    JoyZ = GetKeyState("{{trigger}}")
    
    AddKeys(JoyZ)
}

{% endblock body %}