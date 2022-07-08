var primera = "Azucar";
var segunda = " Leche";
var tercera = " Huevos";
var cuarta = " Arina";
var quinta = " Chocolate";
var Receta = " Pancakes";
Listado = [];
c = 0


function Ingredientes (x){
    Listado[c] = x;
    c = c + 1;
    return Listado;
}

Ingredientes(primera);
Ingredientes(segunda);
Ingredientes(tercera);
Ingredientes(cuarta);
Ingredientes(quinta);

console.log(Listado);

console.log(`Mi primera receta ${Receta}, con los siguientes ingredientes: ${Listado} `);
