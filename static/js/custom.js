(function ($) {
    "use strict";


//------------------------------------------
    //ta-blog-slider
//------------------------------------------
    function blogslider() {
        $(".blog-slider").owlCarousel({
            navigation: true, // Show next and prev buttons
            pagination: true,
            paginationSpeed: 400,
            singleItem: true,
            lazyLoad: true,
            autoPlay: true,
            navigationText: [
                "<i class='fa fa-long-arrow-left'></i>",
                "<i class='fa fa-long-arrow-right'></i>"
            ]
        });
    }

    blogslider();
//------------------------------------------
    //ta-blog-slider
//------------------------------------------
    function viewdetailslider() {
        $(".ta-view-detail-slider").owlCarousel({
            navigation: true, // Show next and prev buttons
            pagination: true,
            paginationSpeed: 400,
            singleItem: true,
            lazyLoad: true,
            autoPlay: true,
            navigationText: [
                "<i class='fa fa-chevron-left'></i>",
                "<i class='fa fa-chevron-right'></i>"
            ]
        });
    }

    viewdetailslider();

})(jQuery);