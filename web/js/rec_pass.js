async function r_p_f() {
    document.getElementById("overlay").classList.remove("none");
    document.getElementById("overlay").classList.add("overlay");
    let email = document.getElementById('em').value;
    let res = await eel.change_pass(email)();
    if (res == '1') {
        document.getElementById('result').innerHTML = "<p id='rec_p'>На вашу почту было отправлено письмо с инструкциями</p>";
        localStorage.setItem('user_email', email);
        setTimeout(function() {
            window.location.href = '../new_p.html';      
            document.getElementById("overlay").classList.remove("overlay");
            document.getElementById("overlay").classList.add("none");           
        }, 10000);
    }
    else if (res == '0') {
        document.getElementById('result').innerHTML = "<p class='error'>Произошла техническая ошибка</p>";
        document.getElementById("overlay").classList.remove("overlay");
        document.getElementById("overlay").classList.add("none");
    }
    else {
        document.getElementById('result').innerHTML = "<p class='error'>Неверные данные</p>";
        document.getElementById('em').value = "";
        document.getElementById("overlay").classList.remove("overlay");
        document.getElementById("overlay").classList.add("none");
    }
}

$(document).ready(function () {
    $('#a').click(function () {
        sessionStorage.removeItem('em-input_save');
    });
    $('#button').click(function () {
        r_p_f();
    });
});