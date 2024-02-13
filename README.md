# EnvServ

###  Before starting, install ```dotenv```
```console
pip install python-dotenv
```

### EnvServ - Model view for easy Python development

Example №1:

```env
# file: .env
FirstVar = Hello, world!
SecondVar = 42
ThirdVar = 23
```

```python
from envserv import EnvBase

class MyEnv(EnvBase):
    __envfile__ = '.env'

    FirstVar:str
    SecondVar:int
    ThirdVar:float

env = MyEnv()

print(env) # EnvServ(FirstVar:<class 'str'> = Hello, world!, SecondVar:<class 'int'> = 42, ThirdVar:<class 'float'> = 23.0)
print(env.FirstVar, env.SecondVar,env.ThirdVar) # Hello, world! 42 23.0
print(type(env.FirstVar), type(env.SecondVar), type(env.ThirdVar)) # <class 'str'> <class 'int'> <class 'float'>
```

Example №2:
```python
from envserv import EnvBase

class MyEnv(EnvBase):
    __envfile__ = '.env'

    FirstVar:str

env = MyEnv()

env.FirstVar = "New variable value" # Also changes a variable in the .env file

print(env) # EnvServ(FirstVar:<class 'str'> = New variable value)
print(env.FirstVar) # New variable value
print(type(env.FirstVar)) # <class 'str'>
```

Example №3:
```env
# file: .env
pass = 100
```
```python
from envserv import EnvBase, variable

class MyEnv(EnvBase):
    __envfile__ = '.env'
    
    pass_:int = variable(alias='pass',overwrite=False)

env = MyEnv()

print(env) # EnvServ(pass_:<class 'int'> = 100)
print(env.pass_) # 100
print(type(env.pass_)) # <class 'int'>

env.pass_ = 1 # envserv.errors.EnvVariableError: Error overwriting variable pass_: It cannot be overwritten
```

Example №4:
```env
# file: .env
A = Text
B = 2
C = [1, 2, 3, 4, 5]
D = {1: 2, 3: 4}
E = null
```
```python
from envserv import EnvBase

from types import NoneType

class MyEnv(EnvBase):
    __envfile__ = '.env'
    
    A:str
    B:int
    C:list
    D:dict
    E:NoneType


env = MyEnv()
print(env.all())
print(env.all(dumps=True))

# Вывод:
# {'A': 'Text', 'B': 2, 'C': [1, 2, 3, 4, 5], 'D': {1: 2, 3: 4}, 'E': None}
# {"A": "Text", "B": 2, "C": [1, 2, 3, 4, 5], "D": {"1": 2, "3": 4}, "E": null}
```

# Version logger:

### 1.0.0
* Model added
* Added variable change
* Added class instance information output

### 1.0.1
* Added rules for variable (beta)

### 1.0.2
* Added setting for docker-compose (Variable \_\_envfile\_\_ does not need to be written)

### 1.0.3
* Fix alias param
* Fix error message

### 1.0.4
* Added support for the list, dict and None variable
* Added parameter encoding to the class instance
* Added function __all()__ to display the dictionary