from Usuario import usuario
def Registro():
        Usuario = input("----------------------\n1/5 Ingrese su usuario: ")
        nombre = input("1/4 Ingrese su nombre: ")
        contra = input("2/4 Ingrese su contraseña: ")
        curp = input("3/4 Ingrese su CURP ")
        cuidad = input("4/4 Ingrese su cuidad ")
        rol = "Cliente"
        if not dicc:
            User = usuario(Usuario,contra,rol,nombre,curp,cuidad)
            dicc.add(User)
            print("¡Se ha registrado exitosamente! primer inicio de sesion")
        else:
            for x in dicc:
                if x._CURP == curp:
                    print("¡El usuario ya existe!")
                    break
                else:
                    User = usuario(Usuario,contra,rol,nombre,curp,cuidad)
                    dicc.add(User)
                    print("¡Se ha registrado exitosamente!")
                    break
def IniciarSesion():
    Usuario = input("----------------------\nIngrese su usuario: ")
    contra = input("Ingrese su contraseña: ")
    for x in dicc:
        if x._Usuario == Usuario and x._Contraseña == contra:
            if x._Rol == "Administrador":
                for z in dicc:
                    print(z)
                break
            else:
                print(x)
                break
    else:
        print("Datos incorectos")
    pass
Admin = usuario("root","1234","Administrador","Eduardo Leyva","GOLJ001230HTNYNA8","Nuevo Laredo")
dicc= set()
dicc.add(Admin)
bandera = True
while bandera:
    Opcion = int(input("1.-Registro \n2.-Inicio de sesion \n3.-Salida \n"))
    if Opcion== 1:
        Registro()
    elif Opcion == 2:
        IniciarSesion()
    elif Opcion == 3:
        print("Hasta la proxima")
        break
    else:
        print("selecione una opcion Valida")