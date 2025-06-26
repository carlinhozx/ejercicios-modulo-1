print("Ejercicio 1")
dato = int(input("Ingrese un numero: "))

if dato > 0 :
    print(f"el numero {dato} es postivo.")
    if dato % 2 ==0:
        print(f"el numero {dato} es par.")
    else:
        print(f"el numero {dato} es impar.")
elif dato == 0 :
    print(f"el nuemro es = {dato}.")
else:
    print(f"el numero  {dato} es negativo")

print("ejercicio 2")

numeros = [15, 22, -8, 0, 10, -3]
suma=0
for numeros in numeros :
    if numeros >0 :
        print(f"numero encontrado {numeros}")
        
        suma += numeros 
        print(f"la suma de los numeros es:{suma} ")
    elif  numeros == 0:
            print(f"Número {0} encontrado, saliendo del bucle.")
            break
        
estudiantes = [('Ana', 85), ('Luis', 50), ('Carlos', 70), ('Marta', 92), ('Jorge', 45)]

secreto=7
usu=int(input("ingrese  un numero para ver si es el numero secreto:"))
vidas=5
while usu != secreto:
    if vidas>0:
        if usu>secreto:
            print("el numero ingresado es mayor que el numero secreto")
            print("Error inteta de nuevo: ")
            print(f"intentos restante: {vidas}")
            vidas=vidas-1
            usu=int(input("ingrese  un numero para ver si es el numero secreto:"))
            
        
        elif usu==secreto :
             print("numero secreto encontrado")    
        else: 
            print("el numero ingresado es menor que el numero secreto")
            print("Error inteta de nuevo: ")
            vidas=vidas-1
            print(f"intentos restante: {vidas}")
            usu=int(input("ingrese  un numero para ver si es el numero secreto:"))
            
    else:
        print("Sin vidas")


for dat in range(50):
    print(f"el numero es: {dat+1} ")
    if dat % 5 == 0:
        print("Multiplo de 5")
        continue


