
var regular
function Telefono(Numero){
    
    regular2 = new RegExp('[0-9]*?[0-9]\-')
    console.log(regular2)
    valor2 = regular2.test(Numero)
    return valor2

    }
    

console.log(Telefono("14553535353-"))