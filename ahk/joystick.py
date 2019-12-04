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

    def bind(self, bindings, mode = "simple", **kwargs):
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

        if mode == "simple":    
            script = self.render_template('joystick/simple_bind.ahk', bindings = bindings)
        elif mode == "hold":
            script = self.render_template('joystick/hold_bind.ahk', bindings = bindings)
        elif mode == "multihold":
            script = self._bind_multihold(bindings = bindings,**kwargs)

        self.run_script(script, blocking=False)
        # logger.debug(f"this is the script:\n{script}")
        
    
    def _bind_multihold(self, **kwargs):
        timer = kwargs.pop("timer", 10)
        try:
            bindings = kwargs.pop("bindings")
            return self.render_template('joystick/multihold_bind.ahk', bindings = bindings, timer = timer)
        except KeyError as e:
            raise KeyError(f"bindings not found")


    
