$(document).ready(function(){
  $('.sidenav').sidenav({edge: "left"});
  $('select').formSelect();
  // Copyright year
  $('.copyright').text(new Date().getFullYear());

  $('.fadeinleftstart').each(function() {
    $(this).animate({'opacity':'1', 'margin-left':'0px'}, 1000);
  });

  

  // Fade in elements on sroll 
  // Code by https://vincoding.com/fade-in-elements-scroll-jquery/
  $(window).scroll(function() {
    $('.fadein').each(function() {
  
      var bottomOfElement = $(this).offset().top + $(this).outerHeight();
      var bottomOfWindow = $(window).scrollTop() + $(window).height();
  
      if (bottomOfWindow > bottomOfElement) {
        $(this).animate({'opacity':'1'}, 1000);
      }
    });

    $('.fadeinleft').each(function() {

      var bottom_of_element = $(this).offset().top + $(this).outerHeight();
      var bottom_of_window =  $(window).scrollTop() + $(window).height();
  
      if (bottom_of_window > bottom_of_element) {
        $(this).animate({'opacity':'1', 'margin-left':'0px'}, 1000);
      }
    });
  });
});


jQuery(function(){

  var minimized_elements = $('p.minimize');
  
  minimized_elements.each(function(){    
      var t = $(this).text();        
      if(t.length < 350) return;
      
      $(this).html(
          t.slice(0,350)+'<span>... </span><a class="more"> <span>|</span> Show More</a>'+
          '<span style="display:none;">'+ t.slice(350,t.length)+' <a class="less"> <span>|</span> Show Less</a></span>'
      );
      
  }); 
  
  $('a.more', minimized_elements).click(function(event){
      event.preventDefault();
      $(this).hide().prev().hide();
      $(this).next().show();        
  });
  
  $('a.less', minimized_elements).click(function(event){
      event.preventDefault();
      $(this).parent().hide().prev().show().prev().show();    
  });

});
