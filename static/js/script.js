$(document).ready(function(){
  $('.sidenav').sidenav({edge: "left"});
  $('select').formSelect();
  // Copyright year
  $('.copyright').text(new Date().getFullYear());
  $('input#review_capture').characterCounter();
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

// Code borrowed from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top

//Back to top btn
//Get the button
mybutton = document.getElementById("myBtn");

// When user scrolls down 20px from the top of document, button fades in.
window.onscroll = function () {
	scrollFunction();
};

function scrollFunction() {
	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		mybutton.style.display = "block";
	} else {
		mybutton.style.display = "none";
    mybutton.style.animation = "fadeIn 1s"
	}
}

// When user clicks on the button, smooth scroll to top of document
function topFunction() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

