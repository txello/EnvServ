class EnvfileError(ImportError):
    def __init__(self, *args: object, name: str | None = ..., path: str | None = ...) -> None:
        super().__init__(*args, name=name, path=path)
        
class EnvVariableError(NameError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class EnvTypeError(TypeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)