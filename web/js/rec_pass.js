$(document).ready(function () {
    $('.h').click(function () {
        $('.i').focus();
    });
    $('#a').click(function () {
        sessionStorage.removeItem('em-input_save');
    });
});