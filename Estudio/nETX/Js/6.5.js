class Evento{
    constructor(id, nombre, cantidadAsistentes, precioPorAsistente){
    this.Id = id
    this.Nombre = nombre
    this.CantidadAsistentes = cantidadAsistentes
    this.PrecioPorAsistente = precioPorAsistente
    }

    enlace(){
        return `/evento/${this.Id}`
    }

    dineroTotalRecaudado(){
        return this.CantidadAsistentes * this.PrecioPorAsistente
    }
}

var evento1 = new Evento(1,"e1", 12, 5);
console.log(evento1.enlace())
console.log(evento1.dineroTotalRecaudado())