"""
class Message()
	sera uma superclasse que pega 
	rodape_valida
	tamanho
	comando
	device
	mensagem

"""
def has_header(frame):
	print(frame[0:3])
	if (frame[0] == 83 and frame[1] == 84 and frame [2] == 88):
		return True

def is_evento(comando):
	if (comando == 4 or comando == 116):
		return True

def eval_input(frame):
	if has_header(frame):
		if (is_evento(frame[6])):
			print("COMANDO EVENTO")
			#run_evento
			#evento = Evento(message]
		else:
			#get_commando
				#run_comando
			pass
	else:
		print("COMANDO DESCONHEcIDO")

