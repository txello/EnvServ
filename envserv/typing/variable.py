class Variable:
    def __init__(self,
            var = ...,
            alias: str | None = None,
            overwrite: bool = True,
            error: bool = True,
        ) -> None:
        self.var = var
        self.alias = alias
        self.overwrite = overwrite
        self.error = error
        
def variable(
        var = ...,
        alias: str | None = None,
        overwrite: bool = True,
        error: bool = True
    ) -> Variable:
    return Variable(var=var, alias=alias, overwrite=overwrite, error=error)
