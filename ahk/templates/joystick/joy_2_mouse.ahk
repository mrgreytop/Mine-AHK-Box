{% extends "base.ahk" %}
{% block body %}
SetTimer, WatchJoystick, {{timer}}
return

GetDelta(axis){
    if (axis < {{thresholds["Lower"]}}){
        delta := axis - {{thresholds["Lower"]}}
    }else if (axis > {{thresholds["Upper"]}}){
        delta := axis - {{thresholds["Upper"]}}
    }else{
        delta := 0
    }
    return delta
}

WatchJoystick:
    X := GetKeyState("{{axes['X']}}")
    Y := GetKeyState("{{axes['Y']}}")

    deltaX := Getdelta(X)
    deltaY := Getdelta(Y)

    if abs(deltaX) > 0 or abs(deltaY) > 0
        {% if mode == "desktop" %}
        MouseMove, deltaX*{{sens}}, deltaY*{{sens}}, 0, R
        {% elif mode == "FPS" %}
        DllCall("mouse_event" ,uint, 1, int, deltaX*{{sens}}, int, deltaY*{{sens}})
        {% endif %}
    return

{% endblock body %}