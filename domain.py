
class Message():
	def __init__(self, frame):
		self.msgsize = frame[4]
		self.command = frame[6]

		if self.command <= 121:
			self.controler = "guaritaIP"
		else:
			self.controler = "ControladoraII"
	
	def is_evento(comando):
		if (comando == 4 or comando == 116):
			return True


def has_header(frame):
	if (frame[0] == 83 and frame[1] == 84 and frame [2] == 88):
		return True

def eval_input(frame):
	if has_header(frame):
		message = Message
		if message.is_evento:
			print("COMANDO EVENTO")
			#run_evento
		else:
			#run_comando
			pass
	else:
		print("Cabecalho Desconhecio")

