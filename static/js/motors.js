$(document).ready(function () {
    $('nav a').on('click', function (e) {
        e.preventDefault();
        var chapter = $(e.target).prop('href').split('#')[1],
            chapterPosition = $('#' + chapter).position().top,
            bodyOffset = parseInt($('body').css('padding-top'));
        $("html, body").animate({scrollTop: chapterPosition - bodyOffset}, 500);
    });

    $(window).on('resize', function () {
        carsLogosFill();
    });

    function carsLogosFill() {
        var currentScreenWidth = $(window).width(), carsLogosContent = '', logosQty = 54,
            colsQty = currentScreenWidth < 768 ? 3 : currentScreenWidth < 992 ? 4 : 6;

        for (var i = 1; i <= logosQty; i++) {
            carsLogosContent +=
                '<div class="col-xs-4 col-sm-3 col-md-2 col-lg-2">' +
                '<img style="width:100px;margin: 10px 5px" src="/static/images/logo_car/lc_' + i + '.png"/>' +
                '</div>';
            if (i % colsQty == 0 && i < logosQty) carsLogosContent += '</div><div class="row text-center">';
            if (i == logosQty) carsLogosContent += '</div>';
        }

        $('#cars-logos').html('<div class="row text-center">' + carsLogosContent + '</div>');
    }

    carsLogosFill();
});

