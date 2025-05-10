import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

print("Tienes 7 intentos para adivinar el número secreto entre 1 y 100.")

while intentos < max_intentos:
    adivina = int(input("Adivina el número: "))
    intentos += 1

    if adivina == numero_secreto:
        print("🎉 ¡Ganaste! Adivinaste el número secreto en", intentos, "intentos.")
        break
    elif adivina < numero_secreto:
        print("🔺 Es mayor que", adivina)
    else:
        print("🔻 Es menor que", adivina)

if intentos == max_intentos and adivina != numero_secreto:
    print("😢 ¡Perdiste! El número secreto era:", numero_secreto)
