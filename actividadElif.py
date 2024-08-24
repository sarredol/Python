# punto 1

"""current_year = int (input("Ingresar el año actual: "))
another_year = int (input("Ingresar otro año cualquiera: "))

if current_year > another_year:
    diferencia = current_year - another_year
    print(f"faltan {diferencia} años desde el año {another_year}" )
elif current_year < another_year:
    diferencia = another_year- current_year
    print(f"han pasado {diferencia} años desde el año {current_year}" )"""
    
# Punto 2

"""figura = input ("Seleccione la figura que desea calcular: 1: Triangulo, 2: Circulo, 3: Cuadrado, 4: Rectangulo `\n`")


if figura == "1":
    base = int(input("Digite la base"))
    altura = int(input("Digite la altura"))
    area = base * altura
    print(f"El area del Triangulo es {area}")
elif figura == "2":
    base = int(input("Digite la base: "))
    altura = int(input("Digite la altura: "))
    area = base * altura
    print(f"El area del Circulo es {area}")
elif figura == "3":
    base = int(input("Digite la base: "))
    altura = int(input("Digite la altura: "))
    area = base * altura
    print(f"El area del Cuadrado es {area}")
elif figura == "4":
    base = int(input("Digite la base: "))
    altura = int(input("Digite la altura: "))
    area = base * altura
    print(f"El area del Rectangulo es {area}")
else:
    print("Selecciones una opcion valida")"""

# Punto 3

"""num1 = int(input("Ingrese el número 1: "))
num2 = int(input("Ingrese el número 2: "))
num3 = int(input("Ingrese el número 3: "))
num4 = int(input("Ingrese el número 4: "))

numeros = [num1, num2, num3, num4]

if num1 == num2 == num3 == num4:
    print("Todos los números son iguales.")

# Verificar si todos los números son diferentes
elif len(set(numeros)) == 4:
    print("Todos los números son diferentes.")

# Verificar si hay al menos un número repetido
else:
    print("Hay un número repetido al menos 2 veces.")"""

# Punto 4

"""edad = int(input("Digite su edad: "))
ingresos = float(input("Digite sus ingresos mensuales: "))

if edad > 18 and ingresos >= 2500000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")"""


# Punto 5

menu = input("Digite operacion a realizar:\n" 
             "1: suma \n"
             "2: resta \n"
             "3: multiplicacion \n"
             "4: Division \n"
             "5: potenciacion\n"
             "6: resto\n")

if menu == "1":
    num= int (input("Digite el primer numero: "))
    num += int (input("Digite el segundo numero: "))
    print(f"El resultado es {num}")
elif menu == "2":
    num= int (input("Digite el primer numero: "))
    num -= int (input("Digite el segundo numero: "))
    print(f"El resultado es {num}")
elif menu == "3":
    num= int (input("Digite el primer numero: "))
    num *= int (input("Digite el segundo numero: "))
    print(f"El resultado es {num}")
elif menu == "4":
    num= int (input("Digite el primer numero: "))
    num /= int (input("Digite el segundo numero: "))
    print(f"El resultado es {num}")
elif menu == "5":
    num= int (input("Digite el primer numero: "))
    num **= int (input("Digite el segundo numero: "))
    print(f"El resultado es {num}")
elif menu == "6":
    num= int (input("Digite el primer numero: "))
    num %= int (input("Digite el segundo numero: "))
    print(f"El resultado es {num}")
else:
    print("Ingrese una opción válida")