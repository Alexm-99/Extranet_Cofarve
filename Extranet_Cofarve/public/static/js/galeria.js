// Create a lightbox
(function() {
    var $lightbox = $("<div class='lightbox'></div>");
    var $img = $("<img>");
    var $caption = $("<p class='caption'></p>");
  
    // Add image and caption to lightbox
  
    $lightbox
      .append($img)
      .append($caption);
  
    // Add lighbox to document
  
    $('body').append($lightbox);
  
    $('.lightbox-gallery img').click(function(e) {
      e.preventDefault();
  
      // Get image link and description
      var src = $(this).attr("data-image-hd");
      var cap = $(this).attr("alt");
  
      // Add data to lighbox
  
      $img.attr('src', src);
      $caption.text(cap);
  
      // Show lightbox
  
      $lightbox.fadeIn('fast');
  
      $lightbox.click(function() {
        $lightbox.fadeOut('fast');
      });
    });
  
  }());


  function estadoGaleria(estado, ruta, formulario){
    // alert("xd");
    // document.getElementById(id).submit()
    // e.preventDefault();
    $(`#${formulario}`).submit(function (e) {
      var dataSend=$(`#${formulario}`).serializeArray();
    var datos = {
      "state" : estado, // Dato #1 a enviar
  };
  //  var serializedData = $(this).serialize();
alert(serializedData);
    $.ajax({
      data: dataSend,
      url: ruta,
      type: 'post',
      // headers: { "X-CSRFToken": getCookie("csrftoken") },
      success:  function (response) {
          console.log(response); // Imprimir respuesta del archivo
          
      },
      error: function (error) {
          console.log(error); // Imprimir respuesta de error
      }
});
    });
  }



  function DeleteGaleria(ruta, id){
    let confirmAction = confirm("¿Estas seguro de Eliminar este registro?");
    
    if (confirmAction) {
        

        $(`#${id}`).attr('href',ruta ); //Cambiando valor a mostrar
         
      }
      else{
       
          return false;
      }
    
    
}