# import ast
import logging
from ahk.script import ScriptEngine
from ahk.utils import make_logger
from ahk.keys import Key, KeyModifier

logger = make_logger(__name__)

class JoyStickMixin(ScriptEngine):
    
    _bind_modes = {
        "simple":"_simple",
        "hold":"_hold",
        "script":"_simple_script",
        "holdscript":"_hold_script"
    }

    def joy_bind(self, bindings = {}, mode = "multihold", **kwargs):
        """
        remap keys according to bindings

        https://www.autohotkey.com/docs/misc/RemapJoystick.htm#different-approaches

        :param bindings: a BindingMap/dict where each key is the name of the key to map
                    and each value is the name of the key to map to
        :param mode: string with 3 possible values, simple, hold and multihold.
        simple mode: key::value
        hold: see Method #3 in link aboves
        """
        if not isinstance(bindings, dict):
            raise TypeError(f"Unsupported operand type for map: {type(bindings)}")

        if mode.lower() in self._bind_modes:
            builder = getattr(self, self._bind_modes[mode.lower()])
        else:
            logger.error(f"invalid mode ({mode}) selected")
            raise ValueError(f"invalid mode ({mode}) selected")

        script = builder(bindings = bindings, **kwargs)

        proc = self.run_script(script, blocking=False)
        return proc
           
    def _hold(self, **kwargs):
        bindings = kwargs.pop("bindings", False)
        if bindings == False:
            raise KeyError("bindings not found")

        timer = kwargs.pop("timer", 10)
        delay = kwargs.pop("delay", 200)

        for key, value in bindings.items():
            KeyVal = Key(key_name = value)
            bindings[key] = {
                "up": f"Send {KeyVal.UP}",
                "down": f"Send {KeyVal.DOWN}\nSleep, {delay}",
                "held": f"Send {KeyVal.DOWN}"
            }

        # return self.render_template('joystick/multihold_bind.ahk', bindings = bindings, timer = timer)
        return self._hold_script(bindings = bindings)

    def _simple(self, **kwargs):
        bindings = kwargs.pop("bindings", False)

        if bindings == False:
            raise ValueError("No bindings given")
        
        return self.render_template('joystick/simple_bind.ahk', bindings=bindings)
    
    def _simple_script(self, **kwargs):
        raise NotImplementedError

    def _hold_script(self, **kwargs):
        bindings = kwargs.pop("bindings", {})
        timers = kwargs.pop("timer", [10]*len(bindings))

        for key, script in bindings.items():
            try:
                bindings[key]["up"] = script.pop("up", False)
                bindings[key]["down"] = script.pop("down", False)
                bindings[key]["held"] = script.pop("held", "return")
            except AttributeError as e:
                logger.error(f"\n{e.with_traceback}")
                raise TypeError(f"script for {key} must be a dict not a {type(script)}")

            for state, action in script.items():
                if action == False:
                    raise ValueError(f"The script for key {state} is undefined")
        
        if len(timers) != len(bindings):
            raise ValueError(f"Number of timers ({len(timers)}) must be equal to the number of bindings ({len(bindings)})")

        bindings_timer = zip(bindings.items(), timers)
        return self.render_template("joystick/holdscript_bind.ahk",bindings_timer = bindings_timer)

    def joyXY_keyboard(self,
    timer = 5, 
    axes = {"X":"JoyX", "Y":"JoyY"},
    keys = {"Left":"a", "Right":"d","Up":"w","Down":"s"},
    modifiers = {}):
        
        """
        Maps the input from an analog stick to four direction keys with 8 directional output
        """
        
        script = self.render_template("joystick/joyXY_keyboard.ahk", 
        keys = keys, axes = axes, timer = timer, modifiers = modifiers)
        proc = self.run_script(script, blocking=False)
        return proc
    
    def joy_2_mouse(self,timer = 5,
    sensitivity = 0.3,axes={"X": "JoyU", "Y": "JoyR"},
    thresholds = {"Upper":55, "Lower":45},mode = "FPS"):

        """
        https://www.autohotkey.com/docs/scripts/JoystickMouse.htm
        """

        script = self.render_template(
            "joystick/joy_2_mouse.ahk", 
            sens = sensitivity, axes=axes, 
            timer=timer, thresholds = thresholds, mode = mode)

        # logger.debug(script)
        proc = self.run_script(script, blocking = False)
        return proc

    def triggers_2_mouseclick(self,threshold = 190,
    timer = 5,joystick = 1,mapping = {"LT":"right", "RT":"left"}):
        
        script = self.render_template(
            'joystick/trigger_2_mouseclick.ahk', 
            threshold = threshold, 
            timer = timer,
            joystick = joystick,
            mapping = mapping)
        
        # logger.debug(f"\n{script}")
        proc = self.run_script(script, blocking=False)
        return proc

    def joy_gridmouse(self,dx=15,dy=15,freq=100,delay=0):

        script = self.render_template(
            'joystick/joy_gridmouse.ahk',
            dx = dx, dy = dy, freq = freq, delay = delay
        )

        proc = self.run_script(script, blocking = False)
        return proc
