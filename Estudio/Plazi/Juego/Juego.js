var Jugador = 0
var pc = 0
alert("Este es el juego de Piedra, papel o Tijeras.")
alert("Para jugar tienes que escojer entre Piedra, Papel o Tijeras")
Jugador = prompt("Escoje Piedra es 1, Papel es 2 y Tijeras es 3:")

function aleatorio(min, max){
    return Math.floor(Math.random() * (max-min+1) + min)
}

function Elecion(numero){
    if(numero == 1){
        return "Piedra"
    }else if(numero == 2){
        return "Papel"
    }else if(numero == 3){
        return "Tijera"
    }else{
        return "Perder"
    }
}

function ganador(n1,n2){
    if(n1==n2){
    return "Un empate"}
else if((n1 == 1 || n2 == 1)&&(n1 == 2 || n2 == 2)){
    if (n1==2){
        return  "Ganas Tu"
    }
    return "La computadora gana"
}else if((n1 == 2 || n2 == 2)&&(n1 == 3 || n2 == 3)){
    if (n1==3){
        return  "Ganas Tu"
    }
    return "La computadora gana"
}else if((n1 == 3 || n2 == 3)&&(n1 == 1 || n2 == 1)){
    if (n1==1){
        return  "Ganas Tu"
    }
    return "La computadora gana"
}else{
    return "Escojiste perder y La computadora gana"
}
}
pc = aleatorio(1,3)
alert(`Tu escojiste ${Elecion(Jugador)} Y la Computadora ${Elecion(pc)}`)
alert(`El Resultado es: ${ganador(Jugador,pc)}`)