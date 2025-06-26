nombre = "carlos"
edad = 21
altura = 1.70
estudiante = True

#sumar
A = 10
B = 20
D= 12
E= 22
suma = A+B
divi =D/E
divi_ent =D//E
modulo = D%E
resta = A-B
multi= A*E
exp= A**E

print("El resultado de la operacion suma :",suma)
print("El resultado de la operacion div :",divi)
print("El resultado de la operacion div ent :",divi_ent)
print("El resultado de la operacion mod :",modulo)
print("El resultado de la operacion resta :",resta)
print("El resultado de la operacion exp :",exp)
print("El resultado de la operacion multi :",multi)

#concatenar texto

saludo = "hola"
mensaje = saludo + nombre
print(mensaje)

# operaciones logicas

es_adulto = edad > 18
print(es_adulto)

print(f"hola tengo",edad,"Años")
print(f"hola tengo {edad} Años")

print("ejercicio 1\n")

nom_ej1= "carlos"
edad_ej1= "21"
ciudad =("san francisco")

print(f"hola me llamo ¨{nom_ej1}, tengo {edad_ej1}, y soy de {ciudad}")

print("ejercicio 2 \n")
nota1= int(input("ingrese su nota 1"))
nota2= int(input("ingrese su nota 2"))
nota3= int(input("ingrese su nota 3"))

sumaej2=nota1+nota2+nota3
prom=sumaej2

print(f"hola {nom_ej1}")
print(f"tus notas son;{nota1}; {nota2} ;{nota3}")
print(f"tus promedio es {prom}")

#formmulario= input("cual es tu nombre\n")
#print(f"tu nombre es {formmulario}")

#formmulario_ent= int(input("cual es tu nombre\n"))
#print(f"tu edad es {formmulario_ent}")

#calcular = 21
#res_pract= formmulario_ent + calcular
#print(res_pract)

print("ejerccio 3\n")

#form_ej31=int(input("ingrerse un numero\n"))

#form_ej32=int(input("otro numero\n"))

#sumaej3= form_ej31 + form_ej32
#print(f"el resultado es de la suma es: {sumaej3} \n")

#resej3= form_ej31 - form_ej32
#print(f"el resultado es de la resta es: {resej3} ")

#multij3= form_ej31 * form_ej32
#print(f"el resultado es de la multiplicacion es: {multi}")

#divij3= form_ej31 / form_ej32
#print(f"el resultado es de la division es: {divij3}")

print("ejercio4\n")

#formej4=int(input("ingrese un numero para verificar si es par"))
#resej4=formej4%2
#print(f"el resutlado es: {resej4}")

print("ejercicon 5\n")


#form_ej5=int(input("ingrerse un numero\n"))
#form_ej51= form_ej5>10
#form_ej52= form_ej5<20
#resej5= form_ej51 and form_ej52
#print(resej5)

print("ejercicon 6\n")

if prom > 100:
    print("su calificacion es A")
elif prom > 90:
    print("su calificacion es B")
elif prom > 80:
    print("su calificacion es C")
elif prom > 70:
    print("su calificacion es D")
elif prom > 60:
    print("su calificacion es E")
else:
    print("su calificacion es F")
