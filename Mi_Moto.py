print("Mi Primera Moto\n") 

nombre = input("Ingrese su Nombre: ").strip()
edad = input("Ingrese su Edad: ").strip()
Ahorros = 10000

# Definición de palabras clave
autobus = "autobus"
taxi = "taxi"
bicicleta = "bicicleta"
economica = "economica"
deportiva = "deportiva"
enduro = "enduro"
ciudad = "ciudad"
casa = "casa"
montaña = "montaña"
si_opcion = "si"
no_opcion = "no"

print("\n¡Comienza la aventura!") 
print(f"\nSoy {nombre.capitalize()}, tengo {edad} años, y hoy es el día más importante de mi vida: ¡por fin compraré mi primera moto!")
print(f"He ahorrado {Ahorros}$ con mucho esfuerzo. El concesionario está a 15 km, y debo llegar con el máximo dinero posible. ¿Cómo me transporto?\n")

print("OPCIONES DISPONIBLES:")
print(f"1. {autobus.upper()} urbano ($2): Es lento pero seguro")  
print(f"2. {taxi.upper()} ($15): Rápido, pero caro.")  
print(f"3. {bicicleta.upper()} prestada (Gratis): Ecológico y económico.")

seleccion1 = input("\n¿Cómo me voy? ").strip()

# Primera decisión
if seleccion1 == autobus.upper() or seleccion1 == autobus.lower() or seleccion1 == autobus.capitalize():
    Ahorros -= 2
    print(f"\nAl venir en {autobus.upper()} llegué más tarde de lo esperado, pero aquí estamos. Veamos qué nos dice el vendedor.")
    print("\nEs algo tarde, solo me quedan estas opciones:")
    print("OPCIONES DISPONIBLES:")
    print(f"1. Moto {economica.upper()} 9000$ (no tiene seguro ni garantía)")
    print(f"2. Moto {deportiva.upper()} 9800$ (con seguro y dos años de garantía)")
    
    seleccion2 = input("\n¿Cuál escoges? ").strip()
    
    if seleccion2 == economica.upper() or seleccion2 == economica.lower() or seleccion2 == economica.capitalize():
        Ahorros -= 9000
        print(f"\nEscogí la moto {economica.upper()}. Me quedan {Ahorros}$")
        print("\n¿A dónde puedo ir a estrenar la moto?")
        print("OPCIONES DISPONIBLES:")
        print(f"1. {ciudad.upper()} - Pasear a toda velocidad")
        print(f"2. {casa.upper()} - Reunir más dinero para la playa")
        
        seleccion3 = input("\n¿A dónde voy? ").strip()
        
        if seleccion3 == ciudad.upper() or seleccion3 == ciudad.lower() or seleccion3 == ciudad.capitalize():
            Ahorros = 0
            print(f"\nEn la {ciudad.upper()} se me vació un caucho y gasté todo lo que tenía para repararla y volver a casa.")
        elif seleccion3 == casa.upper() or seleccion3 == casa.lower() or seleccion3 == casa.capitalize():
            print(f"\nCon el viaje a {casa.upper()} también disfruté la moto y lo mejor es que me quedaron {Ahorros}$ para otra ocasión.")
        else:
            print("\nOpción no válida. Terminaste dando vueltas sin rumbo.")
            
    elif seleccion2 == deportiva.upper() or seleccion2 == deportiva.lower() or seleccion2 == deportiva.capitalize():
        Ahorros -= 9800
        print(f"\nPara probar la moto {deportiva.upper()} fui al cine y me gasté 150$")
        Ahorros -= 150
        print(f"\nAl llegar a casa me quedaron {Ahorros}$. ¡Fue un muy buen día con mi moto!")
    else:
        print("\nOpción no válida. Te vas sin comprar.")
        
elif seleccion1 == taxi.upper() or seleccion1 == taxi.lower() or seleccion1 == taxi.capitalize():
    Ahorros -= 15
    print(f"\nComo vinimos en {taxi.upper()}, llegamos temprano. Veamos qué hay disponible.")
    print("\nHas llegado temprano, tienes más opciones para escoger:")
    print("OPCIONES DISPONIBLES:")
    print(f"1. {deportiva.upper()} 9800$ (2 años seguro y garantía)")
    print(f"2. {enduro.upper()} 9985$ (3 años seguro y garantía)")
    print(f"3. {economica.upper()} 9000$ (sin seguro ni garantía)")
    
    seleccion2 = input("\n¿Cuál escoges? ").strip()
    
    if seleccion2 == deportiva.upper() or seleccion2 == deportiva.lower() or seleccion2 == deportiva.capitalize():
        Ahorros -= 9800
        print(f"\nPor fin me decidí por la moto {deportiva.upper()}")
        print("Fui a recorrer las calles a toda velocidad y me multaron por 200$")
        Ahorros -= 200
        print(f"\nAl llegar a casa me quedaron {Ahorros}$. ¡Qué gran día con mi moto deportiva!")
        
    elif seleccion2 == enduro.upper() or seleccion2 == enduro.lower() or seleccion2 == enduro.capitalize():
        Ahorros -= 9985
        print(f"\nEscogí la moto {enduro.upper()}. ¿Qué quieres hacer ahora?")
        print("OPCIONES DISPONIBLES:")
        print(f"1. {montaña.upper()} - Para una aventura")
        print(f"2. {casa.upper()} - Para descansar")
        
        seleccion3 = input("\n¿A dónde quieres ir? ").strip()
        
        if seleccion3 == montaña.upper() or seleccion3 == montaña.lower() or seleccion3 == montaña.capitalize():
            print(f"\nDecidí ir a una aventura en la {montaña.upper()} y gasté 300$")
            Ahorros -= 300
            print(f"\nAl final del día me quedaron {Ahorros}$. ¡Fue una experiencia increíble!")
        elif seleccion3 == casa.upper() or seleccion3 == casa.lower() or seleccion3 == casa.capitalize():
            print(f"\nFui directo a {casa.upper()} a descansar con mi nueva moto.")
            print(f"\nMe quedaron {Ahorros}$ para futuras aventuras.")
        else:
            print("\nOpción no válida. Terminaste perdido.")
            
    elif seleccion2 == economica.upper() or seleccion2 == economica.lower() or seleccion2 == economica.capitalize():
        Ahorros -= 9000
        print(f"\nEscogí la moto {economica.upper()}. Fui a hacer compras y gasté 100$")
        Ahorros -= 100
        print("De regreso la moto empezo a sonar raro por que me toco volver en taxi y enviar la moto al taller")
        Ahorros-=Ahorros
        print(f"\nAl llegar a casa no me quedo nada debi escoger otra")
    else:
        print("\nOpción no válida. Te vas sin comprar.")
        
elif seleccion1 == bicicleta.upper() or seleccion1 == bicicleta.lower() or seleccion1 == bicicleta.capitalize():
    print("\nLlegamos temprano pero muy sudados. El vendedor se burla de nosotros.")
    print(f"\nSolo te puedo ofrecer la moto {economica.upper()} 9000$ sin garantía")
    print("OPCIONES DISPONIBLES:")
    print(f"1. {si_opcion.upper()} - Comprar la moto")
    print(f"2. {no_opcion.upper()} - Rechazar la oferta")
    
    seleccion2 = input("\n¿Comprar la moto? ").strip()
    
    if seleccion2 == si_opcion.upper() or seleccion2 == si_opcion.lower() or seleccion2 == si_opcion.capitalize():
        Ahorros -= 9000
        print("\nEnviamos la bicicleta en un taxi y pagamos 30$")
        Ahorros -= 30
        print(f"\nVenir en {bicicleta.upper()} no fue la mejor opción. Estoy tan cansado que no quiero salir.")
        print(f"Me quedaron {Ahorros}$ para otra ocasión.")
    elif seleccion2 == no_opcion.upper() or seleccion2 == no_opcion.lower() or seleccion2 == no_opcion.capitalize():
        print("\nOtro día iré a otro concesionario donde no discriminen al cliente.")
    else:
        print("\Opcion no valida.nEl vendedor me ha echado por no poder decidir.")
else:
    print("\nOpción no válida. te quedaste en casa por decicirte por ninguna.")