from typing import Any
from types import NoneType
from dotenv import load_dotenv, set_key
from .errors import EnvfileError, EnvVariableError, EnvTypeError
import os, json, ast

class EnvBase:
    cache = {}
    __envfile__ = ''
    def __init__(self,encoding:str = 'utf-8') -> None:
        if self.__class__.__envfile__ == '':
            env = False
        else:
            env = load_dotenv(self.__class__.__envfile__,encoding=encoding)
            if not env:
                raise EnvfileError("Failed to load env file: File does not exist")
        for key,value in self.__class__.__annotations__.items():
            var = os.environ.get(key)
            if var == None or key in self.__class__.__dict__:
                try:
                    result = self.__class__.__dict__[key]
                except KeyError:
                    raise EnvVariableError("Failed to get variable: {key}".format(key=key))
                if type(result) != dict:
                    raise EnvVariableError("Failed to get variable: {key}".format(key=key))
                if 'Variable' in result and result['Variable'] == True:
                    if result['alias'] != None:
                        var = os.environ.get(result['alias'])
                        EnvBase.cache.update({key:{'alias':result['alias']}})
                    if result['overwrite'] == False:
                        EnvBase.cache.update({key:{'overwrite':False}})
            try: 
                if value in [list,dict]:
                    setattr(self.__class__,key,ast.literal_eval(var))
                else:
                    setattr(self.__class__,key,value(var))
            except (TypeError, ValueError):
                if value == NoneType:
                    if var.capitalize() in ['None', 'Null']:
                        setattr(self.__class__,key,None)
                    else:
                        raise EnvTypeError("Failed to set variable {key}: Cannot convert value {var} to {value}".format(key=key, var=var, value=value))
                else:
                    raise EnvTypeError("Failed to set variable {key}: Unable to convert variable to data type {value}".format(key=key, value=value))
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in EnvBase.cache:
            if 'overwrite' in EnvBase.cache[__name] and EnvBase.cache[__name]['overwrite'] == False:
                raise EnvVariableError(f"Error overwriting variable {__name}: It cannot be overwritten")
        _n__name = EnvBase.cache[__name]['alias'] if __name in EnvBase.cache else __name
        if self.__class__.__envfile__ != '': set_key(self.__class__.__envfile__,_n__name,str(__value))
        else: os.environ[_n__name] = str(__value)
        if self.__class__.__annotations__[__name] == NoneType:
            return setattr(self.__class__,__name,__value)
        return setattr(self.__class__,__name,self.__class__.__annotations__[__name](__value))
    
    def __repr__(self) -> str:
        result = []
        for key, value in self.__annotations__.items():
            result.append(f"{key}:{value} = {self.__class__.__dict__[key]}")
        return f"EnvServ({', '.join(result)})"
    
    def all(self,dumps=False) -> dict:
        result = {}
        for key in self.__annotations__:
            result.update({key:self.__class__.__dict__[key]})
        if dumps:
            return json.dumps(result)
        return result
    
def variable(alias=None,overwrite=True):
    return {'Variable':True, 'alias':alias, 'overwrite':overwrite}