// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {
    // Obtiene la pantalla y todos los botones
    const screen = document.getElementById('screen');
    const buttons = document.querySelectorAll('.btns button');

    // Añade un event listener a cada botón
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            // Obtiene el valor (data-val) o función (data-fn) del botón
            const val = button.getAttribute('data-val');
            const fn = button.getAttribute('data-fn');

            if (val) {
                // Si es un valor numérico/operador, lo añade a la pantalla
                screen.value += val;
            } else if (fn) {
                // Si es una función, llama a handleFunction
                handleFunction(fn, screen);
            }
        });
    });
});

// Maneja las funciones científicas y operaciones
function handleFunction(fn, screen) {
    const value = parseFloat(screen.value); // Convierte el valor a número
    
    switch (fn) {
        // Funciones trigonométricas y logaritmo
        case 'sin':
            screen.value = Math.sin(value);
            break;
        case 'cos':
            screen.value = Math.cos(value);
            break;
        case 'tan':
            screen.value = Math.tan(value);
            break;
        case 'log':
            screen.value = Math.log10(value);
            break;

        // Potencias y raíces
        case 'pow2':
            screen.value = Math.pow(value, 2);
            break;
        case 'pow3':
            screen.value = Math.pow(value, 3);
            break;
        case 'sqrt':
            screen.value = Math.sqrt(value);
            break;
        case 'cbrt':
            screen.value = Math.cbrt(value);
            break;

        // Limpiar pantalla
        case 'clear':
            screen.value = '';
            break;

        // Borrar último carácter
        case 'del':
            screen.value = screen.value.slice(0, -1);
            break;

        // Calcular resultado (evalúa la expresión)
        case 'equal':
            try {
                screen.value = eval(screen.value);
            } catch {
                screen.value = 'Error'; // Manejo de errores
            }
            break;
    }
}