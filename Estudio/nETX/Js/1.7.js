function totalMinutos (hora, minutos) {
    return (hora * 60) + minutos;
}
console.log(totalMinutos(0, 15));

function cantidadRecolectadaSimple (cantidad, tiempo) {
    return cantidad * tiempo;
}
console.log(cantidadRecolectadaSimple(10, 5));

function cantidadRecolectada (costoEstudiante, costoAdulto, cantidadEstudiantes, cantidadAdultos) {
    return costoAdulto * cantidadAdultos + costoEstudiante * cantidadEstudiantes;
}
console.log(cantidadRecolectada(1, 5, 20, 4));

