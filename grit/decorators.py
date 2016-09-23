from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
import json

def datatable(searchs, columns=[], annotate=None, extras=None):
	def old(view):
		def new(request, **kwargs):
			table = view(request, **kwargs)
			return json_datatable(request, table, searchs, columns, annotate, extras)
		#end def
		return new
	#end def
	return old
#end def

def json_datatable(request, table, searchs, columns, annotate, extras):
	draw  = request.GET.get('draw', '1')
	start  = request.GET.get('start', '0')
	lenght = request.GET.get('length', '10')
	serach = request.GET.get('search[value]', '')
	order  = request.GET.get('order[0][column]', '0')
	ordir  = request.GET.get('order[0][dir]', '0')
	
	objects = table
	counter = 0
	q = Q()
	for column in searchs:
		kwargs = {
			'{0}__{1}'.format(column, 'icontains'): serach, 
		}
		q = Q(q | Q(**kwargs))
	#end for
	objects = objects.filter(q)
	if extras:
		objects = objects.extra(select=extras)
	#end if
	objects = objects.order_by((['-',''][ordir == 'desc']) + columns[int(order)])
	segment = objects[int(start):int(start)+int(lenght)]
	records_filtered = objects.count()
	records_total    = table.count()
	if annotate:
		segment = segment.annotate(**annotate)
	#end if
	data = list(segment.values(*columns))
	draw = int(draw) + 1
	dictionary = {'recordsFiltered':records_filtered , 'recordsTotal': records_total, 'data': data, 'draw': draw, 'da': lenght}
	return HttpResponse(json.dumps(dictionary), content_type="application/json")
#end def