

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


// VALIDAR CARACTERES DE UN TEXTO


// FUNCIÓN CON JQUERY
$('#mensaje_ayuda1').text('200 carácteres restantes');
$('#message1').keydown(function () {
  var max = 200;
  var len = $(this).val().length;
  if (len >= max) {
      $('#mensaje_ayuda1').text('Has llegado al límite');// Aquí enviamos el mensaje a mostrar          
      $('#mensaje_ayuda1').addClass('text-danger');
      $('#message1').addClass('is-invalid');
      // $('#inputsubmit').addClass('disabled');    
      // document.getElementById('inputsubmit').disabled = true;                    
  } 
  else {
      var ch = max - len;
      $('#mensaje_ayuda1').text(ch + ' carácteres restantes');
      $('#mensaje_ayuda1').removeClass('text-danger');            
      $('#message1').removeClass('is-invalid');            
      // $('#inputsubmit').removeClass('disabled');
      // document.getElementById('inputsubmit').disabled = false;            
  }
});  
$('#mensaje_ayuda2').text('200 carácteres restantes');
$('#message2').keydown(function () {
  var max = 200;
  var len = $(this).val().length;
  if (len >= max) {
      $('#mensaje_ayuda2').text('Has llegado al límite');// Aquí enviamos el mensaje a mostrar          
      $('#mensaje_ayuda2').addClass('text-danger');
      $('#message2').addClass('is-invalid');
      // $('#inputsubmit').addClass('disabled');    
      // document.getElementById('inputsubmit').disabled = true;                    
  } 
  else {
      var ch = max - len;
      $('#mensaje_ayuda2').text(ch + ' carácteres restantes');
      $('#mensaje_ayuda2').removeClass('text-danger');            
      $('#message2').removeClass('is-invalid');            
      // $('#inputsubmit').removeClass('disabled');
      // document.getElementById('inputsubmit').disabled = false;            
  }
});  

$('#mensaje_ayuda3').text('200 carácteres restantes');
$('#message3').keydown(function () {
  var max = 200;
  var len = $(this).val().length;
  if (len >= max) {
      $('#mensaje_ayuda3').text('Has llegado al límite');// Aquí enviamos el mensaje a mostrar          
      $('#mensaje_ayuda3').addClass('text-danger');
      $('#message3').addClass('is-invalid');
      // $('#inputsubmit').addClass('disabled');    
      // document.getElementById('inputsubmit').disabled = true;                    
  } 
  else {
      var ch = max - len;
      $('#mensaje_ayuda3').text(ch + ' carácteres restantes');
      $('#mensaje_ayuda3').removeClass('text-danger');            
      $('#message3').removeClass('is-invalid');            
      // $('#inputsubmit').removeClass('disabled');
      // document.getElementById('inputsubmit').disabled = false;            
  }
});  