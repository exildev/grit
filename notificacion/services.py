"""from forms import PeriodicidadForm, RecordatorioForm, RecordatorioEditarForm, PeriodoForm, NotificableForm, RecordableForm, RevisionForm
from django.db import connection
import json

class NotificacionService():

	def mostrar_recordable(self, request, pk):
		recordable = Recordable.objects.filter(pk = pk).first()
		if recordable:
			return recordable
		#end if
		return False
	#end def

	def mostrar_notificable(self, request, pk):
		notificable = Notificable.objects.filter(pk = pk).first()
		if notificable:
			return notificable
		#end if
		return False
	#end def

	def panel_recordatorio(self, request, notificable):
		recordatorios = Recordatorio.objects.filter(notificable__pk=notificable)
		return recordatorios
	#end def

	def mostrar_recordatorio(self, request, pk):
		recordatorio = Recordatorio.objects.filter(pk = pk).first()
		if recordatorio:
			notificables = Notificable.objects.filter(recordatorios = recordatorio)
			return recordatorio, notificables
		#end if
		return False, None
	#end def

	def crear_periodicidad(self, request):
		form = PeriodicidadForm(request.POST)
		if form.is_valid():
			periodicidad = form.save()
			return form, periodicidad, True
		#end if
		return form, None, False
	#end def

	def crear_periodo(slef, recordatorio, periodicidad):
		periodo = Periodo(recordatorio=recordatorio, periodicidad=periodicidad)
		return periodo.save()
	#end def

	def form_crear_recordatorio(self, request):
		form_recordatorio = RecordatorioForm()
		form_periodicidad = PeriodicidadForm()
		return form_recordatorio, form_periodicidad
	#end def

	def crear_recordatorio(self, request, notificable):
		form = RecordatorioForm(request.POST)
		notificable = self.mostrar_notificable(request, notificable)
		if notificable:
			periodicidad_form, periodicidad, hecho = self.crear_periodicidad(request)
			if hecho:
				if form.is_valid():
					recordatorio = form.save()
					self.crear_periodo(recordatorio, periodicidad)
					notificable.recordatorios.add(recordatorio)
					return recordatorio, periodicidad, True
				#end if
			#end if
			print form.errors
			return form, periodicidad_form, False
		#end if
		return None, None, False
	#end def

	def form_editar_recordatorio(self, request, recordatorio):
		if request.POST:
			form = PeriodicidadForm(request.POST)
		else:
			recordatorio = recordatorio.periodicidad.last()
			form = PeriodicidadForm(instance=recordatorio)
		#end if
		return form
	#end def

	def editar_recordatorio(self, request, pk):
		recordatorio, notificable = self.mostrar_recordatorio(request, pk)
		if recordatorio:
			periodicidad, hecho = self.cambiar_periodicidad(request, recordatorio)
			return recordatorio, periodicidad, hecho
		#end if
		return recordatorio, None, False
	#end def

	def cambiar_periodicidad(self, request, recordatorio):
		form, periodicidad, hecho = self.crear_periodicidad(request)
		if hecho:
			self.crear_periodo(recordatorio, periodicidad)
			return periodicidad, True
		#end if
		return form, False
	#end if

	def mostrar_aviso(self, request, pk):
		aviso = Aviso.objects.filter(pk=pk).first()
		if aviso:
			return aviso
		#end if
		return False
	#end def

	def mostrar_avisos(self, request, recordable):
		avisos = Aviso.objects.raw("select * from crear_avisos(%s) as (id int, fecha_aviso  date, fecha_limite  date, recordable_id int, recordatorio_id int, fecha timestamp with time zone)"%(str(recordable),))
		return avisos
	#end def

	def mostrar_avisos_json(self, request, recordable):
		cursor = connection.cursor()
		try:
			cursor.callproc('crear_avisos_json', (recordable, ))
			result_set = cursor.fetchall()
			return result_set[0][0]
		finally:
			cursor.close()
		#end try
		return False
	#end def

	def revisar_aviso(self, request, aviso):
		return Revision(aviso = aviso).save()
	#end def
#end class"""