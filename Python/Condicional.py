# Condicionales (IF - ELIF):
# Validar si el numero ingresado es par o impar

"""numero = int (input("Ingrese un numero entero positivo: "))

if numero % 2 == 0:
    print("el numero es par")
    print(f"el {numero} es par")
    print("El numero {} es par".format(numero))
    print("El numero", numero, "Es par")
else:
    print("El numero es impar")"""

#Solicitar nombre,edad de un usuario y si el usuario tiene o no pasaporte. Si el usuario es mayor de edad y tiene pasaporte debe mostrar "Puede realizar viajes internacionales", de lo contrario "No puede abandonar el pais"

"""nombre = input("Ingrese el nombre del usuario: ")
edad = int (input("Ingrese la edad del usuario: "))
pasaporte =bool  (input ("Tiene pasaporte? True/False: "))

if edad >= 18 and pasaporte == True:
    print("Puede realizar viajes internacionales")
else:
    print("No puede abandonar el pais")"""

# Elif: Se utiliza para validar 2 o mas condiciones 

nombre = input("Ingrese el nombre del usuario: ")
edad = int (input("Ingrese la edad del usuario: "))
pasaporte =bool  (input ("Tiene pasaporte? True/False: "))

if edad >= 18 and pasaporte == True:
    print("Puede realizar viajes internacionales")
elif edad <= 18 and pasaporte == True:
    print("Puede realizar viajes internacionales con un mayor de edad")
elif edad >= 18 and pasaporte == False:
    print("Debe volver a solicitar cita")
else:
    print("No puede abandonar el pais")