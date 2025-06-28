print("vamos a calcular el descuento de un poducto")
while True:
    precio_original=int(input("Ingrese el precio original del producto: "))
    descuento=int(input("Ingrese el descuento del producto (solo el numero): "))
    descuento_porcentual=descuento/100
    descuento_antes=precio_original*descuento_porcentual
    descuento_final=precio_original-descuento_antes
    print(f"el producto tiene un descuento de: {descuento_antes} $")
    print(f"el precio final es de: {descuento_final} $")
    