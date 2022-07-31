let PlayerAttack
let EnemyAccion
let PetEnemy
let Resultado
let PetUse
let healPlayer = 20
let healEnemy = 20
let ban

function aleatorio(min, max){
    return Math.floor(Math.random() * (max-min+1) + min)
}

function iniciarjuego(){
    var BotonPetPlayer = document.getElementById("boton-pet")
    BotonPetPlayer.addEventListener("click",SelectMascota)
    let ButonAttack = document.getElementById("boton-rapido")
    ButonAttack.addEventListener("click", Attack)
    let ButonAttackHark = document.getElementById("boton-fuerte")
    ButonAttackHark.addEventListener("click", AttackHard)
    let ButonEscudo = document.getElementById("boton-escudo")
    ButonEscudo.addEventListener("click", escudo)
    let ButonEsquivar = document.getElementById("boton-esquivar")
    ButonEsquivar.addEventListener("click", esquivar)
}


function SelectMascota(){
    var SolarSword = document.getElementById("solar")
    var OceanSword = document.getElementById("ocean")
    var ForestSword = document.getElementById("forest")
    var MoonSword = document.getElementById("moon")
    var PosionSword = document.getElementById("posion")
    var DirtSword = document.getElementById("dirt")
    var swordUse = document.getElementById("sword-use")


    if(SolarSword.checked){
        PetUse = "Solar Sword"

    }else if(OceanSword.checked){
        PetUse = "Ocean Sword"

    }else if(ForestSword.checked){
        PetUse = "Forest Sword" 

    }else if(MoonSword.checked){
        PetUse = "Moon Sword"

    }else if(PosionSword.checked){
        PetUse = "Posion Sword"

    }else if(DirtSword.checked){
        PetUse = "Dirt Sword"

    }else {alert("Seleciona una mascota")}
    swordUse.innerHTML = PetUse

    SelectMascotaEnemy()
}


function SelectMascotaEnemy(){
    swordUseEnemy = document.getElementById("sword-enemy")
        let EnemySelec = aleatorio(1,3)
    if(EnemySelec == 1){
        PetEnemy = "Solar Sword"
    }else if(EnemySelec == 2){
        PetEnemy = "Ocean Sword"
    }else if(EnemySelec == 3){
        PetEnemy = "Forest Sword"
    }else if(EnemySelec == 4){
        PetEnemy = "Moon Sword"
    }else if(EnemySelec == 5){
        PetEnemy = "Posion Sword"
    }else if(EnemySelec == 6){
        PetEnemy = "Dirt Sword"
    }
    swordUseEnemy.innerHTML = PetEnemy
}



function Attack(){
    PlayerAttack = "Ataque Rapido"
    EnemyAttack()
}
function AttackHard(){
    PlayerAttack ="Ataque Fuerte"
    EnemyAttack()
}
function escudo(){
    PlayerAttack ="Escudo"
    EnemyAttack()
}
function esquivar(){
    PlayerAttack ="Esquivo"
    EnemyAttack()
}

function EnemyAttack(){
    EnemyAccionAleatorio = aleatorio(1,4)
    if(EnemyAccionAleatorio==1){
        EnemyAccion = "Ataque Rapido"
    }else if(EnemyAccionAleatorio==2){
        EnemyAccion ="Ataque Fuerte"
    }else if(EnemyAccionAleatorio==3){
        EnemyAccion ="Escudo"
    }else if(EnemyAccionAleatorio==4){
        EnemyAccion ="Esquivo"     
    }
    SayMensaje()
}




function SayMensaje(){
    let secionmensaje = document.getElementById("mensaje")
    let parrafo = document.createElement("p")

    if(parada()){
    parrafo.innerHTML = `Realizaste un ${PlayerAttack} y el enemigo un ${EnemyAccion} Y el resultado es ${ganador(PlayerAttack,EnemyAccion)}`
    secionmensaje.appendChild(parrafo)
    }else{
    parrafo.innerHTML = `Termino el juego`
    secionmensaje.appendChild(parrafo)
    }
}

function finiquito(c1){
    let vidasPlayer = document.getElementById("vidas-player")
    let vidasEnemy = document.getElementById("vidas-enemy")
    if(c1 == "empate"){
        return "Se que mirando como pendejos esperando a que el otro ataque"
    }else if(c1 == "desempate"){
        c1 = desempate(PetUse,PetEnemy)
    }
    if(c1 == "ganas"){
        healEnemy--
        vidasEnemy.innerHTML = healEnemy
        return "Ganas tu"
    }else{
        healPlayer --
        vidasPlayer.innerHTML = healPlayer
        return "Gana la computadora"
    }
    
}

function parada(){
    if(healPlayer == 0){
        alert("Te an derrotado")

        return ban = false

    }else if(healEnemy == 0){
        alert("Derrotaste a tu enemigo")

        return ban = false

    }else{
        return true
    }

}

function ganador(n1,n2){
    let crimen
    if(n1 == n2){
        if(n1 != "Escudo" && n1 != "Esquivo" ){
            crimen = "desempate"
        }
        else{
            crimen = "empate"
        }
    
}else if((n1 == "Ataque Rapido")&&(n2 == "Ataque Fuerte")){
    crimen = "ganas"
}else if((n1 == "Ataque Fuerte")&&(n2 == "Escudo")){
    crimen = "ganas"
}else if((n1 == "Escudo")&&(n2 == "Ataque Rapido")){
    return "El ataque es muy debil para romnper el escudo"
}else if((n1 == "Esquivo")&&(n2 == "Ataque Fuerte")){
    return "El ataque es muy lento y se logra esquivar"
}else if((n1 || n2 == "Ataque Rapido")&&(n2 || n1 == "Esquivo")){
    crimen = "ganas"
}else if((n1== "Esquivo"||n2 == "Esquivo")&&(n1== "Escudo"||n2 == "Escudo")){
    crimen = "empate"
}


return finiquito(crimen)
}


function desempate(n1,n2){
    if(n1==n2){
    return "Un empate"}
else if((n1 == "Solar Sword" || n2 == "Solar Sword")&&(n1 == "Ocean Sword" || n2 == "Ocean Sword")){
    if (n1=="Ocean Sword"){
        return  "ganas"
    }
    return "La computadora gana"
}else if((n1 == "Ocean Sword" || n2 == "Ocean Sword")&&(n1 == "Forest Sword" || n2 == "Forest Sword")){
    if (n1=="Forest Sword"){
        return  "ganas"
    }
    return "La computadora gana"
}else if((n1 == "Forest Sword" || n2 == "Forest Sword")&&(n1 == "Solar Sword" || n2 == "Solar Sword")){
    if (n1=="Solar Sword"){
        return  "ganas"
    }
    return "La computadora gana"
}
}


//window.addEventListener("load",iniciarjuego)