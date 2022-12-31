$(document).ready(function () {
    $('.block3').click(function () {
        if ($(this).html() == '<i class="fa-solid fa-eye"></i>') {
            $(this).html('<i class="fa-sharp fa-solid fa-eye-slash"></i>');
            $('.pass').attr('type', 'text');
        } else {
            $(this).html('<i class="fa-solid fa-eye"></i>');
            $('.pass').attr('type', 'password');
        }
    });
    $('.h1').click(function () {
        $('.i1').focus();
    });
    $('.h2').click(function () {
        $('.i2').focus();
    });
    $('.h3').click(function () {
        $('.i3').focus();
    });
    $("*").focus(function () {
        if ($('#r').attr('class') == 'block') {
            $('#r').addClass('none');
            $('#r').removeClass('block');
        };
    });
    $(".pass").focus(function () {
        $('#r').addClass('block');
        $('#r').removeClass('none');
    });
    $('.sign_up').click(function () {
        if ($('.sign_up').attr('class') == 'sign_up') {
            $('.sign_in').removeClass('active');
            $('.sign_up').addClass('active');
            $('.s_in').addClass('none');
            $('.s_in').removeClass('block');
            $('.s_up').addClass('block');
            $('.s_up').removeClass('none');
        };
    });
    $('.sign_in').click(function () {
        if ($('.sign_in').attr('class') == 'sign_in') {
            $('.sign_up').removeClass('active');
            $('.sign_in').addClass('active');
            $('.s_up').addClass('none');
            $('.s_up').removeClass('block');
            $('.s_in').addClass('block');
            $('.s_in').removeClass('none');
        };
    });
});