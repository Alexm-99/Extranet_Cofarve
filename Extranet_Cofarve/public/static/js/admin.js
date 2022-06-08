


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
   $(valor3).attr('class', `${icono} icon-item icon-happy`);
    //valor2.innerHTML= `<input type="text" name="${icono}" value=${icono} class="form-control"> `
    valor.innerHTML = icono; //Mostar nombre del icono
    
    }

function guardarDato(dato){
  var valor = document.getElementById("data-respaldo");
  $(valor).attr('value', dato);
  //alert(valor);
}
    function iconclickUpdate(icono) {
      
      var id = document.getElementById("data-respaldo").value;

      var valor2 = document.getElementById("envio-icon-"+id); //Llamando a elemento de formulario

      var valor3 = document.getElementById("iconoP-"+id);// llamando al elemento a mostrar
      
    $(valor2).attr('value', icono); //Cambiando valor del elemento del formulario
     $(valor3).attr('class', `${icono}  icon-item icon-happy`); //Cambiando valor a mostrar
    
     
    
      }

//Filtro en submenu
      function filtroArea(){
  
        var area = document.getElementById("area").value;
       // alert(area);
       $("#GuardarIdS").attr('value', area);
      }

//filtro en principal
function filtroAreaP(){
  //var idArea = document.getElementById("GuardarIdS");
    var area = document.getElementById("areaP").value;
    var contenido = document.getElementById("contenidoMenu"+area);
    var todoContenido = document.getElementById("todoFiltro").value;
   //alert(area);

   //$('contenidoMenu').css('background-color', 'blue');
    if (area == "TFiltro"){
      $('.filtroSubmenu').css('display', 'none');
      $('.contenidoMenu').css('display', 'table-row');
    }else{
      $('.filtroSubmenu').css('display', 'none');
      $('.contenidoMenu').css('display', 'none');
   $('#contenidoMenu'+area).css('display', 'table-row');
    }
        
   


  }

    function CodigoMenu(valor){
      var area = document.getElementById("id_name").value;
     
      var valorT = parseInt(valor)+1;

      $(codArea).attr('value',area+valorT ); //Cambiando valor a mostrar
    }