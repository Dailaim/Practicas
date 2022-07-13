var donaciones = [5,15,22,25,30,52,5,1,0];
function minimo(donaciones){
    var minimo = donaciones[0];
    for (i of donaciones){
        if (i < minimo){
            minimo = i;
        }
    }
    return minimo;
}
var min = minimo(donaciones);
console.log("El minimo es: " + minimo(donaciones)); 

function maximo(donaciones){
    var maximo = donaciones[0];
    for (i of donaciones){
        if (i > maximo){
            maximo = i;
        }
    }
    return maximo;
}

var max = maximo(donaciones);
console.log("El maximo es: " + max);

function promedio(donaciones){
    var suma = 0;
    for (i of donaciones){
        suma += i;
    }
    suma = suma - min - max
    return suma/ (-2 + donaciones.length);
}
console.log("El promedio es: " + promedio(donaciones));