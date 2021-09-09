import libbit as convert
import libevents
import controlers.control2conf as conf

class FrameEvt():
	def __init__(self, frame, controler):
		if (controler == "MG3000"):
			self.evttype 		= frame[0] & 0xF1 >> 4
			self.serial 		= convert.fmtByte_to_Str(frame[1:3 + 1], separador='')
			self.date 			= libevents.get_date(frame[4:9 + 1],bcd=True)
			self.device 		= frame[10] >> 4
			self.sector			= (frame[10] & 0x0F) + 1
			self.receptor		= convert.bits2int(frame[14] , 5, 4) + 1
			self.info			= self.__info(frame[0], frame[15])

		if (controler == "CONTROL2"):
			self.evttype 		= frame[0] & 0x1F
			self.sector			= convert.bits2int(frame[0], 7, 5)
			self.mode			= convert.bits2int(frame[1], 7, 6)
			self.id_device		= convert.bits2int(frame[1], 5, 0) + 1
			self.device 		= frame[2] & 0x0F
			self.serial 		= convert.fmtByte_to_Str(frame[3:7 + 1], separador='')
			self.date 			= libevents.get_date(frame[8:13 + 1], bcd=False)
			self.receptor		= convert.bits2int(frame[14], 5, 4) + 1 
			self.info			= convert.bits2int(frame[15], 7, 4)

	def __info(self, evttype, b):
		evttype = (evttype & 0xF1) >> 4
		i = self.receptor - 1
		value = convert.onebit(b, i)
		info = "n/a"
		if (evttype == 0):
			if (b == 170):
				info = "Fora de Horario"
		return info