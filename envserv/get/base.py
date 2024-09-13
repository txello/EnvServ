from dotenv import load_dotenv
from .. import errors
from ..typing.variable import Variable
from .variables import EnvType
from typing import Any
from types import EllipsisType
import os, json
class EnvBase:
    __slots__ = '_cache',
    __envfile__ = ''
    
    def __init__(self,
            encoding:str = 'utf-8'
        ) -> None:
        
        self._encoding = encoding
        self._cache:dict[str, Variable] = {}
        
        self.__readenv()
        vars = self.__getvars()
        self.__setvalues(vars)
        
    
    def __readenv(self):
        if self.__class__.__envfile__:
            load_dotenv(self.__class__.__envfile__,encoding=self._encoding)
            if not os.path.isfile(self.__class__.__envfile__):
                raise errors.EnvfileError("Failed to load env file: File does not exist")
            
    def __getvars(self):
        vars:dict[str, Variable] = {}
        for name in self.__class__.__annotations__.keys():
            if name in self.__class__.__dict__:
                variable = self.__class__.__dict__[name]
            else:
                variable = Variable()
            if not isinstance(variable, Variable):
                variable = Variable(var=variable)
            vars.update({name: variable})
        return vars
    
    def __setvalues(self, vars:dict[str, Variable]):
        for name, typing in self.__class__.__annotations__.items():
            
            variable = vars[name]
            self._cache.update({name: variable})
            
            if variable.alias is None:
                var = os.environ.get(name)
            else:
                var = os.environ.get(variable.alias)
                
            if variable.error:
                if var is None and isinstance(variable.var, EllipsisType):
                    raise errors.EnvValueError("Failed to get value: {key}".format(key=name))
            
            if not isinstance(variable.var, EllipsisType):
                var = variable.var if var is None else var
            
            if var is not None or not isinstance(variable.var, EllipsisType):
                var = EnvType(name, var, typing, error=variable.error)
                
                
            
            setattr(self.__class__, name, var)
    
    def __repr__(self) -> str:
        result = []
        for key, typing in self.__annotations__.items():
            result.append(f"{key}:{typing} = {self.__class__.__dict__[key]}")
        return f"EnvServ({', '.join(result)})"

    def __setattr__(self, name: str, value: Any) -> None:
        if isinstance(self.__class__._cache, dict):
            if name in self.__class__._cache:
                variable:Variable = self.__class__._cache[name]
                if variable.error:
                    
                    if not variable.overwrite:
                        raise errors.EnvOverwriteError("Failed to overwrite: {key}".format(key=name))
                    
                    if not isinstance(value, self.__class__.__annotations__[name]):
                        raise errors.EnvOverwriteError("Failed to overwrite {key}: Invalid data type".format(key=name))
                
        setattr(self.__class__, name, value)
    
    def all(self,
            toString:bool = False
        ) -> dict[str, list[Any, type]]:
        result = {}
        for key in self.__annotations__.keys():
            value = self.__class__.__dict__[key]
            if toString:
                if isinstance(value, set):
                    value = list(value)
            
            result.update({key: value})
        return result
    
    def json(self) -> str:
        result = self.all(toString=True)
        return json.dumps(result)