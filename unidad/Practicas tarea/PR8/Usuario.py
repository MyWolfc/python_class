class usuario:
    def __init__(self,Usuario,Contraseña,Rol,Nombre,CURP,Cuidad) -> None:
        self._Usuario = Usuario
        self._Contraseña = Contraseña
        self._Rol = Rol
        self._Nombre = Nombre
        self._CURP = CURP
        self._Cuidad = Cuidad

    def __str__(self) -> str:
        return f"------------------------\nUSUARIO: {self._Usuario}\nNOMBRE: {self._Nombre} \nCONTRASEÑA: {self._Contraseña}\nROL: {self._Rol} \nCURP: {self._CURP} \nCUIDAD: {self._Cuidad}\n------------------------"

