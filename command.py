import libbit

def acionamento(device):
	#MG3000 commando/tipo_disp/num_disp/saida/evt

	print("Comando Acionamento")
	controler = device.controler
	command = device.cod_acionamento
	disp =  device.devicetype()
	id_disp = device.sector() - 1
	saida = device.receptor()
	geraevt = 1
	payload = bytearray()
	payload +=  command
	payload.append(disp)
	payload.append(id_disp)
	payload.append(saida)
	if (controler == "MG3000"):
		payload.append(geraevt)
	cs = libbit.calcula_checksum(payload)
	payload.append(cs) 
	return(payload)


	