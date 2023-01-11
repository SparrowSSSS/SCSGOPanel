async function r() {
    let email = localStorage.getItem('user_email');
    let new_email = await eel.f_email(email)();
    let id = await eel.get__id(email)();
    let nickname = await eel.get__nickname(id)();
    document.getElementById('nickname').innerHTML = nickname;
    document.getElementById('email').innerHTML = new_email;
    document.getElementById('id').innerHTML = id;
}

$(document).ready(function () {
    if (localStorage.getItem('auto_sign_in') == "yes") {
        r();
    }
    $('#exit').click(function () {
        sessionStorage.removeItem('user_nickname');
        sessionStorage.removeItem('user_email');
        sessionStorage.removeItem('user_id');
        localStorage.removeItem('auto_sign_in');
        localStorage.removeItem('user_email');
    });
});