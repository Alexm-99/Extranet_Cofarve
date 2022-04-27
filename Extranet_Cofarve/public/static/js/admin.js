function principal(){
    cuerpo = document.getElementById("cuerpo");
    let addHtml = ``;

    

    addHtml +=` <h1> Hola Mundo </h1>
    
    
    
    
    `


    cuerpo.innerHTML = addHtml;


}
function showHideRow(row) {
    $("." + row).toggle();
}

function newMenu() {
    var x = document.getElementById("menuid");
     
    if (x.style.visibility != "visible") {
       
        x.style.visibility = "visible";
        
    }

   text = document.getElementById("idMenuNew");
   
   text.focus();
}