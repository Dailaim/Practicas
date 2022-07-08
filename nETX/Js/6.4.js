


class Actividad{
    constructor(identificador,tipo,version){
        this.Identificador = identificador;
        this.Tipo = tipo;
        this.Version = version;
    };
    Ac(){
        return `COMP18S_${this.Identificador}_${this.Tipo}_${this.Version}.midoc`
    }
    
}

a1 = new Actividad(1,"interactiva","V1").Ac()
a2 = new Actividad(2,"ejercicio","V2").Ac()
a3 = new Actividad(3,"laboratorio","V1").Ac()

var actividades = [a1,a2,a3]

for (i in actividades){
    console.log(actividades[i])

}


console.log(a1)