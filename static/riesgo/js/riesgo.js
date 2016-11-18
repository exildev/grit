var matriz = [
	['Bajo'    , 'Bajo'    , 'Moderado', 'Alto'   , 'Alto'   ],
	['Bajo'    , 'Bajo'    , 'Moderado', 'Alto'   , 'Extremo'],
	['Bajo'    , 'Moderado', 'Alto'    , 'Extremo', 'Extremo'],
	['Moderado', 'Alto'    , 'Alto'    , 'Extremo', 'Extremo'],
	['Alto'    , 'Alto'    , 'Extremo' , 'Extremo', 'Extremo']
];

$(document).ready(function (){
	var trs = $("table tbody tr");
	trs.each(function (index){
		make_edit($(this), index);
	});
});

function make_edit(tr, index){
	tr.find("label[for]").click(function (){
		var div = $(this).parent().find("div");
		dialogo(div, this);
	});
	tr.find("ul.errorlist").click(function (){
		var div = $(this).parent().find("div");
		var lab = $(this).parent().find("label[for]");
		dialogo(div, lab);
	});
	
	var probabilidad = tr.find('select[name="form-' + index + '-probabilidad"]');
	var consecuencia = tr.find('select[name="form-' + index + '-consecuencia"]');
	var estimacion   = tr.find('p.estimacion');

	probabilidad.change(function (){
		if (consecuencia.val()){
			var est = matriz[probabilidad.val() - 1][consecuencia.val() - 1];
			estimacion.text(est);
			estimacion.attr("color", est.toLocaleLowerCase())
		}
	});
	consecuencia.change(function (){
		if (probabilidad.val()){
			var est = matriz[probabilidad.val() - 1][consecuencia.val() - 1];
			estimacion.text(est);
			estimacion.attr("color", est.toLocaleLowerCase())
		}
	});

	if (consecuencia.val() && probabilidad.val()){
		var est = matriz[probabilidad.val() - 1][consecuencia.val() - 1];
		estimacion.text(est);
		estimacion.attr("color", est.toLocaleLowerCase())
	}

}

function dialogo(div, label){
	var dialog = div.clone().dialog({
		buttons:{
			Aceptar: function (){
				var val = $(this).find("textarea").val();
				$(label).text(val);
				div.find("textarea").text(val);
				$(this).dialog('close');
				$(this).dialog('destroy');
			},
			Cerrar: function (){
				$(this).dialog('close');
				$(this).dialog('destroy');
			}
		}
	});
}

