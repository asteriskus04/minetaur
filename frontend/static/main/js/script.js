/*Добавление элементов при загрузке страницы*/
$('document').ready(function () {
    $('.network-map').append('<img src="static/main/img/device_icon.svg" alt="Устройство" title="Устройство" class="device-pic">');
    $('.network-map').append('<img src="static/main/img/switch_icon.svg" alt="Комутатор" title="Комутатор" class="switch-pic">');
    $('.network-map').append('<img src="static/main/img/server_icon.svg" alt="Сервер" title="Сервер" class="server-pic">');

    var Renderer = function (canvas) {
        var canvas = $(canvas).get(0);
        var ctx = canvas.getContext("2d");
        var particleSystem;

        var that = {
            init: function (system) {
                //начальная инициализация
                particleSystem = system;
                particleSystem.screenSize(canvas.width, canvas.height);
                particleSystem.screenPadding(80);
                that.initMouseHandling();
            },

            redraw: function () {
                //действия при перересовке
                ctx.fillStyle = "white"; //белым цветом
                ctx.fillRect(0, 0, canvas.width, canvas.height); //закрашиваем всю область

                particleSystem.eachEdge( //отрисуем каждую грань
                    function (edge, pt1, pt2) { //будем работать с гранями и точками её начала и конца
                        ctx.strokeStyle = "rgba(10,10,10, .3)"; //грани будут чёрным цветом с некой прозрачностью
                        ctx.lineWidth = 5; //толщиной в один пиксель
                        ctx.beginPath();  //начинаем рисовать
                        ctx.moveTo(pt1.x, pt1.y); //от точки один
                        ctx.lineTo(pt2.x, pt2.y); //до точки два
                        ctx.stroke();
                    });

                particleSystem.eachNode( //теперь каждую вершину
                    function (node, pt) {  //получаем вершину и точку где она
                        var w = 40;   //ширина квадрата
                        ctx.fillStyle = "orange"; //с его цветом понятно
                        ctx.fillRect(pt.x - w / 2, pt.y - w / 2, w, w); //рисуем
                        //ctx.drawImage(SVGImageElement.href('img/switch_icon.svg'), pt.x - w / 2, pt.y - w / 2, w, w);
                        ctx.fillStyle = "black"; //цвет для шрифта
                        ctx.font = 'italic 13px sans-serif'; //шрифт
                        ctx.fillText(node.name, pt.x + 8, pt.y + 8); //пишем имя у каждой точки
                    });
            },

            initMouseHandling: function () { //события с мышью
                var dragged = null;   //вершина которую перемещают
                var handler = {
                    clicked: function (e) { //нажали
                        var pos = $(canvas).offset(); //получаем позицию canvas
                        _mouseP = arbor.Point(e.pageX - pos.left, e.pageY - pos.top); //и позицию нажатия кнопки относительно canvas
                        dragged = particleSystem.nearest(_mouseP); //определяем ближайшую вершину к нажатию
                        if (dragged && dragged.node !== null) {
                            dragged.node.fixed = true; //фиксируем её
                        }
                        $(canvas).bind('mousemove', handler.dragged); //слушаем события перемещения мыши
                        $(window).bind('mouseup', handler.dropped);  //и отпускания кнопки
                        return false;
                    },
                    dragged: function (e) { //перетаскиваем вершину
                        var pos = $(canvas).offset();
                        var s = arbor.Point(e.pageX - pos.left, e.pageY - pos.top);

                        if (dragged && dragged.node !== null) {
                            var p = particleSystem.fromScreen(s);
                            dragged.node.p = p; //тянем вершину за нажатой мышью
                        }

                        return false;
                    },
                    dropped: function (e) { //отпустили
                        if (dragged === null || dragged.node === undefined) return; //если не перемещали, то уходим
                        if (dragged.node !== null) dragged.node.fixed = false; //если перемещали - отпускаем
                        dragged = null; //очищаем
                        $(canvas).unbind('mousemove', handler.dragged); //перестаём слушать события
                        $(window).unbind('mouseup', handler.dropped);
                        _mouseP = null;
                        return false;
                    }
                }
                // слушаем события нажатия мыши
                $(canvas).mousedown(handler.clicked);
            },

        }
        return that;
    }

    $(document).ready(function () {
        sys = arbor.ParticleSystem(100); // создаём систему
        sys.parameters({ gravity: true }); // гравитация вкл
        sys.renderer = Renderer("#viewport") //начинаем рисовать в выбраной области

        $.getJSON("data.json", //получаем с сервера файл с данными
            function (data) {
                $.each(data.nodes, function (i, node) {
                    sys.addNode(node.name); //добавляем вершину
                });

                $.each(data.edges, function (i, edge) {
                    sys.addEdge(sys.getNode(edge.src), sys.getNode(edge.dest)); //добавляем грань
                });
            });

    })

});

/*Боковая панель*/
function openMenu() {
    document.getElementById("toolsbar").classList.toggle('active');
}