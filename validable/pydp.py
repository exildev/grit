import ctypes
from ctypes import cdll
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/asistencia/lib/'

class PyDP:
	DPFJ_FMD_ANSI_378_2004       = 0x001B0001 # ANSI INSITS 378-2004 Fingerprint Minutiae Data format 
	DPFJ_FMD_ISO_19794_2_2005    = 0x01010001 # ISO IEC 19794-2-2005 Fingerprint Minutiae Data format 
	DPFJ_FMD_DP_PRE_REG_FEATURES = 0          # deprecated DigitalPersona pre-registration feature set format 
	DPFJ_FMD_DP_REG_FEATURES     = 1          # deprecated DigitalPersona registration template format 
	DPFJ_FMD_DP_VER_FEATURES     = 2          # deprecated DigitalPersona verification feature set format 
	DPFJ_PROBABILITY_ONE 		 = 0x7fffffff # brief Normalized value when probability = 1

	def init(self):
		self.dpfpdd = cdll.LoadLibrary(os.path.join(BASE_DIR, 'libdpfpdd.so'))
		self.dpfj   = cdll.LoadLibrary(os.path.join(BASE_DIR, 'libdpfj.so'))
	#end def

	def validate(self, format1, feature1, format2, feature2):
		rate  = self.DPFJ_PROBABILITY_ONE / 1000000

		sizx1 = len(feature1)
		sizx2 = len(feature2)

		size1 = ctypes.c_uint(sizx1)
		size2 = ctypes.c_uint(sizx2)

		list1 = ctypes.c_ubyte * sizx1
		list2 = ctypes.c_ubyte * sizx2

		feat1 = list1(*feature1)
		feat2 = list2(*feature2)

		match = ctypes.c_int(22)

		print format1

		resp = self.dpfj.dpfj_compare(format1, feat1, size1, 1, format2, feat2, size2, 1, ctypes.byref(match))
		print "?", match.value, resp
		return match.value < rate
	#end def
#end class
