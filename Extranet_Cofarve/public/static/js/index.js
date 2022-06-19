document.addEventListener("DOMContentLoaded", function(event) {

  // const showNavbar = (toggleId, navId, bodyId, headerId) =>{
  // // const toggle = document.querySelectorAll(`.${toggleId}`);
  // const toggle = document.getElementById(toggleId),
  // nav = document.getElementById(navId),
  // bodypd = document.getElementById(bodyId),
  // headerpd = document.getElementById(headerId)
  
  // // Validate that all variables exist
  // if(toggle && nav && bodypd && headerpd){
  // // toggle.forEach(el => el.addEventListener('click', event => {
  //   toggle.addEventListener('click', ()=>{

  // // show navbar
  // nav.classList.toggle('show')
  // // change icon
  // toggle.classList.toggle('bx-x')
  // // add padding to body
  // bodypd.classList.toggle('body-pd')
  // // add padding to header
  // headerpd.classList.toggle('body-pd')
  // })
  // }
  // }
  


  // showNavbar('header-toggle','nav-bar','body-pd','header')
  
  /*===== LINK ACTIVE =====*/
  const linkColor = document.querySelectorAll('.nav_link')
  
  function colorLink(){
  if(linkColor){
  linkColor.forEach(l=> l.classList.remove('active'))
  this.classList.add('active')
  }
  }
  linkColor.forEach(l=> l.addEventListener('click', colorLink))
  
  // Your code to run since DOM is loaded and ready
  });


  function mostrarP(){
      var panel = document.getElementById("nav-bar"); 

      const toggle = document.getElementById('header-toggle');
      if(panel.style.width != "216px"){
        toggle.classList.toggle('bx-x');
        
      } 
    
   document.getElementById("body-pd").style.paddingLeft = "216px ";
   document.getElementById("header").style.paddingLeft = "216px ";
    panel.style.width = "216px";
  if(panel.style.width == "216px"){
   
        
      } 

  }
  function ocultarP(){
    var panel = document.getElementById("nav-bar");
    const toggle = document.getElementById('header-toggle');
    if(panel.style.width == "216px"){
   
  document.getElementById("body-pd").style.paddingLeft = "60px ";
   document.getElementById("header").style.paddingLeft = "60px ";
  panel.style.width = "60px";
  toggle.classList.toggle('bx-x');


  $("li.submenu > ul").hide()
  $('li.submenu').click(function () {
    $('ul.submenu').not(this).find('ul').hide();
   
  });



// Temporizador






    }else{
      var panel = document.getElementById("nav-bar");
      document.getElementById("body-pd").style.paddingLeft = "216px ";
      document.getElementById("header").style.paddingLeft = "216px ";
       panel.style.width = "216px";
       toggle.classList.toggle('bx-x');
      
    }

  }

// Función para que el panel se cierre cuando el mouse no se mueve --
 (function(){
  var moviendo= false;
  document.onmousemove = function(){
         moviendo= true;
  };
  setInterval (function() {
     if (!moviendo) {
         // No ha habido movimiento desde hace un segundo, aquí tu codigo
         var panel = document.getElementById("nav-bar");
         const toggle = document.getElementById('header-toggle');
         if(panel.style.width == "216px"){
        
       document.getElementById("body-pd").style.paddingLeft = "60px ";
        document.getElementById("header").style.paddingLeft = "60px ";
       panel.style.width = "60px";
       toggle.classList.toggle('bx-x');
     
     
       $("li.submenu > ul").hide()
       $('li.submenu').click(function () {
         $('ul.submenu').not(this).find('ul').hide();
       });
     }
     } else {
         moviendo=false;
     }
  }, 10000); // Cada 10 segundo
})()

