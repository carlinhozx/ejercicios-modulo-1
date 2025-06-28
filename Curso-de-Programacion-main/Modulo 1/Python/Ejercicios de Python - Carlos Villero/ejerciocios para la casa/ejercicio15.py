while True:
    valor=int(input("ingrese un numeropara comprobar que sea positivo, negativo o igual a 0: "))
    opcion=0
    if valor>0:
        print(f"El  numero {valor} es positivo ")
    elif valor==0:
        print(f"El  numero ingresado es igual a 0 ")
    else:
        print(f"El  numero {valor} es negativo ")
   