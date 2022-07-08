var deporte = {
    nombre : "Judo",
    origen: "Japon"
}


var clubes = {
    
    dojo : ["Sensei VU", "Sensei Sato"],
    ciudad : [
        "Inmaculada",
        "Tokio"]
    
}


function decre (c2){
    return `Club de ${deporte.nombre} ${clubes.dojo[c2]}, Ciudad: ${clubes.ciudad[c2]}`

}

console.log(decre(1))
 