# EnvServ

## Before starting, install ```dotenv```

```console
pip install python-dotenv
```

### EnvServ - Model view for easy Python development

#### Example №1

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

    FirstVar: str
    SecondVar: int
    ThirdVar: float

env = MyEnv()

print(env) # EnvServ(FirstVar:<class 'str'> = Hello, world!, SecondVar:<class 'int'> = 42, ThirdVar:<class 'float'> = 23.0)
print(env.FirstVar, env.SecondVar,env.ThirdVar) # Hello, world! 42 23.0
print(type(env.FirstVar), type(env.SecondVar), type(env.ThirdVar)) # <class 'str'> <class 'int'> <class 'float'>
```

#### Example №2

```python
from envserv import EnvBase

class MyEnv(EnvBase):
    __envfile__ = '.env'

    FirstVar: str

env = MyEnv()

env.FirstVar = "New variable value" # Also changes a variable in the .env file

print(env) # EnvServ(FirstVar:<class 'str'> = New variable value)
print(env.FirstVar) # New variable value
print(type(env.FirstVar)) # <class 'str'>
```

#### Example №3

```env
# file: .env
pass = 100
```

```python
from envserv import EnvBase, variable

class MyEnv(EnvBase):
    __envfile__ = '.env'
    
    pass_: int = variable(alias='pass',overwrite=False)

env = MyEnv()

print(env) # EnvServ(pass_:<class 'int'> = 100)
print(env.pass_) # 100
print(type(env.pass_)) # <class 'int'>

env.pass_ = 1 # envserv.errors.EnvVariableError: Error overwriting variable pass_: It cannot be overwritten
```

#### Example №4

```env
# file: .env
A = Text
ERR = this is error
C = [1, 2, 3, 4, 5]
D = {1: 2, 3: 4}
E = null
F = {1,2,3,4,5}
```

```python
from envserv import EnvBase, Variable

class MyEnv(EnvBase):
    __envfile__ = '.env'
    
    A: str
    B: int = Variable(alias="ERR", error=False)
    C: list
    D: dict
    E: None
    F: set
    not_in: str = "test"


env = MyEnv()
print(env.all())
print(env.json())

# Output:
# {'A': 'Text', 'B': 'this is error', 'C': [1, 2, 3, 4, 5], 'D': {1: 2, 3: 4}, 'E': None, 'F': {1, 2, 3, 4, 5}, 'not_in': 'test'}
# {"A": "Text", "B": "this is error", "C": [1, 2, 3, 4, 5], "D": {"1": 2, "3": 4}, "E": null, "F": [1, 2, 3, 4, 5], "not_in": "test"}
```

#### Example 5

```env
# file: .env
json_string = {"checked": null}
```

```python
from envserv import EnvBase
from envserv.typing import JSON

class MyEnv(EnvBase):
    __envfile__ = '.env'
    
    json_string: JSON


env = MyEnv()
print(env.all())
print(env.json())

# Output:
# {'json_string': {'checked': None}}
# {"json_string": {"checked": null}}
```

## Version logger

### 1.0.8

* Added `JSON` support
* Added `CI/CD`
* Version filtering changed from latest to first
* Code refactoring

### 1.0.7

* Fixed `variable` function

### 1.0.6

* Added the ability to have a default value for .env variable
* Fixed reading of .env file

### 1.0.5

* Code refactoring has been completed
* Added class __Variable__
* Added `toString` parameter to __all()__ function and added __json()__ function

### 1.0.4

* Added support for the list, dict and None variable
* Added parameter encoding to the class instance
* Added function __all()__ to display the dictionary

### 1.0.3

* Fix alias param
* Fix error message

### 1.0.2

* Added setting for docker-compose (Variable \_\_envfile\_\_ does not need to be written)

### 1.0.1

* Added rules for variable (beta)

### 1.0.0

* Model added
* Added variable change
* Added class instance information output
