window.sortables = [];

function sortable(callback){
	window.sortables.push(callback)
}

$( function() {
	$( '.sortable' ).sortable({
		'items': 'tbody.djn-item',
		stop: function( event, ui ) {
			for (var i = 0; i < window.sortables.length; i++) {
				window.sortables[i]();
			}
		}
	});
	$( '.sortable' ).disableSelection();
	$( '.sortable tbody.djn-item' ).css({'cursor': 'pointer'});
} );

