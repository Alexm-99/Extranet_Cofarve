function iconclickRedes(icono) {
    
    var valor = document.getElementById("icon-post");
    var valor2 = document.getElementById("envio-icon");
    var valor3 = document.getElementById("iconoP");
   //$("#input").attr("icon-post2",icono);
   $(valor2).attr('value', icono);
   $(valor3).attr('class', `${icono} icon-item icon-happy`);
    //valor2.innerHTML= `<input type="text" name="${icono}" value=${icono} class="form-control"> `
    valor.innerHTML = icono; //Mostar nombre del icono
    
    }