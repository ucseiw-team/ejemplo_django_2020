function on_boton_rellenar_click() {
    var div_resultados = $("#resultados");
    div_resultados.html("Por ahora resultados hardcodeados");
}

function on_boton_traer_html_click() {
    $.ajax({url: "/ajax/publicidad/"}).done(on_traer_resultados);
}

function on_traer_resultados(html) {
    var div_resultados = $("#resultados");
    div_resultados.html(html);
}


function on_boton_traer_datos_click() {
    $.ajax({url: "/ajax/cantidad_noticias/"}).done(on_resultados_ajax);
}


function on_resultados_ajax(data) {
    var div_resultados = $("#resultados");

    var texto_cantidades = "<p>Total de noticias: " + data["cantidad_total"].toString();
    if (data["hay_archivadas"]) {
        texto_cantidades = texto_cantidades + " <strong>(y hay archivadas)</strong></p>"; 
    } else {
        texto_cantidades = texto_cantidades + " <strong>(y no hay archivadas)</strong></p>"; 
    }

    div_resultados.html(texto_cantidades);
}


function on_pagina_cargada() {
    var boton_rellenar_datos = $("#boton-rellenar-datos");
    boton_rellenar_datos.bind("click", on_boton_rellenar_click);

    var boton_traer_html = $("#boton-traer-html");
    boton_traer_html.bind("click", on_boton_traer_html_click);

    var boton_traer_datos = $("#boton-traer-datos");
    boton_traer_datos.bind("click", on_boton_traer_datos_click);
}


$(on_pagina_cargada);
