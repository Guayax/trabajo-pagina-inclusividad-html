nombreImagenes =[];
linkImagenesGaleria = "trabajo pagina inclusividad html/backend/data/ListaImagenes.json";

function ImportarJson(link){
    fetch(link)
        .then(Response => Response.json())
        .then(lista=> {
            nombreImagenes = lista;
        })
        .catch(error => {
            console.log("Ocurrio un error al importar el nombre de las imagenes")
        })
}

function RellenarGaleria(){
    
}
ImportarJson(linkImagenesGaleria);
console.log(nombreImagenes)
