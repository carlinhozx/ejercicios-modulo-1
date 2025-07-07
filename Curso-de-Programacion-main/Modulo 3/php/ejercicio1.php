<?php
$numero1 = 1;
$numero2 = 20;

$suma = $numero1+$numero2;
$resta = $numero1-$numero2;
$multiplicacion = $numero1*$numero2;
$division = $numero1/$numero2;
$modulo = $numero1%$numero2;

echo'Resultado de la suma: '.$suma."\n";
echo'Resultado de la resta: '.$resta."\n" ;
echo'Resultado de la multiplicacion: '.$multiplicacion."\n" ;
echo'Resultado de la division: '.$division."\n" ;
echo'Resultado de la modulo: '.$modulo."\n" ;

echo"Como desea pagar.\n";

$tipo_depago = "tarjeta";

switch ($tipo_depago) {
    case "efectivo":
        echo "Pago en efectivo.\n";
        break; 

    case "tarjeta":
        echo "Pago con tarjeta. \n";
        break;

    case "transferencia":
        echo "Pago por transferencia \n";
        break;
        
    case "Divisas (USD)":
        echo "Pago con Divisas. \n";
        break;

    default:
        // El bloque 'default' es opcional y se ejecuta si ningún 'case' coincide.
        echo "Método de pago no válido o no seleccionado.\n";
        break;
}

?>