


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
      var idArea = document.getElementById("GuardarIdS");
        var area = document.getElementById("area").value;
       // alert(area);
       $(idArea).attr('value', area);
      }

//filtro en principal
function filtroAreaP(){
  var idArea = document.getElementById("GuardarIdS");
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


      $("element").on("event", function(e) {
        // aquí obtienes los datos si es que deseas
        // enviar esos datos al servidor para que
        // trabaje con ellos, por ejemplo:
        var dataToSend = $("#txt-search").val();
    
        /**
         * @description Llamada AJAX al servidor.
         * url: ruta al archivo del lado del servidor que procesará los datos y/o la acción.
         * dataType: tipo de datos con los que se trabajará. Esto implica que si se envía por
         * ejemplo un objeto JSON, se debe retornar también un objeto JSON. De lo contrario, 
         * aunque del lado del servidor todo esté correcto, jQuery al no poder identificar
         * la respuesta en formato JSON, lanzará un error 'parse error' y se ejecutará el
         * método fail en lugar del done().
         * data: Datos a enviar. Puede ser JSON, texto plano, html, etc. (ver doc.).
         * type: Tipo de petición: POST o GET.
         */
        $.ajax(
        {
            url: "accion.py",
            dataType: "tipo",
            data: dataToSend,
            type: "POST o GET"
        })
        .done(function (data) {
            // proceso
        })
        /**
         * jqXHR: Representa a la respuesta enviada del servidor.
         * textStatus: Texto donde se muestra el mensaje de error enviado del servidor.
         * errorThrown: Objeto que representa el error lanzado desde el servidor (Exception).
         */
        .fail(function (jqXHR, textStatus, errorThrown) {
            // proceso
        })
        /**
         * jqXHR/data: si no hay error en vez del objeto jqXHR recibe la data enviada del servidor.
         * textStatus: Siempre será éste parámetro.
         * erorThrown/jqXHR: Si no hay error recibe el objeto jqXHR. Si hay error recibe errorThrown.
         * @description Este método se ejecuta haya o no haya error. Puede ser útil a veces.
         */
        .always(function (jqXHR, textStatus, errorThrown) {
            // proceso
        });
    
    });




    function confirmarUpdate(id){

      let confirmAction = confirm("¿Estas seguro de actualizar este registro?");
        if (confirmAction) {
         
          document.getElementById(id).submit()
           
        } else {
          alert("Actualización cancelada");
        }
      

    }
    function confirmarUpdate2(id){

      let confirmAction = confirm("¿Estas seguro de actualizar este registro?");
        if (confirmAction) {
         
          document.getElementById(id).submit()
           
        } else {
          alert("Actualización cancelada");
        }
      

    }

    function CodigoMenu(valor){
      var area = document.getElementById("id_name").value;
     
      var valorT = parseInt(valor)+1;

      $(codArea).attr('value',area+valorT ); //Cambiando valor a mostrar
    }