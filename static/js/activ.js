document.addEventListener("DOMContentLoaded", function() {
    const actividades = [
      {
        titulo: "Natación en Providencia",
        inicio: "2025/05/15 10:15",
        termino: "2025/05/15 11:45",
        comuna: "Santiago",
        sector: "Providencia",
        tema: "Natación",
        organizador: "Organizador 1",
        fotos: ["../img/natacion.jpg"]
      },
      {
        titulo: "Escalada en Pudahuel",
        inicio: "2025/05/16 10:15",
        termino: "2025/05/16 11:45",
        comuna: "Santiago",
        sector: "Pudahuel",
        tema: "Escalada",
        organizador: "Organizador 2",
        fotos: ["../img/escalada.jpg"]
      },
      {
        titulo: "Karaoke en Sala Toqui",
        inicio: "2025/05/17 10:15",
        termino: "2025/05/17 11:45",
        comuna: "Santiago",
        sector: "Sala Toqui",
        tema: "Karaoke",
        organizador: "Organizador 3",
        fotos: ["../img/karaoke.jpg"]
      },
      {
        titulo: "Pintar en Ñuñoa",
        inicio: "2025/05/18 10:15",
        termino: "2025/05/18 11:45",
        comuna: "Santiago",
        sector: "Ñuñoa",
        tema: "Pintar",
        organizador: "Organizador 4",
        fotos: ["../img/pintar.jpg"]
      },
      {
        titulo: "Rollers en Las Condes",
        inicio: "2025/05/19 10:15",
        termino: "2025/05/19 11:45",
        comuna: "Santiago",
        sector: "Las Condes",
        tema: "Rollers",
        organizador: "Organizador 5",
        fotos: ["../img/rollers.jpg"]
      }
    ];
  
    const tablaActividades = document.getElementById("tablaActividades");
    const detalle = document.getElementById("detalle");
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modalImg");
    const contenedorFotos = document.getElementById("detalleFotos");
    const volverListadoBtn = document.getElementById("volverListado");
    const cerrarModalBtn = document.getElementById("cerrarModal");
  
    // Event listener para las filas de la tabla
    function agregarEventosFilas() {
      const filas = tablaActividades.querySelectorAll("tbody tr");
      filas.forEach((fila, index) => {
        fila.addEventListener("click", function() {
          mostrarDetalle(index);
        });
      });
    }
  
    // Event listener para las fotos en el detalle
    function agregarEventosFotos() {
      contenedorFotos.addEventListener("click", function(event) {
        if (event.target.tagName === "IMG") {
          ampliarImagen(event.target.src); // Al hacer clic, muestra la imagen en tamaño completo
        }
      });
    }
  
    // Event listener para volver al listado
    function agregarEventoVolverListado() {
      volverListadoBtn.addEventListener("click", volverListado);
    }
  
    // Event listener para cerrar el modal
    function agregarEventoCerrarModal() {
      cerrarModalBtn.addEventListener("click", cerrarModal);
    }
  
    // Mostrar detalle de actividad
    function mostrarDetalle(index) {
      const act = actividades[index];
  
      // Cambiar la vista a detalle
      document.getElementById("tablaActividades").classList.add("hidden");
      detalle.classList.remove("hidden");
  
      // Rellenar los detalles de la actividad
      document.getElementById("tituloActividad").textContent = act.titulo;
      document.getElementById("detalleInicio").textContent = act.inicio;
      document.getElementById("detalleTermino").textContent = act.termino;
      document.getElementById("detalleComuna").textContent = act.comuna;
      document.getElementById("detalleSector").textContent = act.sector;
      document.getElementById("detalleTema").textContent = act.tema;
      document.getElementById("detalleOrganizador").textContent = act.organizador;
  
      // Mostrar las fotos en miniatura
      contenedorFotos.innerHTML = "";
      act.fotos.forEach(src => {
        const img = document.createElement("img");
        img.src = src;
        img.alt = "foto actividad";
        img.style.width = "320px";
        img.style.height = "240px";
        contenedorFotos.appendChild(img);
      });
  
      // Agregar eventos a las fotos
      agregarEventosFotos();
    }
  
    // Volver al listado de actividades
    function volverListado() {
      document.getElementById("tablaActividades").classList.remove("hidden");
      detalle.classList.add("hidden");
    }
  
    // Ampliar la imagen
    function ampliarImagen(src) {
      modalImg.src = src;
      modal.style.display = "flex";
    }
  
    // Cerrar el modal
    function cerrarModal() {
      modal.style.display = "none";
    }
  
    // Inicializar los event listeners
    agregarEventosFilas();
    agregarEventoVolverListado();
    agregarEventoCerrarModal();
  });


