function principal(){
    cuerpo = document.getElementById("cuerpo");
    let addHtml = ``;

    

    addHtml +=` <h1> Hola Mundo </h1>
    
    
    
    
    `


    cuerpo.innerHTML = addHtml;


}
function showHideRow(row) {

    
        $('#submenuid').css('display', 'table-row'); 
   
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

function newSubMenu() {
    var x = document.getElementById("submenuid");
     
    if (x.style.display != "table-row") {
       
        x.style.display = "table-row";
        
    }

   text = document.getElementById("idSubMenuNew");
   
   text.focus();
}


$('#btnSubmenuid').click(function(e) {
  
    // Resetear, por si acaso has estado jugando con la otra propiedad
    $('#submenuid').css('visibility', 'visible');
    
    if( $('#submenuid').is(":visible") ) {
     // $('#submenuid').css('display', 'none'); 
    } else {
      $('#submenuid').css('display', 'table-row');
    }
  });
