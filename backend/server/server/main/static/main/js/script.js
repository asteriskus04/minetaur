$('document').ready(function () {
    $('.help').hide();
    $('.about').hide();
    $('#network-table').hide();

    $("#hello_btn").click(function () {
    $('main').append('<section id="load"><img src="static/main/img/load.gif" alt="Анимация загрузки" class="load_anm"><p>Загрузка карты...</p></section>');
        $.ajax({

            method: "GET",
            url: "api/getmap",

            success: function (result) {

                $("#load").slideUp(300);
                $('.hello').remove();
                $('main').append('<button class="refr" onclick="refr();">Обновить карту</button>');
                $('main').append('<a href="data.json" download><button class="exp" onclick="exp();">Экспорт в файл</button></a>');
                $('main').append('<button class="change" onclick="change();">Сменить вид</button>');
                graph();
                console.log(result);
            }
        });

    });
})

function hide() {
    $('.help').fadeOut();
}
function show() {
    $('.help').fadeIn();
}

function hide_about() {
    $('.about').fadeOut();
}
function show_about() {
    $('.about').fadeIn();
}

var keys = [];
function getmap() {
    fetch('http://localhost:8000/api/getmap')
        .then(d => d.json())
        .then(json => {
            //Карта сети
            anychart.data.loadJson(json, function (data) {
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
                chart.background().fill("#A6B1E1");
                /*
                    chart.background().fill({
                        src: "/static/main/img/bg.svg",
                        mode: "stretch"
                    });
                */
            })
        })
        .catch(e => alert(e))
}
function graph() {

    //Карта сети
    anychart.data.loadJsonFile('static/main/js/data1.json', function (data) {
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
        chart.background().fill("#A6B1E1");
        /*
            chart.background().fill({
                src: "/static/main/img/bg.svg",
                mode: "stretch"
            });
        */
    })
}

function mkmp() {
    $('main').append('<section id="load"><img src="static/main/img/load.gif" alt="Анимация загрузки" class="load_anm"><p>Загрузка карты...</p></section>');
    $("#load").delay(5999).slideUp(300);
    $('.hello').remove();
    $('main').append('<button class="refr" onclick="refr();">Обновить карту</button>');
    $('main').append('<a href="data.json" download><button class="exp" onclick="exp();">Экспорт в файл</button></a>');
    $('main').append('<button class="change" onclick="change();">Сменить вид</button>');
    graph();
}

function change() {
    $('#network-map').toggle(); //включает/выключает элемент id="network-map"
    $('#network-table').toggle(); //включает/выключает элемент id="network-table"
    $('.refr').toggle();
}

// Обновление карты
function refr() {

    $('#network-map').remove();
    $('#load').remove();
    $('main').append('<section id="load"><img src="static/main/img/load.gif" alt="Анимация загрузки" class="load_anm"><p>Загрузка карты...</p></section>');
    $("#load").delay(99).slideUp();
    $('main').append('<div id="network-map">');
    graph();
}