from ahk.script import ScriptEngine
from ahk.keys import Key
# from ahk.directives import *


class MyDict(dict):
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self._d = {**kwargs}

        if len(args) == 1:
            if hasattr(args[0], "__iter__"):
                self._d = self + dict(args[0])
            else:
                raise TypeError(f"Operand type(s) must be iterable for : '{type(args[0])}'")
        else:
            raise TypeError(f"{self.__class__.__name__} expected at most 1 arguments, got {len(args)}")
        
        if not hasattr(self, "_d"):
            self._d = {}
        
        self.dict = dict(self._d)        

    def __add__(self, other: dict):
        return MyDict({**self, **other})

class BindingsMixin(ScriptEngine):
    def bind(self, key1, key2):
        """
        remap key1 to key2

        :param key1: the name of the key to map
        :param key2: the name of key to map to
        """

        script = self.render_template('remapping/key_bind.ahk', key1 = key1, key2 = key2)
    
    def bind_combo(self, key1, combo):
        pass

    def bind_multi(self, *args, **kwargs):
        if len(args) > 0:
            for arg in args:
                if isinstance(dict):
                    pass


a = MyDict(a = 1)
b = MyDict({"b": 2})
c = MyDict({"c1":3},c2 = 3)
d = MyDict(a)

print(a)
print(b)
print(c)
print(d)