secreto=7
adivino=0
vida=5
while adivino != secreto:
    adivino=int(input("Intenta adivinar el numero secreto: "))
    if vida >0:
        if adivino>secreto:
            print(f"el numero secreto es menor que: {adivino} ")
            vida-=1
            print(f"te quedan {vida} intetos ")
        else:
            print(f"el numero secreto es mayor que: {adivino}")
            vida-=1
            print(f"te quedan {vida} intentos ")
    else:
        print("Te has quedado sin intentos")
print("Felicidades adivinaste el numero secreto ")
#