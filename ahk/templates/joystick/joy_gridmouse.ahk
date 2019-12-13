{% extends "base.ahk" %}
{% block body %}
; initialise
global Direction := [0,0]
global move := Func("GridMoveMouse").bind(Direction)

SetTimer, WatchPOV, 5
return

GetDir(POV){
    if POV < 0
        return [0,0]
    else if POV > 31401
        return [0, -{{dy}}]
    else if POV between -1 and 4400
        return [0, -{{dy}}]
    else if POV between 4401 and 13400
        return [{{dx}}, 0]
    else if POV between 13401 and 22400
        return [0, {{dy}}]
    else if POV between 22401 and 31400
        return [-{{dx}}, 0]

}

WatchPOV(){
    PrevDirection := Direction
    POV := GetKeyState("JoyPOV")

    Direction := GetDir(POV)

    if (PrevDirection[1] = Direction[1] and PrevDirection[2] = Direction[2]){
        return
    }else if (Direction[1] = 0 and Direction[2] = 0){
 	    SetTimer, %move%, Off
    }else{
        MouseMove, Direction[1], Direction[0], 0, R
        SetTimer, %move%, Off
        move := Func("GridMoveMouse").bind(Direction)
        {% if delay > 0 %}
        Sleep, {{delay}}
        {% endif %}
        SetTimer, %move%, {{freq}}
    }
    return
}

GridMoveMouse(XY){
    MouseMove, XY[1], XY[2], 0, R
    return
}
{% endblock body %}