


function showHideRow(row) {
      
    
 $("." + row).toggle();
 }



// function newMenu() {
//     var x = document.getElementById("menuid");
     
//     if (x.style.display != "table-row") {
       
//         x.style.display = "table-row";
        
//     }

//    text = document.getElementById("idMenuNew");
   
//    text.focus();
// }

// function newSubMenu() {
//     var x = document.getElementById("submenuid");
     
//     if (x.style.display != "table-row") {
       
//         x.style.display = "table-row";
        
//     }

 //  text = document.getElementById("idSubMenuNew");
   
 //  text.focus();
//}


$('#btnSubmenuid').click(function(e) {
  
    // Resetear, por si acaso has estado jugando con la otra propiedad
    $('#submenuid').css('visibility', 'visible');
    
    if( $('#submenuid').is(":visible") ) {
     // $('#submenuid').css('display', 'none'); 
    } else {
      $('#submenuid').css('display', 'table-row');
    }
  });


  function iconclick(icono) {
      
    var valor = document.getElementById("icon-post");
    var valor2 = document.getElementById("envio-icon");
    var valor3 = document.getElementById("iconoP");
   //$("#input").attr("icon-post2",icono);
   $(valor2).attr('value', icono);
   $(valor3).attr('class', `${icono}  icon-item icon-happy`);
    //valor2.innerHTML= `<input type="text" name="${icono}" value=${icono} class="form-control"> `
    valor.innerHTML = icono;
  
    }
