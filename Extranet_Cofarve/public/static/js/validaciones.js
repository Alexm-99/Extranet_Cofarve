

// VALIDAR TAMAÑO DE ARCHIVO

var banderaTamano = false;

function validarT() {
  var o = document.getElementById('id_imageX');
  var foto = o.files[0];
  var c = 0;

  if (o.files.length == 0 || !(/\.(jpg|png)$/i).test(foto.name)) {
    alert('Ingrese una imagen con alguno de los siguientes formatos: .jpeg/.jpg/.png.');
    return false;
  }
   
  // Si el tamaño de la imagen fue validado
  if (banderaTamano) {
    return true;
  }

  var img = new Image();
  img.onload = function dimension() {
    if (this.width.toFixed(0) != 1301&& this.height.toFixed(0) != 500) {
      alert('Las medidas deben ser: 1301 x 500');
    } else {
    //   alert('Imagen correcta ');
    
      // El tamaño de la imagen fue validado
      banderaTamano = true;
      
      // Buscamos el formulario
      var form = document.getElementById('formularioImagen');
      // Enviamos de nuevo el formulario con la bandera modificada.
    // form.submit();
    form.submit();

     
    }
  };
  img.src = URL.createObjectURL(foto);
  
  // Devolvemos false porque falta validar el tamaño de la imagen
  return false;
}