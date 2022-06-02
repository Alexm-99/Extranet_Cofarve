
      
// // preventing from page reload and default actions

// // make POST ajax call
//   // catch the form's submit event
//   $('#todo-form').submit(function (e) {
//     e.preventDefault();
// // serialize the data for sending the form data.
// var serializedData = $(this).serialize();
//       // create an AJAX call
//       $.ajax({
//           data: serializedData, // get the form data
//           type:'POST', // GET or POST
//           url: "{% url 'admin' %}",
          
//           // on success
//           success: function (response) {
//             $("#todo-form").trigger('reset');
//             alert("Guardado Con éxito " );
//             $("#id_name").focus();
//             var instance = JSON.parse(response["instance"]);
//             var fields = instance[0]["fields"];
//             console.log(instance[0]);

//             var tabla = ``;
//             tabla +=`<tr>
//             <td onclick="showHideRow('{{enlace.linkP1}}');"><i class='bx bx-list-ul icon-flecha icon-item'
//         id=""></i></td>

//         <td> <input type="text" name="" id="" class="text-id form-control txt-general "
//         value="${instance[0]["pk"]||""}" readonly></td>

//         <td><input type="text" name="{{form.name.name}}" id="" class="form-control txt-general "
//         value="${fields["name"]||""}"></td>
        
//         <td><input type="text" name="{{form.enlaceP.name}}" id="" class="form-control txt-general "
//         value="${fields["enlaceP"]||""}"></td>
          
//         <td><input type="text" name="{{form.description.name}}" id="" class="form-control txt-general "
//         value="${fields["description"]||""}"></td>


//         <td>
//       <input type="hidden" name="" id="data-respaldo">
//       <!--Para formulario--><input type="hidden" name="{{form.icon.name}}" value="${fields["icon"]||""}"
//         id='envio-icon-"${instance[0]["pk"]||""}"'>
//       <a href="" data-toggle="modal" data-target="#ModalUpddate" onclick='guardarDato("${instance[0]["pk"]||""}") '><i
//           class="${fields["icon"]||""} icon-item icon-happy" id="iconoP-"${instance[0]["pk"]||""}"></i></a>
       
//     </td>`
//       if (fields["state"]){
   
//        tabla += `
      
//        <td> <div class="form-check form-switch">
//         <input type="checkbox" id="flexSwitchCheckChecked" class="form-check-input" name="${fields["state"]}" 
//           checked> </td>` 
//       }else{
        
//         tabla += `<td>
//         <input class="form-check-input" name="${fields["state"]}" type="checkbox" id="flexSwitchCheckChecked"
//           >  </div></td>

        
//           ` 

//       }
    

//        tabla +=`
//        <td> <a href="" onclick="confirmarUpdate('FormUpdate${instance[0]["pk"]||""}'); return false;" class="Button"><i
//           class='bx bxs-save icon-item icon-update' id=""></i></i></a></td>

//           <td> <a href="" onclick="confirm('¿Estas seguro de Eliminar este registro?'); return false;" class="modal-action modal-close waves-effect waves-green btn-flat "><i
     
//             class='bx bxs-trash icon-item icon-delete' id=""></i></a></td>
//     <!-- <td> <a href=""><i class='bx bx-save' ></i></a></td> -->
//     <td> <a href="" data-toggle="modal" data-target="#ModalMenu"><i
//           class='bx bxs-add-to-queue icon-item icon-nuevo'></i></a></td>
//        </tr>`
//           $("#tablaT tbody").prepend(tabla)

//           },
//           // on error
//           error: function (response) {
//               // alert the error if any error occured
//               alert(response["responseJSON"]["error"]);
//           }
//       });
//       return false;
//   });

