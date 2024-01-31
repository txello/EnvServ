class EnvfileError(ImportError):
    def __init__(self, *args: object, name: str | None = ..., path: str | None = ...) -> None:
        super().__init__(*args, name=name, path=path)
        print(*args)
        
class EnvVariableError(NameError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print(*args)