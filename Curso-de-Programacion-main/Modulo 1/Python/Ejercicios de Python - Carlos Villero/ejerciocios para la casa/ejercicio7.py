print("Vamos a verificar si un numero esta ente un rango de numero")
rango_a=int(input("ingrese un numero para determinar un limite: "))
rango_b=int(input("ingrese otro numero para determinar un limite: "))
if rango_a==rango_b:
    print("los numero son iguales")

else:
    dato=int(input(f"veamos si este numero se encuentra en el rango de {rango_a} y {rango_b}:  "))
   
    if (rango_a<dato<rango_b) or (rango_b<dato<rango_a) :
        print(f"el numero {dato} se encuentra en el rango de valores! ")
    else:
        print(f"el numero {dato} no se encuentra en el rango de valores! ")

