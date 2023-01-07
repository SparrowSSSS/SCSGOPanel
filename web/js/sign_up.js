$(document).ready(function () {
    if (localStorage.getItem('auto_sign_in') == "yes") {
        window.location.href = '../main.html';
        sessionStorage.setItem('user_nickname', localStorage.getItem('user_nickname'));
        sessionStorage.setItem('user_email', localStorage.getItem('user_email'));
        sessionStorage.setItem('user_id', localStorage.getItem('user_id'));
    }
    async function sign_up() {
        document.getElementById("overlay").classList.remove("none");
        document.getElementById("overlay").classList.add("overlay");
        let email = document.getElementById('e').value;
        let nickname = document.getElementById('n').value;
        let password = document.getElementById('p').value;
        let res = await eel.sign_up__f(email, nickname, password)();
        if (res == '1') {
            window.location.href = '../main.html';
            localStorage.setItem('auto_sign_in', "yes");
            sessionStorage.setItem('user_nickname', nickname);
            sessionStorage.setItem('user_email', email);
            localStorage.setItem('user_nickname', nickname);
            localStorage.setItem('user_email', email);
            let id = await eel.get__id(email)();
            sessionStorage.setItem('user_id', id);
            localStorage.setItem('user_id', id);
        }
        else if (res == '0') {
            document.getElementById("error0").classList.remove("none");
            document.getElementById("error0").classList.add("block");
        }
        else if (res == '2') {
            document.getElementById("error2").classList.remove("none");
            document.getElementById("error2").classList.add("block");
        }
        else {
            document.getElementById("error3").classList.remove("none");
            document.getElementById("error3").classList.add("block");
        }
        document.getElementById("overlay").classList.remove("overlay");
        document.getElementById("overlay").classList.add("none");
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