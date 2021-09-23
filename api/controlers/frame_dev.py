class FrameDev():
	def __init__(self, frame):
		self.frame = frame
		if (controler == "MG3000"):
			self.device = frame[0]
			self.serial = frame[1:3 +1]
			self.cont_hl = frame[4:5]
			self.unid_h	 = frame[6]
			self.unid_l = frame [7]
			self.unid = self.unid_h + self.unid_l
			self.bloco = frame[8]
			self.group = frame[9]
			self.receptor = frame[10]
			self.label = frame[11:28 +1]
			self.flags = frame[29]
			self.brand = frame[30]
			self.cor = frame[31]
			self.carid = frame[32:38 +1]
