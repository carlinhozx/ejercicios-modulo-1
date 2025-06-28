print("Vamos a ver cual es tu calificacion: ")
nota=int(input("ingrese su nota: "))

if 90<=nota<=100:
    print("tu calificacion es: A")
elif 80<=nota<90:
    print("tu calificacion es: B")
elif 70<=nota<80:
    print("tu calificacion es: C")
elif 60<=nota<70:
    print("tu calificacion es: D")
else:
    print("tu calificacion es: F")