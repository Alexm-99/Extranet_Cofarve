function iconclickRedes(icono) {
    
    var valor = document.getElementById("icon-post");
    var valor2 = document.getElementById("envio-icon");
    var valor3 = document.getElementById("iconoR");
   //$("#input").attr("icon-post2",icono);
   $(valor2).attr('value', icono);
   $(valor3).attr('class', `${icono} icon-item icon-happy`);
    //valor2.innerHTML= `<input type="text" name="${icono}" value=${icono} class="form-control"> `
    valor.innerHTML = icono; //Mostar nombre del icono
    
    }
    function guardarDatoRedes(dato){
        var valor = document.getElementById("data-respaldo-redes");
        $(valor).attr('value', dato);
        //alert(valor);
      }
    function iconclickRedesUpdate(icono) {
      
        var id = document.getElementById("data-respaldo-redes").value;
  
        var valor2 = document.getElementById("envio-icon-"+id); //Llamando a elemento de formulario
  
        var valor3 = document.getElementById("iconoR-"+id);// llamando al elemento a mostrar
        
      $(valor2).attr('value', icono); //Cambiando valor del elemento del formulario
       $(valor3).attr('class', `${icono}  icon-item icon-happy`); //Cambiando valor a mostrar
      
       
      
        }