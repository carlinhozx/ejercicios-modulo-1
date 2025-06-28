print("Vamos a verificar si un numeros es mayor que los otros dos  ")
rango_a=int(input("ingrese el primer numero para determinar: "))
rango_b=int(input("ingrese el segundo numero para determinar: "))
rango_c=int(input("ingrese el tercer numero para determinar: "))

if rango_a>rango_b>rango_c:
    print(f"{rango_a} es mayor que  {rango_b} y, {rango_b} es mayor que {rango_c}")
else:
    print(f" no es mayor que alguno de los numeros ingresados")

