$(function () {
    $("#load").delay(2999).slideUp(300);
});

$('document').ready(function () {
    $('.help').hide();
    $('.about').hide();
})

function hide() {
    $('.help').fadeOut();
}
function show() {
    $('.help').fadeIn(300);
}

function hide_about() {
    $('.about').fadeOut();
}
function show_about() {
    $('.about').fadeIn(300);
}

function exp() {
    alert('Эта функция скоро появится!');
}

var keys = [];

//Карта сети
anychart.data.loadJsonFile('data.json', function (data) {
    // создание графа из загруженных данных
    var chart = anychart.graph(data);

    // рисование графа
    chart.container("network-map").draw();

    // название графа вверху схемы
    chart.title(false);

    // подписи у точек
    chart.nodes().labels().enabled(false);
    chart.nodes().labels().format("{%id}");
    chart.nodes().labels().fontSize(12);
    chart.nodes().labels().fontWeight(600);

    // запрет на перемещение точек
    chart.interactivity().nodes(true);

    // запрет на зум
    chart.interactivity().zoomOnMouseWheel(true);
    // запрет на скролл по вертикали
    chart.interactivity().scrollOnMouseWheel(false);

    // угол наклона графа
    chart.rotation(30);

    // всплывающие окна у точек
    chart.nodes().tooltip().useHtml(true);
    chart.nodes().tooltip().format(
        "<span style='font-weight:bold; color:white;'>{%id}: {%status}</span><br><span style='color:white;'>IP-адрес: {%ip}<br>MAC-адрес: {%mac}</span>"
    );

    // подписи на рёбрах
    chart.edges().tooltip(false);

    // настройка отображения рёбер
    chart.edges().normal().stroke("#ffffff", 2);
    chart.edges().hovered().stroke("#ffa000", 2, "10 5");
    chart.edges().selected().stroke("#ffa000", 4);


    //настройка фона
    chart.background().fill("#797ba1");
    /*
        chart.background().fill({
            src: "/static/main/img/bg.svg",
            mode: "stretch"
        });
    */
})

// Обновление карты
function refr() {
    $('#network-map').remove();
    $('main').append('<div id="network-map">');

    anychart.data.loadJsonFile('data.json', function (data) {
        // создание графа из загруженных данных
        var chart = anychart.graph(data);

        // рисование графа
        chart.container("network-map").draw();

        // название графа вверху схемы
        chart.title(false);

        // подписи у точек
        chart.nodes().labels().enabled(false);
        chart.nodes().labels().format("{%id}");
        chart.nodes().labels().fontSize(12);
        chart.nodes().labels().fontWeight(600);

        // запрет на перемещение точек
        chart.interactivity().nodes(true);

        // запрет на зум
        chart.interactivity().zoomOnMouseWheel(true);
        // запрет на скролл по вертикали
        chart.interactivity().scrollOnMouseWheel(false);

        // угол наклона графа
        chart.rotation(30);

        // всплывающие окна у точек
        chart.nodes().tooltip().useHtml(true);
        chart.nodes().tooltip().format(
            "<span style='font-weight:bold; color:white;'>{%id}: {%status}</span><br><span style='color:white;'>IP-адрес: {%ip}<br>MAC-адрес: {%mac}</span>"
        );

        // подписи на рёбрах
        chart.edges().tooltip(false);

        // настройка отображения рёбер
        chart.edges().normal().stroke("#ffffff", 2);
        chart.edges().hovered().stroke("#ffa000", 2, "10 5");
        chart.edges().selected().stroke("#ffa000", 4);


        //настройка фона
        chart.background().fill("#797ba1");
        /*
            chart.background().fill({
                src: "/static/main/img/bg.svg",
                mode: "stretch"
            });
        */
        // fit the chart to the container

    })
}