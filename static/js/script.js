$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

// Copyright year
$('#copyright').text(new Date().getFullYear());


// Fade in elements on sroll 
// Code by https://vincoding.com/fade-in-elements-scroll-jquery/

$(document).ready(function(){
  $(window).scroll(function() {
    $('.fadein').each(function() {

        var bottom_of_element = $(this).offset().top + $(this).outerHeight();
        var bottom_of_window = $(window).scrollTop() + $(window).height();

        if (bottom_of_window > bottom_of_element) {
          $(this).animate({'opacity':'1'}, 1000);
        }
    })
  });
});