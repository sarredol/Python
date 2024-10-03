# #Diccionario
# datos_personales = {"Nombre": "Sebastian", 
#                     "Apellido":"Arredondo",
#                     "Edad": 30,
#                     "Sexo": "F"}
# print(type(datos_personales))

# #Opcion 2
# # datos = dict(Nombre = "Juan",
# #              Apellido = "Valdez",
# #              Edad = 30)
# # print(type(datos))

# #acceder a la edad de Sebastian
# print(datos_personales["Edad"])
# print(datos_personales.get("Edad"))

# #Modificar la edad de Sebastian
# datos_personales["Edad"] = 31
# print(datos_personales)
# datos_personales ["Fecha_nac"] = "27/09/1994"
# print(datos_personales)

# #Eliminar elemento
# #pop(clave)
# #popitem()
# datos_personales.popitem()
# print(datos_personales)
# #del, clear
# #keys(), value(), items()

# #keys: obtiene claves del diccionario
# claves = datos_personales.keys()
# print(claves)
# for c in datos_personales.values():
#     print(c)

# #values: obtiene valores del diccionario
# valores = datos_personales.values()
# print(valores)
# for v in datos_personales.values():
#     print(v)

# #items: obtiene claves y valores al tiempo
# CV = datos_personales.items()
# print(CV)
# for c,v in datos_personales.items():
#     print(f"El valor de la clave {c} es {v}")
# otros_datos = {"Fecha_nac":"27/09/2024",
#                "profesion":"ing. sistemas",
#                "ocupacion":"Lider de equipo"}

# #update actualizar diccionario
# datos_personales.update(otros_datos)
# print(datos_personales)

#//////////////////////////////////////////////////////////////////////////////

#Ejercicio 1
#Solicitar un numero por teclado y crear un diccionario, cuyas claves sean desde el 1 hasta el numero ingresado y los valores sean el cubo de las claves. Mostrar claves y su valor correspondiente.

# numero = int(input("Ingrese un número: "))

# diccionario = {
#     clave: clave**3 for clave in range(1, numero+1)
# }

# for c,v in diccionario.items():
#     print(f"El valor de la clave {c} es {v}")

#Ejercicio 2
#Crear un diccionario que almacene nombre de frutas como clave y su precio como valor. Solicitar un nombre de una fruta (validar si la fruta existe o no) si no existe preguntar la cantidad que desea comprar y debe mostrar cual seria el precio total

frutas = {
    "manzana": 3500,
    "pera": 2000,
    "uva": 6000,
    "naranja": 1000
}

nombre_fruta = input("Ingrese el nombre de la fruta: ").lower()

if nombre_fruta in frutas:
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    precio_total = cantidad * frutas[nombre_fruta]
    print(f"El precio total de la compra es {precio_total}")
else: print("La fruta no esta disponible")
