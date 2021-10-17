$(document).ready(function(){
  $('.sidenav').sidenav({edge: "left"});
  $('select').formSelect();
  // Copyright year
  $('.copyright').text(new Date().getFullYear());
  $('input#review_capture').characterCounter();
  $('.modal').modal();
});

// Code borrowed from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top with some modifications

//Get the button
var mybutton = document.getElementById("myBtn");

// When user scrolls down 20px from the top of document, button fades in.
window.onscroll = function () {
	scrollFunction();
};

function scrollFunction() {
	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		mybutton.style.display = "block";
	} else {
		mybutton.style.display = "none";
    mybutton.style.animation = "fadeIn 1s";
	}
}

// When user clicks on the button, smooth scroll to top of document
function topFunction() {
  // https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}

topFunction();
