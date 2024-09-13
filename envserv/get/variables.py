from ..errors import EnvTypeError
import ast
from types import NoneType

class EnvType:
    def __new__(self, name, value:str, typing, error:bool):
        if error:
            if typing in [list, dict, bool, set]:
                return self.type_literal(name, value, typing)
            
            if typing in [None, NoneType]:
                return self.type_none(name, value)
        return self.type_any(name, value, typing, error)
    
    def type_literal(name, value:str, typing):
        result = ast.literal_eval(value)
        if not isinstance(result, typing):
            raise EnvTypeError("Failed to set value: {key}".format(key=name))
        return result
    
    def type_none(name, value:str):
        if value.lower() in ['null', 'none']:
            return None
        raise EnvTypeError("Failed to set value: {key}".format(key=name))
    
    def type_any(name, value:str, typing, error):
        if error:
            try:
                result = typing(value)
            except (ValueError, TypeError):
                raise EnvTypeError("Failed to set value: {key}".format(key=name))
        else: result = str(value)
        return result