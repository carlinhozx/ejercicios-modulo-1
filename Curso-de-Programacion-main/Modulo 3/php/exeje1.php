<?php
//Escribe un script que cuente y muestre la cantidad de números pares e impares que hay en el rango del 1 al 50.

for ($i = 1; $i <= 50; $i++) {
    if ($i%2==0){
        echo "El numero ".$i." es par\n";
    }
    else{
        echo "El numero ".$i." es impar\n";
    }
}

//Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del número 8, desde el 8x1 hasta el 8x10.

for ($i = 1; $i <= 10; $i++) {

    echo "8 x ".$i."= ". (8*$i)."\n";
    
    
}
//Escribe un script que calcule la suma de todos los números impares desde el 1 hasta el 100.
$sumatoria=0;
for ($i = 1; $i <= 100; $i++) {

     if ($i%2!=0){
        echo "El numero ".$i." es Impar\n";
        $sumatoria+=$i;
        echo "la sumatoria es: ".$sumatoria."\n";
    }
    
}

//Crea un programa que verifique si una persona puede obtener una licencia de conducir. La condición es que debe tener al menos 18 años y no más de 65 años. Define una variable para la edad y muestra si cumple los requisitos o no.

$edad=18;

if ($edad>=18){
    echo "puedes obtener tu licencia conducir";
}
else {
    echo "aun eres muy joven para conducir";
}
//Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero y muestre el resultado.


if($edad>0){
    echo"el numero es positivo";
}
else if($edad<0){
    echo"el numero es negativo";
}
else{
    echo"el numero es Cero";
}

//Escribe un programa que imprima los números del 1 al 30. Para los múltiplos de 3, debe imprimir "Mar" en su lugar. Para los múltiplos de 5, debe imprimir "Tierra". Para los múltiplos de ambos (3 y 5), debe imprimir "MarTierra".

for ($i = 1; $i <= 30; $i++) {
     if(($i%5==0) & ($i%3==0)){
        echo "Mar y Tierra\n";
    }
    else if ($i%3==0){
        echo "Mar\n";
    }
    else if($i%5==0){
        echo "tierra\n";
    }
   
}
//Crea un script que, dada una variable numérica que representa la temperatura en grados Celsius, muestre un mensaje diferente si la temperatura es "fría" (menos de 10°C), "templada" (entre 10°C y 25°C) o "calurosa" (más de 25°C).
$temp=10;
if($temp<=10){
    echo"hay Frio";
}
else if(($temp>10) && ($temp<25)){
    echo"templado";
}
else if($temp>25){
    echo"calor";
}
//Escribe un programa que realice una cuenta regresiva para Año Nuevo desde el 10 hasta el 1. Al final, debe mostrar el mensaje "¡Feliz Año Nuevo!".
for ($i = 11; $i >= 0; $i--) {

    echo "$i...\n";
    
    
}
echo "Feliz Año nuevo";
?>