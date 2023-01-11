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
        let id = await eel.get__id(email)();
        sessionStorage.setItem('user_id', id);
        let nickname = await eel.get__nickname(id)();
        sessionStorage.setItem('user_nickname', nickname);
    }
    else if (res == '0') {
        document.getElementById('result').innerHTML = "<p class='error'>Произошла техническая ошибка</p>";
    }
    else if (res == '2.1'){
        document.getElementById('result').innerHTML = "<p class='error'>Неверные данные</p>";
        document.getElementById('em').value = "";
        document.getElementById('p').value = "";
    }
    else {
        document.getElementById('result').innerHTML = "<p class='error'>Неверные данные</p>";
        document.getElementById('p').value = "";
    }
    document.getElementById("overlay").classList.remove("overlay");
    document.getElementById("overlay").classList.add("none");
}

$(document).ready(function () {
    $('.button__s_in').click(function () {
        sign_in();
    });
    $('.rec_pass').click(function () {
        sessionStorage.setItem('em-input_save', document.getElementById('em').value);
    });
});