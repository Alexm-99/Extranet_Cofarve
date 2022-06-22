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


  function estadoGaleria(id, ruta){
   
    var x = ruta;
    // alert(x);
    var state =document.getElementById(id);
    // alert(state);
    if ($('input[type=checkbox]:checked').length > 4) {
      $(state).prop('checked', false);
      alert("Solo puedes seleccionar 4 imagenes");
  }else{


   if(state.checked) {
      $.post(`update/State/${x}`, {},
      function(data, status){
          console.log("Data: " + data + "\nStatus: " + status);
      });
     
    }else{
 $.post(`update/StateF/${x}`, {},
      function(data, status){
          console.log("Data: " + data + "\nStatus: " + status);
      });

    }
 }
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