$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
  	items: 5,
  	margin: 10,
  	nav: true,
  	loop: true,

  });
});


var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel)