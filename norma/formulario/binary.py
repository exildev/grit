from django.db import models
import struct

class ByteAField(models.Field):
	def db_type(self, connection):
		if connection.settings_dict['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
			return 'bytea'
		#end if
		raise Exception('ByteAField no soporta el motor "%s".' % (connection.settings_dict['ENGINE'],))
	#end def

	def get_prep_value(self, value):
		return u'%s' % (value, )
	#end def

	def to_python(self, value):
		return u'%s' % (value, )
	#end def

#end class
