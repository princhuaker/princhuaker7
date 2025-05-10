# Definimos precios
precio_entrada = 15000
precio_entrada_prime = 45000

print("Bienvenido al cine")

# Pedimos el nombre
nombre = input("Ingrese su nombre: ")

# Pedimos la edad
print(f"Hola {nombre}, ¿qué edad tienes?")
edad = int(input("Ingrese su edad: "))

# Verificamos la edad
if edad >= 18:
    # opcion menu
    print(" que tipos de entrada deseas?")
    print(" 1. normal ($15.000)")
    print("2. prime (45.000)")
    opcion = int(input(" ingresa una opcion 1 / 2:"))

    if opcion == 1:
        precio = precio_entrada
        opcion = " normal"
    elif opcion == 2:
        precio = precio_entrada_prime
        opcion = "prime"
    else:
        print (" la  opcion es invalida")

    # Pedimos cuántas entradas quiere
    cantidad_entradas = int(input("Ingrese el número de entradas: "))
    total = cantidad_entradas * precio_entrada

    print("El total a pagar es:", total)

    # Pedimos el pago
    pago = int(input("¿Con cuánto desea pagar?: "))
    vuelto = pago - total

    print("Su vuelto es:", vuelto)
# si edad  es menor que 18 , no podra ingrear
else:
    print(f"Tienes {edad} años, no puedes ingresar.")
