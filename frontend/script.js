/*Боковая панель*/
function openMenu() {
    document.getElementById("toolsbar").classList.toggle('active');
}
$('document').ready(function () {
    $('.network-map').append('<img src="img/device_icon.svg" alt="Устройство" title="Устройство" class="device-pic">');
    $('.network-map').append('<img src="img/switch_icon.svg" alt="Комутатор" title="Комутатор" class="switch-pic">');
    $('.network-map').append('<img src="img/server_icon.svg" alt="Сервер" title="Сервер" class="server-pic">');
});

