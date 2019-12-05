{% extends "base.ahk" %}
{% block body %}
SetTimer, WatchAxis, {{timer}}
return

WatchAxis:
JoyX := GetKeyState("{{axes['X']}}")  
JoyY := GetKeyState("{{axes['Y']}}") 
KeyToHoldDownPrev := KeyToHoldDown  ; Prev now holds the key that was down before (if any).

if (JoyX > 100-{{threshold}})
    KeyToHoldDown := "{{keys['Right']}}"
else if (JoyX < {{threshold}})
    KeyToHoldDown := "{{keys['Left']}}"
else if (JoyY > 100-{{threshold}})
    KeyToHoldDown := "{{keys['Down']}}"
else if (JoyY < {{threshold}})
    KeyToHoldDown := "{{keys['Up']}}"
else
    KeyToHoldDown := ""

if (KeyToHoldDown = KeyToHoldDownPrev)  ; The correct key is already down (or no key is needed).
    return  ; Do nothing.

{% raw %}
; Otherwise, release the previous key and press down the new key:
SetKeyDelay -1  ; Avoid delays between keystrokes.
if KeyToHoldDownPrev   ; There is a previous key to release.
    Send, {%KeyToHoldDownPrev% up}  ; Release it.
if KeyToHoldDown   ; There is a key to press down.
    Send, {%KeyToHoldDown% down}  ; Press it down.
return
{% endraw %}
{% endblock body %}