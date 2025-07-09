// Online C++ compiler to run C++ program online
#include <iostream>

int main() {
    // Write C++ code here
    std::cout << "¡Hola, Mundo!" << std::endl;
    
    int entero = 10;
    float decimal=0.5;
    bool verda =true;
    char letra = 'C';
    
    std::cout << "Valor del entero: " << entero << std::endl;
    std::cout << "Valor del decimal: " << decimal << std::endl;
    std::cout << "Valor del caracter: " << letra << std::endl;
    std::cout << "Valor del booleano: " << verda << std::endl;
    
    double num1, num2,suma,resta,multiplicacion;
    float division, modulo;
    
    
    std::cout << "vamos a realizar calclulos" << std::endl;
    std::cout << "ingrese el primer numero: ";
    std::cin >> num1;
    
    std::cout << "ingrese el segundo numero: ";
    std::cin >> num2;
    suma=num1+num2;
    resta=num1-num2;
    multiplicacion=num1*num2;
    division=num1/num2;

    std::cout << "Valor de la suma: " << suma << std::endl;
    std::cout << "Valor de la resta: " << resta << std::endl;
    std::cout << "Valor de la multiplicacion: " << multiplicacion << std::endl;
    std::cout << "Valor del division: " << division << std::endl;
    
     int edad;
     std::cout << "ingrese su edad: ";
     std::cin >> edad;
    
    if (edad >= 18) {
        
        std::cout << "Eres mayor de edad." << std::endl;
    }
    else {
        std::cout << "menor"<< std::endl;
    }
    int multi;
    
    std::cout << "vamos a multiplicar ingrese un numero: ";
     std::cin >> multi;
    
    for (int i = 1; i<  11; i++) {
        std::cout <<i<<"x"<<multi<<"="<< i*multi << std::endl;
    }
    #include <iostream>

int main() {
    int numeroSecreto = 7;
    int intento;
    
    std::cout << "Bienvenido al juego de adivinanza!\n";
    std::cout << "Intenta adivinar el numero secreto (entre 1 y 100" << std::endl;
    
    do {
        std::cout << "Ingresa tu intento: ";
        std::cin >> intento;
        
        if (intento < numeroSecreto) {
            std::cout << "el numero secreto es mas  alto!\n";
        } 
        else if (intento > numeroSecreto) 
        {
            std::cout << "el numero secreto es mas bajo!\n";
        }
        
    }
    while (intento!=numeroSecreto);
    std::cout << "Felicidades! Adivinaste el numero secreto.\n";
}
    return 0;
}

#include <iostream>

int main() {
    int opcion;
    
    do {
        std::cout << "Menu Principal "<< std::endl;
        std::cout << "1. Saludar"<< std::endl;
        std::cout << "2. Despedirse"<< std::endl;
        std::cout << "3. Salir"<< std::endl;
        std::cout << "Seleccione una opcion: "<< std::endl;
        std::cin >> opcion;
        
        switch(opcion) {
            case 1:
                std::cout << "hola usuario " << std::endl;
                break;
            case 2:
                std::cout << "Despedir " << std::endl;
                break;
            case 3:
                std::cout << "saliendo... " <<std::endl;
                break;
            default:
                std::cout << "Opcion no valida. Por favor, seleccione 1, 2 o 3.";
        }
    } while (opcion != 3);
    
    return 0;
}
#include <iostream>


float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura;
    
    std::cout << "CALCULADORA DE AREA DE RECTANGULO"<<std::endl;
    std::cout << "Ingrese la base del rectangulo: "<<std::endl;
    std::cin >> base;
    std::cout << "Ingrese la altura del rectangulo: "<<std::endl;
    std::cin >> altura;
    
    
    float area = calcularAreaRectangulo(base, altura);
    std::cout << "El area del rectangulo es: " << area << std::endl;
    
    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}

#include <iostream>


void modificarPorValor(int numero);
void modificarPorReferencia(int &numero);

int main() {
    int numero;
    
    std::cout << "Valor inicial de numero: ";
    std::cin >> numero;
    
    modificarPorValor(numero);
    std::cout << "Despues de modificarPorValor: " << numero << std::endl;
    
    modificarPorReferencia(numero);
    std::cout << "Despues de modificarPorReferencia: " << numero << std::endl;
    
    return 0;
}


void modificarPorValor(int numero) {
    numero += 10; 
}


void modificarPorReferencia(int &numero) {
    numero += 10; 
}

#include <iostream>
#include <vector>
#include <string>

int main() {
    const int NUM_COMIDAS = 3;  
    std::vector<std::string> comidasFavoritas;
    comidasFavoritas.reserve(NUM_COMIDAS);
    
    std::cout << "Por favor, introduce tus " << NUM_COMIDAS << " comidas favoritas."<< std::endl;


    for (int i = 0; i < NUM_COMIDAS; ++i) {
        std::string comida;
        std::cout << "Comida " << i + 1 << ": ";
        std::getline(std::cin >> std::ws, comida);
        comidasFavoritas.push_back(comida);
    }

    std::cout << "--- Tus comidas favoritas son ---"<<std::endl;
    
    for (const auto& comida : comidasFavoritas) {
        std::cout << "- " << comida <<std::endl; 
    }

    return 0;
}