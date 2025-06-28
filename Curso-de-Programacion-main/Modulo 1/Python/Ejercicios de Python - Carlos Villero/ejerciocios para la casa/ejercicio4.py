print("Vamos a comprobar si un año es bisiesto o no")
while True:
    
    año=int(input("Por favor, coloca un año: "))
    if (año %4==0 and año %100 !=0 ) or año%400==0 :
        print(f"el año {año} es bisiesto")
    else:
        print(f"el año {año} no es bisiesto")