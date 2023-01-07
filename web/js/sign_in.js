$(document).ready(function () {
    async function sign_in() {
        document.getElementById("overlay").classList.remove("none");
        document.getElementById("overlay").classList.add("overlay");
        let email = document.getElementById('em').value;
        let password = document.getElementById('p').value;
        let res = await eel.sign_in__f(email, password)();
        if (res == '1') {
            window.location.href = '../main.html';
            localStorage.setItem('auto_sign_in', "yes");
            sessionStorage.setItem('user_email', email);
            localStorage.setItem('user_email', email);
            let nickname = await eel.get__nickname(email)();
            sessionStorage.setItem('user_nickname', nickname);
            localStorage.setItem('user_nickname', nickname);
            let id = await eel.get__id(email)();
            sessionStorage.setItem('user_id', id);
            localStorage.setItem('user_id', id);
        }
        else if (res == '0') {
            document.getElementById("error0").classList.remove("none");
            document.getElementById("error0").classList.add("block");
        }
        else {
            document.getElementById("error2").classList.remove("none");
            document.getElementById("error2").classList.add("block");
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
    $('.button__s_in').click(function () {
        sign_in();
    });
    $('.rec_pass').click(function () {
        sessionStorage.setItem('em-input_save', document.getElementById('em').value);
    });
});