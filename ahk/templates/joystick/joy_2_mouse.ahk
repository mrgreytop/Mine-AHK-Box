{% extends "base.ahk" %}
{% block body %}

SetTimer, WatchJoystick, {{timer}}
return

WatchJoystick:
MoveMouse := False
X := GetKeyState("{{axes['X']}}")
Y := GetKeyState("{{axes['Y']}}")

Getdelta(X)
; Getdelta(Y)

; s := Format("{1},{2}`n",deltaX,deltaY)
; FileAppend, %s%, "mouse.txt"
return

Getdelta(axis){
    s := Format("X{1}",%axis%)
    FileAppend %s%, *
    ; if (axis > {{thresholds["Upper"]}}){
    ;     delta := axis - {{thresholds["Upper"]}}
    ; }else if (axis < {{thresholds["Lower"]}}){
    ;     delta := axis - {{thresholds["Lower"]}}
    ; }else{
    ;     delta := 0
    ; }
    ; return %delta%
}

{% endblock body %}