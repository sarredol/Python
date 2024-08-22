# Solicitar una contraseña, validar si esta tiene una longitud mayor o igual a 16, si es así validar si la contraseña ingresada es igual a una propuesta  por ud, si es igual debe mostrar contraseña correcta, de lo contrario contraseña incorrecta. Debe tener en cuenta  tambien la posibilidad que la contraseña no tenga la longitud requerida.

#funcion para determinar la longitud: len(contraseña)

#pwCorrecta = "PazyaMOR27941015"
pwSolicitar = input("Ingrese la contraseña: ")

if len(pwSolicitar) >= 16:

    if pwSolicitar == "PazyaMOR27941015":
        print("La contraseña es correcta")
    else:
        print("Contraseña incorrecta")
else:
    print("La contraseña no cumple con el total de caracteres")
