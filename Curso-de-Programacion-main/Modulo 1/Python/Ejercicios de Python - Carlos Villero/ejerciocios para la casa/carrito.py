print("Bienvenido a Super Market El del Carrito")
producto=[]
precio=[]
cantidad=[]
print("Elija una de las siguientes opciones:")
while True:
    print("1. AGREGAR producto")
    print("2. VER carro")
    print("3. ELIMINAR producto")
    print("4. CAlCULAR total")
    print("5. SALIR")

    opcion = input("Ingrese su opción: ")

    if (opcion =="AGREGAR") or (opcion=="Agregar") or (opcion=="agregar") or (opcion == "1"):
        agregar_producto=input("Ingrese el nombre del producto: ").strip().capitalize()
        agregar_precio=float(input("Ingrese el precio del producto: "))
        while agregar_precio <= 0:
            print("El precio debe ser mayor que cero. Inténtelo de nuevo.")
            agregar_precio = float(input("Ingrese el precio del producto: "))
        agregar_cantidad=int(input("Ingrese la cantidad del producto: "))
        while agregar_cantidad <= 0:
            print("La cantidad debe ser mayor que cero. Inténtelo de nuevo.")
            agregar_cantidad = int(input("Ingrese la cantidad del producto: "))
        producto.append(agregar_producto)
        precio.append(agregar_precio)
        cantidad.append(agregar_cantidad)
        print(f"{producto} ha sido agregado al carro.\n")
    elif (opcion =="VER") or (opcion=="Ver") or (opcion=="ver") or (opcion == "2"):
        if len(producto)==0:
            print("El Carrito esta Vacio")
        else:
            print("Los productos en el carro son:")
            for i in range(len(producto)):
                print(f"{i+1}. {producto[i]} -> precio unitario: ${precio[i]} -> cantidad: {cantidad[i]} -> total: ${precio[i] * cantidad[i]}\n")
    elif (opcion =="ELIMINAR") or (opcion=="Eliminar") or (opcion=="eliminar") or (opcion == "3"):
        if len(producto)==0:
            print("El Carrito esta Vacio")
        else:
            numero = int(input("¿Qué producto desea eliminar? (Ingrese el número): ")) - 1
            if 0 <= numero < len(producto):
                eliminado = producto.pop(numero)
                precio.pop(numero)
                print(f"{eliminado} ha sido eliminado del carrito.\n")
            else:
                print("Número de producto no válido.")
    elif (opcion =="CALCULAR") or (opcion=="Calcular") or (opcion=="calcular") or (opcion == "4"):
        if len(precio) == 0:
            print("El Carrito esta Vacio")
        else:
            print("Los productos en el carro son:")
            for i in range(len(producto)):
                print(f"{i+1}. {producto[i]} -> precio unitario: ${precio[i]} -> cantidad: {cantidad[i]} -> total: ${precio[i] * cantidad[i]}\n")    
            total = sum(precio[i] * cantidad[i] for i in range(len(precio)))
            print(f"El total de los productos en el carrito es: ${total}\n")
    elif (opcion =="SALIR") or (opcion=="Salir") or (opcion=="salir") or (opcion == "5"):
        print("Gracias por su compra, vuelva pronto!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")