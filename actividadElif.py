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

figura = input ("Seleccione la figura que desea calcular: 1: Triangulo, 2: Circulo, 3: Cuadrado, 4: Rectangulo `\n`")


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
    print("Selecciones una opcion valida")