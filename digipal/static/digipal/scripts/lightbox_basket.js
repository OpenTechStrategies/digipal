(function() {
	var csrftoken = getCookie('csrftoken');
	$.ajaxSetup({
		headers: {
			"X-CSRFToken": csrftoken
		}
	});

	$('#sort-select').bootstrapSelect({
		label: "Group By"
	});
})();

var cache = {};

var selectedItems = [];

var editorialCache = {};

var sum_images_collection = function(basket) {
	var n = 0;
	if (basket.annotations) {
		n += basket.annotations.length;
	}

	if (basket.images) {
		n += basket.images.length;
	}
	return n;
};

var selectedAnnotations = function() {
	var checkboxes = $('.checkbox_image');
	var graphs = {};
	var n = 0;
	$.each(checkboxes, function() {
		if ($(this).is(':checked')) {
			graphs[$(this).data('graph')] = $(this).data('type');
			n++;
		}
	});
	return {
		'graphs': graphs,
		'graphs_number': n
	};
};

function update_counter() {
	var checkboxes = $('.checkbox_image');
	var check_annotations_all = $('#check_annotations_all');
	var check_images_all = $('#check_images_all');
	var check_editorial_all = $('#check_editorial_all');
	var annotations = 0,
		images = 0,
		editorial = 0;

	$.each(checkboxes, function() {
		if ($(this).is(':checked')) {
			if ($(this).data('type') == 'image') {
				images++;
			} else if ($(this).data('type') == 'annotation') {
				annotations++;
			} else {
				editorial++;
			}
		}
	});

	$('#counter-annotations').html(annotations);
	$('#counter-images').html(images);
	$('#counter-editorial').html(editorial);

	if (!annotations) {
		check_annotations_all.prop('checked', false).prop('indeterminate', false);
	} else if ($('#table-annotations .table-row').length == annotations) {
		check_annotations_all.prop('checked', true).prop('indeterminate', false);
	} else {
		check_annotations_all.prop('indeterminate', true);
	}

	if (!images) {
		check_images_all.prop('checked', false).prop('indeterminate', false);
	} else if ($('#table-images .table-row').length == images) {
		check_images_all.prop('checked', true).prop('indeterminate', false);
	} else {
		check_images_all.prop('indeterminate', true);
	}

	if (!editorial) {
		check_editorial_all.prop('checked', false).prop('indeterminate', false);
	} else if ($('#table-editorial .table-row').length == editorial) {
		check_editorial_all.prop('checked', true).prop('indeterminate', false);
	} else {
		check_editorial_all.prop('indeterminate', true);
	}

	if (!selectedItems.length) {
		$('#remove_from_collection').attr('disabled', true);
		//$('#to_lightbox').attr('disabled', true);
	} else {
		$('#remove_from_collection').attr('disabled', false);
		//$('#to_lightbox').attr('disabled', false);
	}


	$("#header_annotations").add($("#annotations-grid h2")).html("Graphs (" + $('#table-annotations').find('tr[data-graph]').length + ")");
	$("#header_editorial").add($("#editorial-grid h2")).html("Editorial Annotations (" + $('#table-editorial').find('tr[data-graph]').length + ")");
	$("#header_images").add($("#images-grid h2")).html("Images (" + $('#table-images').find('tr[data-graph]').length + ")");

}

var changeNumbers = function() {
	var tbody = $("tbody");
	tbody.find('tr').each(function() {
		$(this).find('.num_row').text('#' + $(this).index());
	});
};

function main() {

	var element_basket = $('#collection_link');
	var container_basket = $('#container_basket');
	var collection, collection_name, data = {};
	var isExternal = false;

	if (!getParameter('collection').length) {
		var collections = JSON.parse(localStorage.getItem('collections'));
		var url = location.href;
		var collection_name_from_url = decodeURIComponent(url.split('/')[url.split('/').length - 2]);
		var selectedCollection = localStorage.getItem('selectedCollection');

		$.each(collections, function(index, value) {
			if (index.replace(/\s+/gi, '').toLowerCase() == collection_name_from_url.toLowerCase()) {
				collection = value;
				collection_name = index;
			}
		});

		if (!collection) {
			location.href = "../";
		}

		var graphs = [],
			images = [],
			editorial = [];

		if (typeof collection.annotations !== 'undefined' && collection.annotations.length) {
			for (var i = 0; i < collection.annotations.length; i++) {
				graphs.push(collection.annotations[i]);
			}
			data.annotations = graphs;
		}

		if (typeof collection.images !== 'undefined' && collection.images.length) {
			for (d = 0; d < collection.images.length; d++) {
				if (typeof collection.images[d] != 'number') {
					images.push(parseInt(collection.images[d].id, 10));
				} else {
					images.push(parseInt(collection.images[d], 10));
				}
			}
			data.images = images;
		}

		if (typeof collection.editorial !== 'undefined' && collection.editorial.length) {
			for (d = 0; d < collection.editorial.length; d++) {
				editorial.push(collection.editorial[d]);
			}
			data.editorial = editorial;
		}

	} else {
		/*
		var external_collection = JSON.parse(getParameter('collection'));
		data = external_collection;
		collection_name = data['name'];
		collection = data;
		isExternal = true;
		*/

		// GN: hack here to unescape the param, although it should already have been unescaped in GetParam
		// so I imagine the param has been escaped twice before...
		var collection_param = getParameter('collection');
		if (collection_param.length) {
			collection_param = collection_param[0];
			if (collection_param.lastIndexOf('%', 0) === 0) {
				collection_param = unescape(collection_param);
			}
			var external_collection = JSON.parse(collection_param);

			data = external_collection;
			collection_name = data['name'];
			collection = data;
			isExternal = true;
		}

	}

	var header = $('.page-header');
	header.find('.collection-title').html(collection_name);
	$('#breadcrumb-current-collection').html(collection_name);
	var length_basket = length_basket_elements(collection) || 0;
	$('#delete-collection').attr('data-original-title', 'Delete ' + collection_name);
	$('#share-collection').attr('data-original-title', 'Share ' + collection_name);
	var url_request = '/digipal/collection/' + collection_name.replace(/\s*/gi, '') + '/images/';
	if (!$.isEmptyObject(data)) {

		var request = $.ajax({
			type: 'GET',
			url: url_request,
			contentType: 'application/json',
			data: {
				'data': JSON.stringify(data)
			},
			success: function(data) {
				var attrs = {
					"isExternal": isExternal,
					"reverse": true
				};
				displayTable(data, attrs);


				displayGrid(data, {
					'sorting': 11
				});

			},

			complete: function() {
				var loading_div = $(".loading-div");
				if (loading_div.length) {
					loading_div.fadeOut().remove();
				}
				$('#close-alert').unbind().click(function() {
					$('#alert-save-collection').fadeOut().remove();
				});

				$('#save-collection').unbind().click(function() {
					save_collection(collection);
					$('#alert-save-collection').fadeOut().remove();
					notify('Collection successfully saved', 'success');
				});
			},

			error: function() {

				var s = '<div class="container alert alert-warning">Something has gone wrong. Please refresh the page and try again.</div>';
				container_basket.html(s);

				var loading_div = $(".loading-div");
				if (loading_div.length) {
					loading_div.fadeOut().remove();
				}
			}
		});

	} else {
		s = '<div class="container alert alert-warning"><p>The collection is empty.</p>';
		s += '<p>Start adding images from <a href="/digipal/page">Browse Images</a> or using the DigiPal <a href="/digipal/search/?from_link=true">search engine</a></div>';

		container_basket.html(s);

		var loading_div = $(".loading-div");
		if (loading_div.length) {
			loading_div.fadeOut().remove();
		}
	}

	$('#delete-collection').add($('#share-collection')).tooltip();

	header.find('.collection-title').on('blur', function() {
		if (!$(this).data('active')) {
			$(this).data('active', true);
			var collections = JSON.parse(localStorage.getItem('collections'));
			var name = $.trim($(this).text()),
				flag = false;

			$.each(collections, function(index, value) {
				if (name == index) {
					flag = false;
					return false;
				} else {
					if (value.id == selectedCollection) {
						//name = name.replace(/\s+/gi, '');
						if (name && name.length <= 30) {
							collections[name] = collections[index];
							delete collections[index];
							basket = value;
							history.pushState(null, null, '../' + encodeURIComponent(name));
							flag = true;
							return false;
						} else {
							notify("Ensure the name entered doesn't contain special chars, nor exceeds 30 chars", 'danger');
							$('.collection-title').html(index);
							return false;
						}
					}
				}
			});

			if (flag) {
				localStorage.setItem('collections', JSON.stringify(collections));
				element_basket.html(name + ' (' + sum_images_collection(basket) + ' <i class="fa fa-picture-o"></i> )');
				element_basket.attr('href', '/digipal/collection/' + name.replace(/\s+/gi), '');
				$('#breadcrumb-current-collection').html(name);
				notify("Collection renamed as " + name, 'success');
			} else {
				return false;
			}
		}
	}).on('focus', function(event) {
		$(this).on('keyup', function(event) {
			var code = (event.keyCode ? event.keyCode : event.which);
			if (code == 13) {
				$(this).blur();
				event.preventDefault();
				return false;
			}
		}).on('keydown', function(event) {
			var code = (event.keyCode ? event.keyCode : event.which);
			if (code == 13) {
				$(this).blur();
				event.preventDefault();
				return false;
			}
		}).data('active', false);
	});

	$('#share-collection').on('click', function() {
		share([collection['id']]);
	});

	$('#delete-collection').on('click', function() {
		delete_collections([collection['id']], false, true);
	});
}

function sort(property, reverse, type) {
	property = parseInt(property, 10);
	var copy_cache = $.extend({}, cache);

	copy_cache[type].sort(function(x, y) {
		return x[property] == y[property] ? 0 : (x[property] < y[property] ? -1 : 1);
	});

	if (reverse) {
		copy_cache[type].reverse();
	}

	var attrs = {
		"isExternal": false,
		"reverse": reverse
	};

	displayTable(copy_cache, attrs);
}

function displayTable(data, attrs) {
	var container_basket = $('#container_basket');
	var isExternal = attrs.isExternal;
	var reverse = attrs.reverse;
	var s = '';

	if (data.annotations && data.annotations.length) {
		if (!cache.annotations) {
			cache.annotations = data.annotations;
		}
		s += "<h3 id='header_annotations'>Graphs (" + data.annotations.length + ")</h3>";
		s += "<table id='table-annotations' class='table'>";
		s += '<th><span id="counter-annotations"></span><input data-toggle="tooltip" title="Toggle all" type="checkbox" id="check_annotations_all" /></th><th>Graph</th><th data-sort="14" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Manuscript</th><th data-sort="11" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Allograph</td><th data-sort="3" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Hand</th><th data-sort="4" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Scribe</th><th data-sort="5" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Place</th>';
		for (var i = 0; i < data.annotations.length; i++) {
			var annotation = data.annotations[i];
			s += "<tr class='table-row' data-graph = '" + annotation[1] + "'><td><input data-toggle='tooltip' title='Toggle item' data-graph = '" + annotation[1] + "' type='checkbox' data-type='annotation' class='checkbox_image' /> <span class='num_row'># " + (i + 1) + "</span>  </td><td data-graph = '" + annotation[1] + "'><a title='Inspect letter in manuscript viewer' href='/digipal/page/" + annotation[8] + "/?graph=" + annotation[1] + "'>" + annotation[0] + "</a>";
			s += "</td>";

			s += "<td data-graph = '" + annotation[1] + "'><a data-toggle='tooltip' title='Go to manuscript page' href='/digipal/page/" + annotation[8] + "'>" + annotation[14] + "</a>";
			s += "</td>";

			s += "<td><a data-toggle='tooltip' title='Go to " + annotation[11] + "' href='/digipal/search/graph/?character_select=" + annotation[13] + "&allograph_select=" + annotation[12] + "'>" + annotation[11] + "</a></td>";

			if (annotation[3] !== null && annotation[3] != 'Unknown') {
				s += "<td><a data-toggle='tooltip' title='Go to Hand' href='/digipal/hands/" + annotation[9] + "'>" + annotation[3] + "</a></td>";
			} else {
				s += "<td>Unknown</td>";
			}


			if (annotation[4] !== null && annotation[4] != 'Unknown') {
				s += "<td><a data-toggle='tooltip' title = 'Go to Scribe' href='/digipal/scribes/" + annotation[10] + "'>" + annotation[4] + "</a></td>";
			} else {
				s += "<td>Unknown</td>";
			}

			if (annotation[5] !== null && annotation[5] != 'Unknown') {
				s += "<td><a data-toggle='tooltip' title = 'Explore manuscripts in " + annotation[5] + "' href='/digipal/page/?town_or_city=" + annotation[5] + "'>" + annotation[5] + "</a></td>";
			} else {
				s += "<td>Unknown</td>";
			}

			/*if (annotation[6] !== null && annotation[6] != 'Unknown') {
							s += "<td><a title = 'Explore manuscripts written in " + annotation[6] + "' href='/digipal/page/?date=" + annotation[6] + "'>" + annotation[6] + "</a></td>";
						} else {
							s += "<td>Unknown</td>";
						}*/

		}
	}

	s += "</table>";

	if (data.images && data.images.length) {
		if (!cache.images) {
			cache.images = data.images;
		}
		s += "<h3 id ='header_images'>Images (" + data.images.length + ")</h3>";
		s += "<table id='table-images' class='table'>";
		s += '<th><span id="counter-images"></span> <input data-toggle="tooltip" title="Toggle all" type="checkbox" id="check_images_all" /></th><th>Page</th><th data-sort="0" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Label</td><th data-sort="3" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Hand</th>';
		for (i = 0; i < data['images'].length; i++) {

			var image = data['images'][i];
			s += "<tr data- class='table-row' data-graph = '" + image[1] + "'><td><input data-toggle='tooltip' title='Toggle item' data-graph = '" + image[1] + "' type='checkbox' data-type='image' class='checkbox_image' /> <span class='num_row'># " + (i + 1) + "</span>  <td data-graph = '" + image[1] + "'><a data-toggle='tooltip' title ='See manuscript' href='/digipal/page/" + image[1] + "'>" + image[0] + "</a></td>";
			s += "<td data-graph = '" + image[1] + "'><a data-toggle='tooltip' title ='See manuscript' href='/digipal/page/" + image[1] + "'>" + image[2] + "</a></td>";
			s += "<td>" + image[3] + "</td>";
		}
		s += "</table>";
	}

	if (data.editorial && data.editorial.length) {
		s += "<h3 id='header_editorial'>Editorial Annotations (" + data.editorial.length + ")</h3>";
		s += "<table id='table-editorial' class='table'>";
		s += '<th><span id="counter-editorial"></span> <input data-toggle="tooltip" title="Toggle all" type="checkbox" id="check_editorial_all" /></th><th>Annotation</th><th data-sort="3" data-reverse="' + reverse + '"><span class="glyphicon glyphicon-sort-by-attributes-alt small"></span> Page</th><th>Public Note</th>';
		if (!cache.editorial) {
			cache.editorial = data.editorial;
		}

		for (i = 0; i < data['editorial'].length; i++) {

			var editorial_annotation = data['editorial'][i];
			s += "<tr class='table-row' data-graph = '" + editorial_annotation[2] + "'><td><input data-toggle='tooltip' title='Toggle item' data-graph = '" + editorial_annotation[2] + "' type='checkbox' data-type='editorial' class='checkbox_image' /> <span class='num_row'># " + (i + 1) + "</span>  </td><td data-graph = '" + editorial_annotation[2] + "'><a title='Inspect letter in manuscript viewer' href='/digipal/page/" + editorial_annotation[1] + "/?vector_id=" + editorial_annotation[2] + "'>" + editorial_annotation[0] + "</a>";
			s += "</td>";

			s += "<td data-graph = '" + editorial_annotation[2] + "'><a data-toggle='tooltip' title='Go to manuscript page' href='/digipal/page/" + editorial_annotation[2] + "'>" + editorial_annotation[3] + "</a>";
			s += "</td>";

			if (typeof isAdmin !== 'undefined' && isAdmin) {
				s += "<td data-graph = '" + editorial_annotation[2] + "'><div class='public-note'>" + editorial_annotation[4].substring(0, 50) + " ... </div> <button class='btn-link read-more' data-image='" + editorial_annotation[1] + "' data-id = '" + editorial_annotation[2] + "'>Read and Edit</button>";
			} else {
				if (editorial_annotation[4].length > 50) {
					s += "<td data-graph = '" + editorial_annotation[2] + "'><div class='public-note'>" + editorial_annotation[4].substring(0, 50) + " ... </div><button class='btn-link read-more' data-image='" + editorial_annotation[1] + "' data-id = '" + editorial_annotation[2] + "'>Read more</button>";
				} else {
					s += "<td data-graph = '" + editorial_annotation[2] + "'><div class='public-note'>" + editorial_annotation[4] + "</div>";
				}
			}
			s += "</td>";
		}
		s += "</table>";
	}

	if (isExternal) {
		var alert_string = "<div id='alert-save-collection' class='alert alert-success'>This is an external collection. Do you want to save it?  <div class='pull-right'><input type='button' id='save-collection' class='btn btn-xs btn-success' value='Save' /> <input id='close-alert' type='button' class='btn btn-xs btn-danger' value='Close' /></div> </div>";
		s = alert_string + s;
	}

	container_basket.html(s);

	update();

	launchEvents();
}

function groupManuscripts(annotations) {
	var manuscripts = {};
	var n = 0;
	for (var i = 0; i < annotations.length; i++) {
		if (!manuscripts[annotations[i][14]]) {
			n++;
			manuscripts[annotations[i][14]] = n;
		}
	}
	return manuscripts;
}

function displayGrid(data, attrs) {
	var manuscripts = groupManuscripts(data.annotations);
	var container = $('#grid');
	var s = '';

	data.annotations = data.annotations.sort(function(x, y) {
		return x[attrs.sorting] == y[attrs.sorting] ? 0 : (x[attrs.sorting] < y[attrs.sorting] ? -1 : 1);
	});

	s += "<div id='manuscripts-index'>";
	if (data.annotations && data.annotations.length) {
		for (var manuscript in manuscripts) {
			s += "<p class='manuscript-index'>" + manuscripts[manuscript] + ") " + manuscript + "</p>";
		}
	}
	s += "</div>";

	if (data.annotations && data.annotations.length) {
		s += "<div id='annotations-grid' class='panel'>";
		s += "<h2>Graphs (" + data.annotations.length + ")</h2>";
		for (var i = 0; i < data.annotations.length; i++) {

			if (!i || (data.annotations[i][attrs.sorting] !== data.annotations[i - 1][attrs.sorting])) {
				s += "<h3>" + data.annotations[i][attrs.sorting] + "</h3>";
				s += "<div class='grid-images'>";
			}

			s += "<div class='grid-image' data-graph='" + data.annotations[i][1] + "'><span class='manuscript-number'>" + manuscripts[data.annotations[i][14]] + "</span>" + data.annotations[i][0] + "</div>";

			if (!data.annotations[i + 1] || (data.annotations[i][attrs.sorting] !== data.annotations[i + 1][attrs.sorting])) {
				s += "</div>";
			}
		}
		s += "</div>";
	}

	if (data.images && data.images.length) {
		s += "<div id='images-grid' class='panel'>";
		s += "<h2>Images (" + data.images.length + ")</h2>";
		for (var i = 0; i < data.images.length; i++) {

			if (!i || (data.images[i][2] !== data.images[i - 1][2])) {
				s += "<h3>" + data.images[i][2] + "</h3>";
				s += "<div class='grid-images'>";
			}

			s += "<div class='grid-image' data-graph='" + data.images[i][1] + "'>" + data.images[i][0] + "</div>";

			if (!data.images[i + 1] || (data.images[i][2] !== data.images[i + 1][2])) {
				s += "</div>";
			}
		}
		s += "</div>";
	}

	if (data.editorial && data.editorial.length) {
		s += "<div id='editorial-grid' class='panel'>";
		s += "<h2>Editorial Annotations (" + data.editorial.length + ")</h2>";
		for (var i = 0; i < data.editorial.length; i++) {
			editorialCache[data.editorial[i][2]] = data.editorial[i][4];
			if (!i || (data.editorial[i][3] !== data.editorial[i - 1][3])) {
				s += "<h3>" + data.editorial[i][3] + "</h3>";
				s += "<div class='grid-images'>";
			}

			s += "<div class='grid-image' data-graph='" + data.editorial[i][2] + "'><span class='manuscript-number'>" + manuscripts[data.editorial[i][3]] + "</span>" + data.editorial[i][0] + "</div>";

			if (!data.editorial[i + 1] || (data.editorial[i][3] !== data.editorial[i + 1][3])) {
				s += "</div>";
			}
		}
		s += "</div>";
	}

	container.html(s);

	$('.grid-image').on('click', function() {
		var graph = $(this).data('graph');
		if ($(this).find('img').hasClass('selected') && selectedItems.indexOf(graph) >= 0) {
			selectedItems.splice(selectedItems.indexOf(graph), 1);
			$(this).find('img').removeClass('selected');
		} else {
			if (selectedItems.indexOf(graph) < 0) {
				selectedItems.push(graph);
			}
			$(this).find('img').addClass('selected');
		}
		update_counter();
	});

	$('.grid-images').sortable();
	update_counter();
	update();
}

function launchEvents() {
	update_counter();
	$('#check_images_all').unbind().on('change', function() {
		if ($(this).is(':checked')) {
			$('#table-images').find('input[type="checkbox"]').prop('checked', true);
			$('#table-images').find('.table-row').addClass('selected').each(function() {
				selectedItems.push($(this).data('graph'));
			});
		} else {
			$('#table-images').find('input[type="checkbox"]').prop('checked', false);
			$('#table-images').find('.table-row').removeClass('selected').each(function() {
				selectedItems.splice(selectedItems.indexOf($(this).data('graph')), 1);
			});
		}
		update_counter();
	});

	$('#check_annotations_all').unbind().on('change', function() {
		if ($(this).is(':checked')) {
			$('#table-annotations').find('input[type="checkbox"]').prop('checked', true);
			$('#table-annotations').find('.table-row').addClass('selected').each(function() {
				selectedItems.push($(this).data('graph'));
			});
		} else {
			$('#table-annotations').find('input[type="checkbox"]').prop('checked', false);
			$('#table-annotations').find('.table-row').removeClass('selected').each(function() {
				selectedItems.splice(selectedItems.indexOf($(this).data('graph')), 1);
			});
		}
		update_counter();
	});

	$('#check_editorial_all').unbind().on('change', function() {
		if ($(this).is(':checked')) {
			$('#table-editorial').find('input[type="checkbox"]').prop('checked', true);
			$('#table-editorial').find('.table-row').addClass('selected').each(function() {
				selectedItems.push($(this).data('graph'));
			});
		} else {
			$('#table-editorial').find('input[type="checkbox"]').prop('checked', false);
			$('#table-editorial').find('.table-row').removeClass('selected').each(function() {
				selectedItems.splice(selectedItems.indexOf($(this).data('graph')), 1);
			});
		}
		update_counter();
	});

	$('th[data-sort]').unbind().on('click', function() {
		var reverse = !$(this).data('reverse');
		$(this).data('reverse', reverse);
		sort($(this).data('sort'), $(this).data('reverse'), $(this).closest('table').attr('id').split('-')[1]);
	});

	$('#remove_from_collection').on('click', function() {

		var basket;
		var selectedCollection = localStorage.getItem('selectedCollection');
		var collections = JSON.parse(localStorage.getItem('collections'));
		$.each(collections, function(index, value) {
			if (value.id == selectedCollection) {
				basket = value;
				basket.name = index;
				basket.id = value.id;
			}
		});

		if (!$(".loading-div").length) {
			var loading_div = $("<div class='loading-div'>");
			var background = $("<div class='dialog-background'>");
			loading_div.html('<h2>Removing images</h2>');
			loading_div.append("<p>You are about to remove " + selectedItems.length + " images. Continue?");
			loading_div.append("<p><button class='btn btn-success btn-sm' id='remove_images_from_collection'>Remove</button> <button class='btn btn-danger btn-sm' id='cancel'>Cancel</button></p>");
			background.append(loading_div);
			$('body').append(background);
		}

		$('#remove_images_from_collection').unbind().on('click', function() {
			for (var j = 0; j < selectedItems.length; j++) {
				for (var i in basket) {
					if (basket[i] instanceof Array) {
						if (basket[i].indexOf(selectedItems[j]) >= 0) {
							if (i == "editorial") {
								selectedItems[j] = selectedItems[j].toString();
							}
							basket[i].splice(basket[i].indexOf(selectedItems[j]), 1);
							$('[data-graph="' + selectedItems[j] + '"]').fadeOut().remove();
							selectedItems.splice(j, 1);
							j--;
						}
					}
				}
			}
			cache = basket;

			update_counter();

			if (!sum_images_collection(basket)) {
				var s = '<div class="container alert alert-warning"><p>The collection is empty.</p>';
				s += '<p>Start adding images from <a href="/digipal/page">Browse Images</a> or using the DigiPal <a href="/digipal/search/?from_link=true">search engine</a></div>';
				container_basket.html(s);
			}

			localStorage.setItem('collections', JSON.stringify(collections));
			background.fadeOut().remove();
			update_collection_counter();
			changeNumbers();
		});

		$('#cancel').unbind().on('click', function() {
			background.fadeOut().remove();
		});

	});


	var print = $('#print');
	print.on('click', function() {
		var tab = $('.tab-pane.active').attr('id');
		location.href = location.href + '?view=print&tab=' + tab;
	});

	$('#to_lightbox').unbind().on('click', function() {
		var graphs = [],
			images = [],
			editorial_annotations = [],
			element,
			basket;

		var selectedCollection = localStorage.getItem('selectedCollection');
		var collections = JSON.parse(localStorage.getItem('collections'));

		$.each(collections, function(index, value) {
			if (value.id == selectedCollection) {
				basket = value;
			}
		});

		if (basket && basket.annotations && basket.annotations.length) {
			for (i = 0; i < basket.annotations.length; i++) {
				if (basket.annotations[i].hasOwnProperty('graph')) {
					element = basket.annotations[i].graph;
				} else {
					element = basket.annotations[i];
				}
				if ($('input[type="checkbox"][data-graph="' + element + '"]').is(':checked')) {
					graphs.push(element);
				}
			}
		}
		if (basket && basket.images && basket.images.length) {
			for (i = 0; i < basket.images.length; i++) {
				element = basket.images[i];
				if ($('input[type="checkbox"][data-graph="' + element + '"]').is(':checked')) {
					images.push(element);
				}
			}
		}
		if (basket && basket.editorial && basket.editorial.length) {
			for (i = 0; i < basket.editorial.length; i++) {
				element = basket.editorial[i].toString();
				if ($('input[type="checkbox"][data-graph="' + basket.editorial[i][0] + '"]').is(':checked')) {
					editorial_annotations.push(element);
				}
			}
		}
		location.href = '/lightbox/?annotations=[' + graphs.toString() + ']&images=[' + images.toString() + ']&editorial=[ ' + editorial_annotations + ' ]&from=' + location.pathname;
	});

	$('tr.table-row').unbind().on('click', function(event) {

		var checkbox = $(this).find('.checkbox_image');

		if ($(this).hasClass('selected') && selectedItems.indexOf($(this).data('graph')) >= 0) {
			$(this).removeClass('selected');
			checkbox.prop('checked', false);
			selectedItems.splice(selectedItems.indexOf($(this).data('graph')), 1);
		} else {
			$(this).addClass('selected');
			checkbox.prop('checked', true);
			if (selectedItems.indexOf($(this).data('graph')) < 0) {
				selectedItems.push($(this).data('graph'));
			}
		}
		update_counter();
		event.stopPropagation();
		event.stopImmediatePropagation();
	});

	var editCollection = function(el) {
		var _collections = JSON.parse(localStorage.getItem('collections')),
			_basket;

		var list, type, new_list = [];

		$.each(_collections, function(index, value) {
			if (value.id == selectedCollection) {
				_basket = value;
				_basket['name'] = index;
			}
		});

		$.each($('tr[data-graph]'), function() {
			new_list.push($(this).data('graph'));
		});

		if (el.closest('table').attr('id') == 'table-annotations') {
			_basket['annotations'] = new_list;
		} else {
			_basket['images'] = new_list;
		}

		localStorage.setItem('collections', JSON.stringify(_collections));
	};

	var makeSortable = function() {
		var item_index, target_index;
		$("tbody").sortable({
			items: "tr[data-graph]",
			update: function(event, ui) {
				changeNumbers();
				editCollection(ui.item);
			}
		});
	};

	makeSortable();



	$('.read-more').unbind().on('click', function(event) {

		if ($('.dialog-background').length) {
			$('.dialog-background').remove();
		}
		var image = $(this).data('image');
		var id = $(this).data('id');
		var background = $("<div class='dialog-background'>");
		var windowGraph = $("<div class='editorial-annotation-div'>");
		var title = $("<p class='editorial-annotation-title'>Editorial Annotation <span class='pull-right'><span style='cursor:pointer' class='fa fa-times' title='Close' data-toggle='tooltip'></span></span></p>");
		windowGraph.append(title);
		if (typeof isAdmin !== 'undefined' && isAdmin) {
			title.find('.pull-right').prepend("<span title='Edit' data-toggle='tooltip' style='cursor:pointer' class='fa fa-pencil-square-o'></span> <span title='Save' data-toggle='tooltip' style='cursor:pointer' class='fa fa-check-square'></span> ");
		}
		var content = $("<p class='editorial-annotation-content'>");
		var value = editorialCache[id];
		content.append(value);
		windowGraph.append(content);
		background.append(windowGraph);
		$('body').append(background);

		windowGraph.on('click', function(event) {
			event.stopPropagation();
		});

		background.on('click', function(event) {
			$(this).remove();
			event.stopPropagation();
		});

		title.find('.fa-times').on('click', function() {
			background.remove();
			event.stopPropagation();
		});

		title.find('.fa-pencil-square-o').on('click', function() {
			content.attr('contenteditable', true).focus();
			event.stopPropagation();
		});

		title.find('.fa-check-square').on('click', function() {

			var data = {
				'display_note': content.html()
			};

			var url_data = {};
			url_data.image = image;
			url_data.id = id.toString();

			$.ajax({
				type: 'POST',
				url: '/digipal/api/graph/save_editorial/' + JSON.stringify([url_data]) + '/',
				data: data,
				success: function(data) {
					if (data.success) {
						notify("Annotation successfully saved", "success");
						var value = data.graphs[0].display_note;
						if (value.length > 50) {
							value = value.substring(0, 50) + '...';
						}
						$('td[data-graph="' + id + '"]').find('.public-note').html(value);
						editorialCache[id] = data.graphs[0].display_note;
					} else {
						if (data.errors.length) {
							notify("Annotation not saved", "danger");
						}
					}
				},
				error: function(data) {
					console.warn(data);
				}
			});
			event.stopPropagation();
		});

		$('[data-toggle="tooltip"]').tooltip();
		event.stopPropagation();
	});

	update();

	$('[data-toggle="tooltip"]').tooltip();
}

$(document).ready(function() {

	$('a[data-toggle="pill"]').on('shown.bs.tab', function(e) {
		if (e.target.getAttribute('data-target') == "#table") {
			$('#select-sort-select').attr('disabled', true);
		} else {
			$('#select-sort-select').attr('disabled', false);
		}
		update();
	});
	$('#select-sort-select').attr('disabled', true);
	$('#sort-select').attr('disabled', true).on('change', function() {
		displayGrid(cache, {
			'sorting': $(this).val()
		});
	});

	main();

	var print_view = getParameter('view');
	var tab = getParameter('tab');
	if (print_view.length && print_view[0] == 'print') {
		if (tab[0]) {
			$('[data-target="#' + tab[0] + '"]').tab('show');
		}
		$('[media="print"]').attr('media', 'screen');
	}

	$(window).bind('storage', function(e) {
		main();
		update_counter();
		update_collection_counter();
	});
});


function update() {
	$("tr[data-graph]").each(function() {
		var graph = $(this).data('graph');
		if (selectedItems.indexOf(graph) >= 0) {
			$(this).addClass('selected');
			$(this).find('.checkbox_image').prop('checked', true);
		} else {
			$(this).removeClass('selected');
			$(this).find('.checkbox_image').prop('checked', false);
		}
	});

	$(".grid-image").each(function() {
		var graph = $(this).data('graph');
		if (selectedItems.indexOf(graph) >= 0) {
			$(this).find('img').addClass('selected');
		} else {
			$(this).find('img').removeClass('selected');
		}
	});

	update_counter();
}