$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });

    //slide up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
    });

    // toggle Memu Navbar Script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });


    // typing animmation
    var typed = new Typed(".typing",{
        strings: ["Developer.","Programmer.", "Designer.", "Freelancer."],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing2",{
        strings: ["Developer.","Programmer.", "Designer.", "Freelancer."],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });
    //Owl Carousel Script
    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        autoPlayTimeOut: 2000,
        autoPlayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },
            600:{
                items: 2,
                nav: false
            },
            1000:{
                items: 3,
                nav: false
            }
        }

    });
});