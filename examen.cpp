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
    int secreto =7;
    int adivinar;
     std::cout << "vamos a adivinar el numero secreto: ";
     std::cin >> secreto;
    
    while (adivinar !=secreto) {
        std::cout << "Intenta de nuevo adivinar el numero secreto: ";
        std::cin >> adivinar;
        
        if (secreto>adivinar){
            std::cout << "el numero secreto es mayor " << std::endl;
        }
        else if (secreto<adivinar){
            std::cout << "el numero secreto es menor " << std::endl;
        }
    }
   
        std::cout << "adivinaste el numero secreto." << std::endl;
        
    
    return 0;
}
