var esIngeniero = true;
var tieneRecomendacion = false;
var tieneExperienciaLaboral = true;
if (!esIngeniero) {
	if (!tieneExperienciaLaboral) {
		console.log("Rechazado");
	}
	else {
		console.log("En estudio");
	}
}
else {
	if (tieneRecomendacion) {
		console.log("Admitido");
	}
	else {
		console.log("Admitido condicional");
	}
}