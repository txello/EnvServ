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
# Version logger:

### 1.0.0
* Model added
* Added variable change
* Added class instance information output
