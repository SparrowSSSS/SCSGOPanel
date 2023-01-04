$(document).ready(function () {
    async function sign_up() {
        let email = document.getElementById('e').value;
        let nickname = document.getElementById('n').value;
        let password = document.getElementById('p').value;
        let res = await eel.sign_up__f(email, nickname, password)();
    }
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
    $('.create_account').click(function () {
        sign_up();
    });
});