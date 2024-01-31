from typing import Any
from dotenv import load_dotenv, get_key, set_key
from .errors import EnvfileError, EnvVariableError

class EnvBase:
    def __init__(self) -> None:
        if not hasattr(self.__class__,'__envfile__'):
            raise EnvfileError("Failed to load env file: No variable __envfile__")
        env = load_dotenv(self.__class__.__envfile__)
        if not env:
            raise EnvfileError("Failed to load env file: File does not exist")
        for key,value in self.__class__.__annotations__.items():
            var = get_key(self.__class__.__envfile__,key)
            if var == None:
                raise EnvVariableError("Failed to get variable: {key}".format(key=key))
            setattr(self.__class__,key,value(var))
            pass
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        set_key(self.__class__.__envfile__,__name,str(__value))
        setattr(self.__class__,__name,self.__class__.__annotations__[__name](__value))
    
    def __repr__(self) -> str:
        result = []
        for key, value in self.__annotations__.items():
            result.append(f"{key}:{value} = {self.__class__.__dict__[key]}")
        return f"EnvServ({', '.join(result)})"
