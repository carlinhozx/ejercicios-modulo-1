// Variables globales para manejar el estado de la calculadora
let currentInput = '';       // Almacena la entrada actual del usuario
let previousInput = '';      // Almacena la entrada anterior para operaciones de dos valores
let currentOperation = null; // Guarda la operación actual (+, -, *, /, ^, etc.)

// Espera a que el DOM esté completamente cargado antes de ejecutar el código
document.addEventListener('DOMContentLoaded', () => {
    // Obtiene la referencia al elemento de la pantalla de la calculadora
    const screen = document.getElementById('screen');
    // Selecciona todos los botones dentro del contenedor .btns
    const buttons = document.querySelectorAll('.btns button');

    // Añade un event listener a cada botón
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // Obtiene el valor del atributo data-val (para números y operadores básicos)
            const val = button.getAttribute('data-val');
            // Obtiene el valor del atributo data-fn (para funciones especiales)
            const fn = button.getAttribute('data-fn');

            if (val) {
                // Si es un valor numérico/operador básico:
                currentInput += val;       // Agrega el valor a la entrada actual
                screen.value = currentInput; // Muestra la entrada actual en pantalla
            } else if (fn) {
                // Si es una función especial, llama a handleFunction
                handleFunction(fn, screen);
            }
        });
    });
});

/**
 * Maneja las funciones científicas y operaciones de la calculadora
 * @param {string} fn - Nombre de la función/operación a ejecutar
 * @param {HTMLInputElement} screen - Elemento de la pantalla de la calculadora
 */
function handleFunction(fn, screen) {
    // Convierte currentInput a número, o usa 0 si está vacío
    const value = currentInput ? parseFloat(currentInput) : 0;
    
    // Ejecuta diferentes acciones según la función solicitada
    switch (fn) {
        // Funciones trigonométricas (usan el valor actual)
        case 'sin':
            screen.value = Math.sin(value); // Calcula seno
            currentInput = screen.value;    // Actualiza currentInput con el resultado
            break;
        case 'cos':
            screen.value = Math.cos(value); // Calcula coseno
            currentInput = screen.value;
            break;
        case 'tan':
            screen.value = Math.tan(value); // Calcula tangente
            currentInput = screen.value;
            break;
        case 'log':
            screen.value = Math.log10(value); // Calcula logaritmo base 10
            currentInput = screen.value;
            break;

        // Operaciones de potencias y raíces
        case 'pow2':
            screen.value = Math.pow(value, 2); // Eleva al cuadrado
            currentInput = screen.value;
            break;
        case 'pow3':
            screen.value = Math.pow(value, 3); // Eleva al cubo
            currentInput = screen.value;
            break;
        case 'pow':
            // Prepara la operación de potencia (a^b):
            previousInput = currentInput;   // Guarda el primer número (base)
            currentInput = '';             // Resetea para recibir el segundo número (exponente)
            currentOperation = 'pow';      // Establece la operación actual
            screen.value = previousInput + '^'; // Muestra la base con el operador ^
            break;
        case 'sqrt':
            screen.value = Math.sqrt(value); // Raíz cuadrada
            currentInput = screen.value;
            break;
        case 'cbrt':
            screen.value = Math.cbrt(value); // Raíz cúbica
            currentInput = screen.value;
            break;

        // Operaciones de limpieza
        case 'clear':
            currentInput = '';          // Limpia entrada actual
            previousInput = '';         // Limpia entrada anterior
            currentOperation = null;    // Resetea operación
            screen.value = '';          // Limpia pantalla
            break;

        // Borrado de caracteres
        case 'del':
            currentInput = currentInput.slice(0, -1); // Elimina último carácter
            screen.value = currentInput; // Actualiza pantalla
            break;

        // Cálculo de resultado
        case 'equal':
            if (currentOperation === 'pow' && previousInput && currentInput) {
                // Caso especial para potencia (a^b):
                const base = parseFloat(previousInput);     // Obtiene base
                const exponent = parseFloat(currentInput);  // Obtiene exponente
                screen.value = Math.pow(base, exponent);   // Calcula potencia
                currentInput = screen.value;                // Actualiza currentInput
                currentOperation = null;                   // Resetea operación
                previousInput = '';                        // Limpia previousInput
            } else {
                // Para otras operaciones usa eval (cuidado con seguridad en producción)
                try {
                    screen.value = eval(screen.value); // Evalúa la expresión
                    currentInput = screen.value;        // Actualiza currentInput
                } catch {
                    screen.value = 'Error'; // Manejo de errores
                    currentInput = '';
                }
            }
            break;
    }
}