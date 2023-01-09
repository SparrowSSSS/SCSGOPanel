async function new_pass() {
    document.getElementById("overlay").classList.add("overlay");
    document.getElementById("overlay").classList.remove("none");
    let password = document.getElementById('p').value;
    let email = localStorage.getItem('user_email');
    let res = await eel.new_password(password, email)();
    if (res == '1') {
        document.getElementById('result').innerHTML = "<p id='rec_p'>Ваш пароль был успешно изменён</p>";
        localStorage.removeItem('user_email');
        setTimeout(function() {
            window.location.href = '../sign_in.html';      
            document.getElementById("overlay").classList.add("none");   
            document.getElementById("overlay").classList.remove("overlay");           
        }, 10000);
    }
    else if (res == '0') {
        document.getElementById('result').innerHTML = "<p class='error'>Произошла техническая ошибка</p>";
        document.getElementById("overlay").classList.add("none");   
        document.getElementById("overlay").classList.remove("overlay"); 
    }
    else {
        document.getElementById('result').innerHTML = "<p class='error'>Новый пароль является неверным</p>";
        document.getElementById('p').value = "";
        document.getElementById("overlay").classList.add("none");   
        document.getElementById("overlay").classList.remove("overlay"); 
    }
}

$(document).ready(function () {
    $('.h').click(function () {
        $('.i').focus();
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
    $('#button').click(function () {
        new_pass();
    });
});