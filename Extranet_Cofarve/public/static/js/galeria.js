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


  function estadoGaleria(estado, ruta){
    // alert("xd");
    // document.getElementById(id).submit()
    var datos = {
      "state" : estado, // Dato #1 a enviar
  };
  

    $.ajax({
      data: datos,
      url: ruta,
      type: 'post',
      success:  function (response) {
          console.log(response); // Imprimir respuesta del archivo
          
      },
      error: function (error) {
          console.log(error); // Imprimir respuesta de error
      }
});
  }