//Боковая панель
function openMenu() {
    document.getElementById("toolsbar").classList.toggle('active');
}

//Карта сети
anychart.data.loadJsonFile("static/main/js/data.json", function (data) {

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

    // configure the visual settings of edges
    chart.edges().normal().stroke("#364F6B", 2);
    chart.edges().hovered().stroke("#ffa000", 2, "10 5");
    chart.edges().selected().stroke("#ffa000", 4);

})