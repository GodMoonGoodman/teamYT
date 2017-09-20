$(window).load(function() {
  // Animate loader off screen
  $(".se-pre-con").fadeOut("slow");;
});
// Changing navbar on scroll
$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('nav').removeClass('nav-expanded');
  } else {
    $('nav').addClass('nav-expanded');
  }
});

$( document ).ready(function() {
  $('.counter').counterUp({
   	delay: 20,
    time: 1500
  });
  $('body').scrollspy({
    target: '.navbar-fixed-top',
    offset: 80
  })
  $('a.scrollto').bind('click', function(event) {
    var $anchor = $(this);
    $('html, body').stop().animate({
        scrollTop: ($($anchor.attr('href')).offset().top - 40)
    }, 1250, 'easeInOutExpo');
    event.preventDefault();
  });

   //Client Speak Owl Carousel
  $("#testimonials").owlCarousel({
   	items: 1,
   	animateOut: 'slideOutDown',
    animateIn: 'flipInX',
    smartSpeed:450,
    autoplay: true,
    autoplayTimeout: 4000,
    loop: true,
    autoplayHoverPause: true
  });
  $("#client-logos").owlCarousel({
   	items: 5,
    autoplay: true,
    autoplayTimeout: 3000,
    loop: true,
    autoplayHoverPause: true,
    dots: false,
    margin: 60,
    responsive:{
        0:{
            items:2,
            margin: 30
        },
        768:{
            items:5,
            margin: 30
        },
        992:{
            items:5,
            margin: 60
        }
    }
  });
  $("#team").owlCarousel({
    items: 3,
    autoplay: true,
    autoplayTimeout: 3000,
    loop: true,
    autoplayHoverPause: true,
    margin: 30,
    dots: false,
    responsiveClass:true,
    responsive:{
        0:{
            items:1
        },
        768:{
            items:3
        }
    }
  });
  $('.section-pricing').parallax();

   
  $('.gallery-work').magnificPopup({
    type: 'image',
    zoom: { enabled: true },
    gallery:{ enabled: true }
  });

 // Contact form Validation
  $("#contact-form").validate({
    rules: {
      name: {
        required: true
      },
      email: {
        required: true,
        email: true
      },
      phone: {
        required: true,
        number: true
      },
      subject: {
        required: true
      },
      message: {
        required: true
      }
    }
  });
  $("#subscribe-form").validate({
    rules: {
      email: {
        required: true,
        email: true
      }
    },
    errorElement : 'div',
    errorLabelContainer: '.error-msg'
  });
  
new WOW().init();
});

  

// Back to Top
if ($('#back-to-top').length) {
    var scrollTrigger = 100, // px
        backToTop = function () {
            var scrollTop = $(window).scrollTop();
            if (scrollTop > scrollTrigger) {
                $('#back-to-top').addClass('show');
            } else {
                $('#back-to-top').removeClass('show');
            }
        };
    backToTop();
    $(window).on('scroll', function () {
        backToTop();
    });
    $('#back-to-top').on('click', function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 700);
    });
}

