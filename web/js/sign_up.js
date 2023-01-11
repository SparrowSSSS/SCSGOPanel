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
        localStorage.setItem('user_email', email);
        let id = await eel.get__id(email)();
        sessionStorage.setItem('user_id', id);
    }
    else if (res == '0') {
        document.getElementById('result').innerHTML = "<p class='error'>Произошла техническая ошибка</p>";
    }
    else if (res == '2.1') {
        document.getElementById('result').innerHTML = "<p class='error'>Неверные данные</p>";
        document.getElementById('e').value = "";
        document.getElementById('p').value = "";
    }
    else if (res == '2.2') {
        document.getElementById('result').innerHTML = "<p class='error'>Неверные данные</p>";
        document.getElementById('p').value = "";
    }
    else {
        document.getElementById('result').innerHTML = "<p class='error'>Пользователь с данной почтой уже существует</p>";
        document.getElementById('e').value = "";
        document.getElementById('p').value = "";
    }
    document.getElementById("overlay").classList.remove("overlay");
    document.getElementById("overlay").classList.add("none");
}

$(document).ready(function () {
    if (localStorage.getItem('auto_sign_in') == "yes") {
        window.location.href = '../main.html';
    }
    $('.create_account').click(function () {
        sign_up();
    });
});