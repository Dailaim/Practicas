var arreglo1 = [1,2,3,4,5];
var arreglo2 = [1,2,4,8];

function doble (lista){
    var resultado = []
    for (i in lista){
    resultado.push(lista[i]*2)
    }
    return resultado
}
console.log(doble(arreglo1))
console.log(doble(arreglo2))

function impar (lista){
    impares = []
    for (i of lista){
        if(i%2==1){
            impares.push(i)
        }
    }
    return impares
}
console.log(impar(arreglo1))
console.log(impar(arreglo2))

function discriminate (lista){
    dis = []
    for (i of lista){
        if(i%2==0){
            dis.push(i/2)
        }
        else{
            dis.push(i*2)
        }
    }
    return dis
}
console.log(discriminate(arreglo1))
console.log(discriminate(arreglo2))