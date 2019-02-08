(function($) {
  
  "use strict";  

  $(window).on('load', function() {
  	// Material
	$.material.init();

	// Dropdown 
  	$('.dropdown-toggle').dropdown()

  	$('.search-icon').on('click',function() {
    $('.navbar-form').fadeIn(300);
    $('.navbar-form input').focus();
	  });
	  $('.navbar-form input').blur(function() {
	    $('.navbar-form').fadeOut(300);
	 });

  	// Carousel
	$('.carousel').carousel()

	// Preloader
    $('#preloader').fadeOut();

    // Sticky Nav
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 200) {
            $('.scrolling-navbar').addClass('top-nav-collapse');
        } else {
            $('.scrolling-navbar').removeClass('top-nav-collapse');
        }
    });

    //  VIDEO POP-UP
    $('.video-popup').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false,
    });

    //WOW Scroll Spy
	var wow = new WOW({
	    //disabled for mobile
	    mobile: false
	});
	wow.init();
	// Testimonial Carousel
	  var owl = $(".testimonials-carousel");
	  owl.owlCarousel({
	    navigation: false,
	    pagination: true,
	    slideSpeed: 1000,
	    stopOnHover: true,
	    autoPlay: true,
	    items: 1,
	    itemsDesktopSmall: [1024, 1],
	    itemsTablet: [600, 1],
	    itemsMobile: [479, 1]
	  });

	  // Client Owl Carousel

	$("#client-logo").owlCarousel({
	    navigation: false,
	    pagination: false,
	    slideSpeed: 1000,
	    stopOnHover: true,
	    autoPlay: true,
	    items: 4,
	    itemsDesktopSmall: [1024, 3],
	    itemsTablet: [600, 1],
	    itemsMobile: [479, 1]
	});

	// Flickr Carousel
	$("#flickr-carousel").owlCarousel({
	  slideSpeed : 300,
	  paginationSpeed : 400,
	  items : 1,
	  autoPlay: 3000,
	  stopOnHover : true,

	});

	// Image Carousel
	$("#Material-image-carousel").owlCarousel({
	  slideSpeed : 300,
	  paginationSpeed : 400,
	  items : 4,
	  autoPlay: 3000,
	  stopOnHover : true,
	});

	// Image Carousel
	$("#team-carousel").owlCarousel({
	  slideSpeed : 300,
	  paginationSpeed : 400,
	  items : 4,
	  autoPlay: 3000,
	  stopOnHover : true,
	});

	// Counter JS
    $('.work-counter-section').on('inview', function(event, visible, visiblePartX, visiblePartY) {
        if (visible) {
            $(this).find('.timer').each(function() {
                var $this = $(this);
                $({
                    Counter: 0
                }).animate({
                    Counter: $this.text()
                }, {
                    duration: 3000,
                    easing: 'swing',
                    step: function() {
                        $this.text(Math.ceil(this.Counter));
                    }
                });
            });
            $(this).off('inview');
        }
    });	

	// MixitUp Init
	$('#Material-portfolio').mixItUp(); 

    $('#myTab a').on('click',function (e) {
	  e.preventDefault()
	  $(this).tab('show')
	})

	// Slick Nav 
    $('.wpb-mobile-menu').slicknav({
      prependTo: '.navbar-header',
      parentTag: 'span',
      allowParentLinks: true,
      duplicate: false,
      label: '',
      closedSymbol: '<i class="mdi mdi-chevron-right"></i>',
      openedSymbol: '<i class="mdi mdi-chevron-down"></i>',
    });

	 // Back Top Link
	  var offset = 200;
	  var duration = 500;
	  $(window).scroll(function() {
	    if ($(this).scrollTop() > offset) {
	      $('.back-to-top').fadeIn(400);
	    } else {
	      $('.back-to-top').fadeOut(400);
	    }
	  });
	  
	  $('.back-to-top').click(function(event) {
	    event.preventDefault();
	    $('html, body').animate({
	      scrollTop: 0
	    }, 600);
	    return false;
	  });

  });      

}(jQuery));


