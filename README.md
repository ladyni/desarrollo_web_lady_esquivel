Tarea 2 Desarrollo Web
Incluye archivos html, css, javascript e imagenes con derechos de autor de gettyimages

# Tarea 2 - Desarrollo Web

Se incluye funcionalidades para gestionar actividades, visualizar estadísticas y trabajar con formularios dinámicos. El proyecto utiliza tecnologías como HTML, CSS, JavaScript y Python (Flask) para su implementación.

## Funcionalidades

### **Agregar Actividad**
- Despliega un formulario con secciones para agregar los datos requeridos de una actividad:
  - Información básica: región, comuna, sector, nombre del organizador, correo electrónico, etc.
  - Fechas y horarios: inicio y término de la actividad.
  - Temas: permite seleccionar entre varios temas predefinidos o agregar un tema personalizado.
  - Fotos: incluye un botón para subir fotos de la actividad (actualmente, el botón para agregar múltiples fotos no está implementado).
- Los datos ingresados son validados antes de ser enviados al servidor.

### **Ver Listado**
- Muestra un listado de las actividades subidas, incluyendo:
  - Fecha y hora de inicio y término.
  - Comuna y sector donde se realizará la actividad.
  - Temas asociados a la actividad.
  - Una foto representativa de la actividad (si está disponible).
- Permite visualizar los detalles de cada actividad al hacer clic en una fila del listado.

### **Estadísticas**
- Genera tres gráficos utilizando `matplotlib` para mostrar estadísticas relacionadas con las actividades:
  - Distribución de actividades por comuna.
  - Temas más populares.
  - Cantidad de actividades por rango de fechas.
- Los gráficos son generados dinámicamente y se basan en datos inventados para cumplir con los requisitos de la tarea.

## Requisitos del Proyecto

Este proyecto requiere un entorno virtual configurado con las librerías necesarias para su correcto funcionamiento. A continuación, se detallan los pasos para instalar y configurar el entorno:

### Instalación del Entorno Virtual
1. Crea un entorno virtual en el directorio del proyecto:
   ```bash
   python3 -m venv venv
   source flak_app/venv/bin/activate
   Flask run