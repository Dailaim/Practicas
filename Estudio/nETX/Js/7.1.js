var palabra;
var expresionRegular;

expresionRegular = /as/i

palabra = "pASa";

console.log(expresionRegular.test(palabra))

palabra = "al1"

expresionRegular = new RegExp('^[abc]l[0-9]')

var resultado = palabra.match(expresionRegular)
console.log(resultado)






