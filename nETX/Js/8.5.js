
var eventos = [
    {
        nombre: "e1",
        fecha: new Date(2018,3,20)
    },
    {
        nombre: "e2",
        fecha: new Date(2018,2,20)
    },
    {
        nombre: "e3",
        fecha: new Date(2018,3,10)
    },
    {
        nombre: "e4",
        fecha: new Date(2018,5,20)
    },
    {
        nombre: "e5",
        fecha: new Date(2018,6,20)
    },
    {
        nombre: "e6",
        fecha: new Date(2018,0,20)
    },
    {
        nombre: "e7",
        fecha: new Date(2018,8,20)
    },
]

function organizarEventos(eventos, fechaReferencia){
    var futuros = eventos.filter(x => x.fecha.getTime() > fechaReferencia.getTime())
    var pasados = eventos.filter(x => x.fecha.getTime() <= fechaReferencia.getTime())
    futuros = futuros.sort((a,b)=>{
        if (a.fecha.getTime() > b.fecha.getTime()){
            return 1;
        }
        if (a.fecha.getTime() < b.fecha.getTime()){
            return -1;
        }
        return 0;
    })
pasados = pasados.sort((a,b)=>{
    if (a.fecha.getTime() > b.fecha.getTime()){
        return -1;
    }
    if (a.fecha.getTime() < b.fecha.getTime()){
        return 1;
    }
    return 0;
})

return [futuros,pasados];
}
var resultado = organizarEventos(eventos, new Date(2018, 3, 21));
console.log(resultado[0]);
console.log(resultado[1]);