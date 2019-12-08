# import ast
import logging
from ahk.script import ScriptEngine
from ahk.utils import make_logger

logger = make_logger(__name__)


class BindingMap(dict):
    """
    Subclass of dict which incorporates an __add__ method
    """
    def __init__(self, *args, **kwargs):

        if len(args) == 1:
            if hasattr(args[0], "__iter__"):
                if len(kwargs) > 0:
                    self._d = dict(args[0], **kwargs)
                else:
                    self._d = dict(args[0])
            else:
                raise TypeError(f"Operand type(s) must be iterable for : '{type(args[0])}'")
        elif len(args) != 0:
            raise TypeError(f"{self.__class__.__name__} expected at most 1 arguments, got {len(args)}")
        else:
            if len(kwargs) > 0:
                self._d = dict(**kwargs)
            else:
                self._d = {}
        
        super().__init__(self._d)
        
    def __add__(self, other: dict):
        return BindingMap({**self, **other})

class JoyStickMixin(ScriptEngine):
    
    bind_modes = {
        "simple":"_simple",
        "hold":"_hold",
        "multihold":"_multihold",
        "script":"_bind_script"
    }

    def joy_bind(self, bindings = {}, mode = "simple", **kwargs):
        """
        remap keys according to bindings

        https://www.autohotkey.com/docs/misc/RemapJoystick.htm

        :param bindings: a BindingMap/dict where each key is the name of the key to map
                    and each value is the name of the key to map to
        :param mode: string with 3 possible values, simple, hold and multihold.
        simple mode: key::value
        hold: see Method #2 in link above
        multihold: see Method #3 in link above
        """
        if not isinstance(bindings, dict):
            raise TypeError(f"Unsupported operand type for map: {type(bindings)}")

        builder = self.__getattr__(bind_modes[mode])
        script = bu(bindings = bindings, **kwargs)

        self.run_script(script, blocking=False)
        # logger.debug(f"this is the script:\n{script}")
        
    
    def _multihold(self, **kwargs):
        timer = kwargs.pop("timer", 10)
        try:
            bindings = kwargs.pop("bindings")
            return self.render_template('joystick/multihold_bind.ahk', bindings = bindings, timer = timer)
        except KeyError as e:
            raise KeyError(f"bindings not found")

    def _simple(self, **kwargs):
        bindings = kwargs.pop("bindings", False)

        if bindings == False:
            raise ValueError("No bindings given")
        
        return self.render_template('joystick/simple_bind.ahk', bindings=bindings)

    def _hold(self, **kwargs):
        bindings = kwargs.pop("bindings", False)

        if bindings == False:
            raise ValueError("No bindings given")

        return self.render_template('joystick/hold_bind.ahk', bindings=bindings)
    
    def _script(self, **kwargs):
        raise NotImplementedError

    def joyXY_keyboard(self,
    timer = 5, 
    axes = {"X":"JoyX", "Y":"JoyY"},
    keys = {"Left":"a", "Right":"d","Up":"w","Down":"s"}):
        
        """
        Maps the input from an analog stick to for direction keys
        https://www.autohotkey.com/docs/misc/RemapJo-ystick.htm#joystick-axes
        """
        script = self.render_template("joystick/joyXY_keyboard.ahk", keys = keys, axes = axes, timer = timer)
        self.run_script(script, blocking=False)
        
        

    def joy_2_mouse(self,
    timer = 5,
    sensitivity = 0.3,
    axes={"X": "JoyU", "Y": "JoyR"},
    thresholds = {"Upper":60, "Lower":40},
    mode = "FPS"):

        """
        https://www.autohotkey.com/docs/scripts/JoystickMouse.htm
        """

        script = self.render_template(
            "joystick/joy_2_mouse.ahk", 
            sens = sensitivity, axes=axes, 
            timer=timer, thresholds = thresholds, mode = mode)

        # logger.debug(script)
        self.run_script(script, blocking = False)

    def trigger_2_keys(self,
    trigger = "JoyZ",
    thresholds = {"Upper":70,"Lower":30},
    keys = ["MouseButton1","MouseButton2"],
    timer = 10):
        
        script = self.render_template(
            'joystick/trigger_2_keys', 
            keys = keys, 
            thresholds = thresholds, 
            trigger = trigger,timer = timer)
        
        logger.debug(f"\n{script}")