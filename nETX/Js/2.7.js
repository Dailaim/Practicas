function encabezadoEvento (evento, lugar) {
    Cabeza = "Evento:" + " " + evento + " " + "Lugar:" + " " + lugar;
    return Cabeza;
}
console.log(encabezadoEvento("Cumpleaños", "Calle falsa 123"));

function limpiarNombreParticipante (nombre, apellido) {
    limpio = apellido.toUpperCase().trim() + ", " + nombre.toLowerCase().trim();
    return limpio;
}
console.log(limpiarNombreParticipante("juan", "perez"));
