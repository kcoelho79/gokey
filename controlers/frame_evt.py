import libbit as convert
import libevents

class FrameEvt():
	def __init__(self, frame, controler):
		if (controler == "MG3000"):
			self.evttype 		= self.__evttype(frame[0])
			self.serial 		= self.__serial(frame[1:3 + 1])
			self.date 			= self.__date(frame[4:9 + 1])
			self.device 		= self.__device(frame[10])
			self.sector			= self.__sector(frame[10])
			self.receptor		= self.__receptor(frame[14])
			self.info			= self.__info(frame[0], frame[15])

	def __evttype(self, b):
		return  (b & 0xF1) >> 4

	def __serial(self, frame):
		return convert.fmtByte_to_Str(frame, separador='')

	def __date(self, frame):
		return libevents.get_date(frame)

	def __device(self, b):
		nibbleH = (b >> 4)
		if (nibbleH < 4):
			return nibbleH
		else:
			return 0

	def __sector(self, b): #porta can 
		return  (b & 0x0F) + 1

	
	def __receptor(self, b):
		value = convert.bits2int(b, 5, 4)  # bit2:1
		return value + 1

	def __info(self, evttype, b):
		evttype = (evttype & 0xF1) >> 4
		i = self.receptor - 1
		value = convert.onebit(b, i)
		info = "n/a"
		if (evttype == 0):
			if (b == 170):
				info = "Fora de Horario"
		return info
