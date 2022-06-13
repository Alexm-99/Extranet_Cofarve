function PostMenu(ruta){
      // preventing from page reload and default actions
        
        // make POST ajax call
            // catch the form's submit event
            $('#todo-form').submit(function (e) {
                e.preventDefault();
          // serialize the data for sending the form data.
          var serializedData = $(this).serialize();
                  // create an AJAX call
                  $.ajax({
                      data: serializedData, // get the form data
                      type:'POST', // GET or POST
                      url: ruta,
                      
                      // on success
                      success: function (response) {
                        $("#todo-form").trigger('reset');
                        alert("Guardado Con éxito " );
                        $("#id_name").focus();
                //         var instance = JSON.parse(response["instance"]);
                //         var fields = instance[0]["fields"];
                //         console.log(instance[0]);
  
               
                //       $("#tablaT tbody").prepend(tabla)
  
                      },
                      // on error
                      error: function (response) {
                          // alert the error if any error occured
                          alert(response["responseJSON"]["error"]);
                      }
                  });
                  alert(response["responseJSON"]["error"])
                  return false;
              });
}



function PostSubMenu(ruta){
    
      
      // make POST ajax call
          // catch the form's submit event
          $('#todo-form2').submit(function (e) {
            // preventing from page reload and default actions
              e.preventDefault();
            var dataSend=$('#todo-form2').serializeArray(); // obtengo los inputs y sus valores del formulario
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
                // create an AJAX call
                $.ajax({
                    data: dataSend, // get the form data
                    type:'POST', // GET or POST
                    url:ruta,
                    
                    // on success
                    success: function (response) {
                      $('#todo-form2').trigger('reset');
                      alert("Guardado Con éxito " );
                      $('#subarea').focus();
                      
              //         var instance = JSON.parse(response["instance"]);
              //         var fields = instance[0]["fields"];
              //         console.log(instance[0]);

             
              //       $("#tablaT tbody").prepend(tabla)

                    },
                    // on error
                    error: function (response) {
                        // alert the error if any error occured
                        alert(response["responseJSON"]["error"]);
                    }
                });
                return false;
            });
}


function DeleteMenu(ruta, id){
    let confirmAction = confirm("¿Estas seguro de Eliminar este registro?");
    
    if (confirmAction) {
        

        $(`#${id}`).attr('href',ruta ); //Cambiando valor a mostrar
    //    // preventing from page reload and default actions
    
    //   // make POST ajax call
    //       // catch the form's submit event
    //       $(`#${id}`).submit(function (e) {
    //         e.preventDefault();
    //   // serialize the data for sending the form data.
    //   var serializedData = $(this).serialize();
    //           // create an AJAX call
    //           $.ajax({
    //               data: serializedData, // get the form data
    //               type:'POST', // GET or POST
    //               url: ruta,
                  
    //               // on success
    //               success: function (response) {
                 
    //                 alert("Eliminado Con éxito " );
          
    //         //         var instance = JSON.parse(response["instance"]);
    //         //         var fields = instance[0]["fields"];
    //         //         console.log(instance[0]);

           
    //         //       $("#tablaT tbody").prepend(tabla)

    //               },
    //               // on error
    //               error: function (response) {
    //                   // alert the error if any error occured
    //                   alert(response["responseJSON"]["error"]);
    //               }
    //           });
              
    //       });
         
      }
      else{
       
          return false;
      }
    
    
}

function confirmarUpdate(id){

    let confirmAction = confirm("¿Estas seguro de actualizar este registro?");
      if (confirmAction) {
       // $(`#${id}`).attr('href',ruta ); //Cambiando valor a mostrar
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