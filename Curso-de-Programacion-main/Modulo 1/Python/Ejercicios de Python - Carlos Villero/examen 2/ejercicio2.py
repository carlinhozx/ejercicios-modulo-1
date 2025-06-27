numeros = [15, 22, -8, 0, 10, -3]
suma=0
for numeros in numeros:
   if numeros >0:
        print(f"numero encontrado: {numeros}")
        suma+=numeros
        print(f"La suma de los numeros es: {suma}")
   elif numeros==0:
    print(f"Numero {numeros} encontrado")
    break