$(document).ready(function () {
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
    $('.h').click(function () {
        $('.i').focus();
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
    $('.block3').click(function () {
        if ($(this).html() == '<i class="fa-solid fa-eye"></i>') {
            $(this).html('<i class="fa-sharp fa-solid fa-eye-slash"></i>');
            $('.pass').attr('type', 'text');
        } else {
            $(this).html('<i class="fa-solid fa-eye"></i>');
            $('.pass').attr('type', 'password');
        }
    });
});