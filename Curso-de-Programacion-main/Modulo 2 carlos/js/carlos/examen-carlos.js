const nombreProducto = "Tablet 10 pulgadas";
let precio = 450.99;
let stock = 25;
const enviogratis = true

console.log(`Nombre del Producto: ${nombreProducto}`);
console.log(`Precio: $ ${precio}`);
console.log(`Stock disponible: ${stock}`);
console.log(`¿Tiene envio Gratis? : ${nombreProducto}`);

console.log(`Cliente compra dos laptos`);
let compra=2*precio;
console.log(`Sub-total :$ ${compra}`);
let impuesto=0.07
console.log(`Impuesto : ${impuesto*100}%`);
 let calculo= compra*impuesto
console.log(`Total : $ ${compra+calculo}`);

const edadusuario =20;

if(edadusuario>=18){
    console.log(`Puedes obtener tu licencia de conducir`);
}
else{
   console.log(`Aún no tienes la edad para obtener la licencia`); 
}

const colorsemaforo ="verde";

if(colorsemaforo=="verde"){
    console.log(`puedes avanzar`);
}
else if(colorsemaforo=="amarillo"){
    console.log(`baja la velocidad`);
}
else if(colorsemaforo=="rojo"){
    console.log(`detente`);
}
else{
    console.log(`color invalido`);
}

const diasemana= 3;

switch (diasemana) {
    case 1:
        console.log("Lunes: Lentejas");
        break; 
    case 2:
        console.log("Martes: Pollo al horno");
        break;
    case 3:
        console.log("Miércoles: Pescado a la plancha");
        break;
    case 4:
        console.log("Jueves: Pasta");
        break;
    case 5:
        console.log("Viernes: Paella");
        break;
    default: // Se ejecuta si ninguno de los casos anteriores coincide.
        console.log("Día no válido para menú.");
        break;
}

for (let i = 1; i <= 20; i++) {
    if((i%2)==0){
    console.log(`numero par: ${i}`);
    }
}

console.log("\nConteo Regresivo parael despegue");

let conteo =10;
const despegue= 0;
while (despegue <= conteo) {
    
    console.log(`Despegando en... ${conteo}`);
    conteo -= 1; // Aumentamos la cantidad descargada

    
    
}

for (let i = 1; i <= 50; i++) {
    if((i%3)==0){
    console.log(`fizz ${i}`);
    }
    else if((i%5)==0){
    console.log(`buzz ${i}`);
    }
    else if(((i%3)==0) & ((i%5)==0)){
    console.log(`FizzBuzz: ${i}`);
    }
}

let contador =0;
for (let j = 1; j <= 100; j++) {
    contador +=j;
    console.log(`numero: ${j}`);
    console.log(`sumatoria: ${contador}`);
    
    
    
    
}

