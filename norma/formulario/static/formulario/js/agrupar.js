$(document).ready(function () {
	$("[group]").each(function(){
		var name = $(this).attr("group");
		var ver = $(this).attr("ver");
		console.log(name);
		var fieldset = $(this).parents("fieldset");
		var row = $(this).parents(".form-row");
		var group = fieldset.find("#"+name);
		if (group.size() == 0){
			group = $('<div id="' + name + '"></div>').appendTo(fieldset);
			group.append('<div class="form-row" style="text-align:center;width:100%"><h4>' + name + '</h4></div>');
		}
		if (ver == 'inline'){
			row.css({
				'float': 'left'
			});
		}else{
			row.css({
				'width': '100%'
			});
		}
		group.append(row);
	});
})