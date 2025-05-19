nombre = input(" ingrese su nombre:")


promedio = float(input(" ingrese su promedio:"))

print (f" hola { nombre} tu promedio es de {promedio}")


quintil= int(input(" ingrese su quintil (1,2,3,4,5)"))

if (quintil ==1 or quintil== 2) and promedio >= 6.0:
    descuento = 0.20
    print ((f" hola { nombre}. tiene un descuento de 20 de arancel"))

elif (quintil ==3 or quintil== 4) and promedio >= 6.0:
    descuento = 0.15
    print ((f" hola { nombre}. tiene un descuento de 15 de arancel"))

elif (quintil ==1 or quintil== 2) and  5.0 < promedio <= 6.0:
    descuento = 0.13
    print ((f" hola { nombre}. tiene un descuento de 13 de arancel"))

elif (quintil ==3 or quintil== 4) and  5.0 < promedio <=  6.0:
    descuento = 0.10
    print ((f" hola { nombre}. tiene un descuento de 20 de arancel"))
else:
    print ((f" hola { nombre}. no tiene descuento de arancel"))

arancel = float(input(" ingrese el valor arancel"))
matricula = float(input(" ingrese el valor matricula:"))


monto_final = arancel* (1- descuento)
total_a_pagar = monto_final + matricula


print (nombre)
print (f" tu pomedio es {promedio}")
print (quintil)
print (f" descuento aplicado : { descuento*100}%")
print (f" arancel con descuento { monto_final}")
print (matricula)
print(f" total a pagar : {total_a_pagar}")
