$(document).ready(function(){
  $('.sidenav').sidenav({edge: "left"});

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

