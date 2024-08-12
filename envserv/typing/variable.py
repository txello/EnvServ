class Variable:
    def __init__(self,
            alias:str|None = None,
            overwrite:bool = True,
            error:bool = True,
        ) -> None:
        self.alias = alias
        self.overwrite = overwrite
        self.error = error
        
def variable(
        alias:str|None = None,
        overwrite:bool = True,
        error:bool = True
    ) -> Variable:
    return Variable(alias, overwrite, error)