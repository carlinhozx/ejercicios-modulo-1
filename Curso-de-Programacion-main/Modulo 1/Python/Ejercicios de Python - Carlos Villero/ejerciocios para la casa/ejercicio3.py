print("Vamos a comparar dos numeros")
while True:
    numero1 = int(input("Por favor, coloca el primer numero: "))
    numero2 = int(input("Por favor, coloca el segundo numero: "))

    if numero1 > numero2:
        print("El primer numero es mayor que el segundo")
    elif numero1 < numero2:
        print("El segundo numero es mayor que el primero")
    else:        
        print("Los numeros son iguales")