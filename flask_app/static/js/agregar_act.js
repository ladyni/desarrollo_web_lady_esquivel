// Obtener los elementos del formulario
const inicioInput = document.getElementById('inicio');
const terminoInput = document.getElementById('termino');
const emailInput = document.getElementById('email');
const phoneInput = document.getElementById('phone');
const temaSelect = document.getElementById('tema');
const temaOtroContainer = document.getElementById('tema-otro-container');
const temaOtroInput = document.getElementById('tema-otro');
const form = document.querySelector('form');

// Prellenar fecha y hora de inicio
const now = new Date();
const isoString = now.toISOString().slice(0, 16); // Formato: "YYYY-MM-DDTHH:mm"
inicioInput.value = isoString;

// Prellenar fecha y hora de término (+3 horas)
const threeHoursLater = new Date(now.getTime() + 3 * 60 * 60 * 1000).toISOString().slice(0, 16);
terminoInput.value = threeHoursLater;

// Mostrar input de "Otro" tema si se selecciona "Otro"
temaSelect.addEventListener('change', function () {
    if (temaSelect.value === 'otro') {
        temaOtroContainer.style.display = 'block';
    } else {
        temaOtroContainer.style.display = 'none';
        temaOtroInput.value = ''; // Limpiar el campo si no es "Otro"
    }
});

//Validaciones
form.addEventListener('submit', function (event) {
    let isValid = true;

    //email
    if (!emailInput.value || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
        alert('Por favor, ingrese un email válido.');
        isValid = false;
    }

    // telefono
    if (phoneInput.value && !/^\+\d{3}\.\d{8}$/.test(phoneInput.value)) {
        alert('Por favor, ingrese un número de teléfono válido en el formato +NNN.NNNNNNNN.');
        isValid = false;
    }

    //
    if (temaSelect.value === 'otro' && (temaOtroInput.value.length < 3 || temaOtroInput.value.length > 15)) {
        alert('Por favor, especifique un tema válido (entre 3 y 15 caracteres).');
        isValid = false;
    }

    
    if (terminoInput.value && new Date(terminoInput.value) <= new Date(inicioInput.value)) {
        alert('La fecha y hora de término debe ser mayor a la de inicio.');
        isValid = false;
    }
    if (fotoInput.files.length < 1 || fotoInput.files.length > 5) {
        alert('Por favor, suba entre 1 y 5 fotos.');
        isValid = false;
    }

    if (!isValid) {
        event.preventDefault();
    }
});
// Obtener los elementos de los menús desplegables
const regionSelect = document.getElementById('region');
const comunaSelect = document.getElementById('comuna');

// Cargar las regiones en el menú desplegable
function cargarRegiones() {
    region_comuna.regiones.forEach(region => {
        const option = document.createElement('option');
        option.value = region.numero;
        option.textContent = region.nombre;
        regionSelect.appendChild(option);
    });
}

// Cargar las comunas correspondientes a la región seleccionada
function cargarComunas(regionNumero) {
    // Limpiar las comunas actuales
    comunaSelect.innerHTML = '<option value="">Seleccione Comuna</option>';

    // Buscar la región seleccionada
    const region = region_comuna.regiones.find(r => r.numero == regionNumero);
    if (region) {
        region.comunas.forEach(comuna => {
            const option = document.createElement('option');
            option.value = comuna.id;
            option.textContent = comuna.nombre;
            comunaSelect.appendChild(option);
        });
    }
}

// Evento para cargar las comunas cuando se selecciona una región
regionSelect.addEventListener('change', function () {
    cargarComunas(this.value);
});

// Inicializar el formulario cargando las regiones
cargarRegiones();