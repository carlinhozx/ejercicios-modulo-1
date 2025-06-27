opcion=1
while opcion !=0:
    
    valor=int(input("ingrese un numeropara comprobar que sea positivo, negativo o igual a 0: "))
    opcion=0
    if valor>0:
        print(f"El  numero {valor} es positivo ")
        if valor % 2==0:
            print("El numero es par")
        else:
            print("El numero es impar")
    elif valor==0:
        print(f"El  numero ingresado es igual a 0 ")
    else:
        print(f"El  numero {valor} es negativo ")
        if valor % 2==0:
            print("El numero es par")
        else:
            print("El numero es impar")