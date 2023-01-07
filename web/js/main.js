$(document).ready(function () {
    $('#exit').click(function () {
        sessionStorage.removeItem('user_nickname');
        sessionStorage.removeItem('user_email');
        sessionStorage.removeItem('user_id');
        localStorage.removeItem('auto_sign_in');
        localStorage.removeItem('user_nickname');
        localStorage.removeItem('user_email');
        localStorage.removeItem('user_id');
    });
});