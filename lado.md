lado1= float(input(" escribe el lado:"))
lado2= float(input(" escribe el lado:"))
lado3= float(input(" escribe el lado:"))

if lado1 >= lado2 or lado2 >= lado1 or lado3 >= lado2 + lado1:
    print (" el triangulo no es valido")
elif lado1 == lado2 or  lado1 == lado3:
    print (" es un triangulo isoceles")
elif lado1 != lado2 or lado2 != lado3:
    print (" es un triangulo escaleno")
else:
    print (" algo esta invalido")
