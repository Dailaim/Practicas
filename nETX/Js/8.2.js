function GestionarEstudiante (estudiante,nota1,nota2, Gestion){
       var resGestion = Gestion(nota1,nota2);
       console.log (`Nombre Completo del Estudiante: ${estudiante} ${resGestion}`);

}
function Promedio (nota1,nota2){
       return (nota1+nota2)/2;
} 

GestionarEstudiante('Jose Carrillo', 18,20, Promedio);
