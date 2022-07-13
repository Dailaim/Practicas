var evento = {
    nombre: "Evento 1",
    descripcion: "Esto es una descripción",
    fecha: new Date(2018,10,1)
};

function stringValido(string, largo){

    if (string == null || string == undefined){
        return false;
        }
        
    if ( largo && string.trim().length < largo){
        return false;
        }
    return true
    }


function fechaValida(fecha,minimaFecha){

    if (fecha == null || fecha == undefined){
        return false;
        }
        
    if ( minimaFecha && fecha.getTime() < minimaFecha.getTime()){
        return false;
        }
    return true
    }

    function eventoValido(evento){

        if (evento == null || evento == undefined){
            return false;
            }
            
        return (
            stringValido(evento.nombre, 3) &&
            stringValido(evento.descripcion, 10) &&
            fechaValida(evento.fecha, new Date(2018,0,1,0,0,0))
            )
                
    }
console.log(eventoValido(evento));