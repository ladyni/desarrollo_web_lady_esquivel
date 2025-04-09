function openImageInNewWindow(imgElement) {
    const modal = document.getElementById("myModal");
    const modalImg = document.getElementById("img01");
    const captionText = document.getElementById("caption");

    // Mostrar el modal
    modal.style.display = "block";
    modalImg.src = imgElement.src;
    modalImg.style.width = "800px";
    modalImg.style.height = "600px";
    captionText.innerHTML = imgElement.alt;

    // Cerrar el modal al hacer clic en la "X"
    const closeBtn = document.getElementsByClassName("close")[0];
    closeBtn.onclick = function () {
        modal.style.display = "none";
    };
}

// Cerrar el modal al hacer clic fuera de la imagen
window.onclick = function (event) {
    const modal = document.getElementById("myModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

document.addEventListener("DOMContentLoaded", function () {
    const filas = document.querySelectorAll("table tr");
    const detalleActividad = document.getElementById("detalle-actividad");
    const volverListado = document.getElementById("volver-listado");

    filas.forEach((fila, index) => {
        if (index === 0) return; // Saltar la fila de encabezados
        fila.addEventListener("click", function () {
            const celdas = fila.querySelectorAll("td");
            document.getElementById("detalle-inicio").textContent = celdas[0].textContent;
            document.getElementById("detalle-termino").textContent = celdas[1].textContent;
            document.getElementById("detalle-comuna").textContent = celdas[2].textContent;
            document.getElementById("detalle-sector").textContent = celdas[3].textContent;
            document.getElementById("detalle-tema").textContent = celdas[4].textContent;
            document.getElementById("detalle-foto").src = celdas[5].querySelector("img").src;

            // Mostrar el contenedor de detalles y ocultar la tabla
            detalleActividad.style.display = "block";
            document.querySelector("table").style.display = "none";
        });
    });

    volverListado.addEventListener("click", function () {
        // Ocultar el contenedor de detalles y mostrar la tabla
        detalleActividad.style.display = "none";
        document.querySelector("table").style.display = "table";
    });
});