import requests
import json
import socket
import libbit as convert
import libevents

def teste_ler_dispositivo():
	payload = bytearray()
	payload += b'\x00\x46'
	resposta = enviarframe(payload)
	print("ReSPOSTA HEX: ",resposta)
	print("ReSPOSTA BCD: ",convert.fmtByte_to_Str(resposta,'/'))


#libera passagem
def teste_cadastrar_cartao():
	label= 'testiculo01'
	serial =  '070-35060'
	op = 4 # cadastro
	receptor = 2 # can2
	print("Comando Cadastar ")
	payload = bytearray()
	payload += b'\x00\x43'
	payload.append(op) # operacao CRUD 0=Cad
	payload += b'\x30' # x30 = device(bHigh)=3 e disp_dev(bLow)=0 
	payload.extend(libevents.wiegand_to_hex(serial))
	payload += b'\x00\x00' # byte 5+6 contadorHL
	payload += b'\x00\x00' # byte 7+8 UnidadeHL
	payload += b'\x00'     # byte 9 bloco
	payload += b'\x01'     # grupo 1 Horario
	payload.append(receptor)
	payload.extend(libevents.label_to_bcd(label, max_char=18))
	payload += b'\x10'     #flags'
	payload += b'\x00\x00\x20\x20\x20\x20\x20\x20\x20'
	print("RESP0STA: ",convert.fmtByte_to_Str(enviarframe(payload)," "))

# nao liberado
#data = b'STX\x00\x15\x00t\x00(\x11\x00\x03\x00\x00F\x89\n\x15\x11\x0f\x04\x01\x00\x00R\x15ETX'


TCP_IP = '10.238.0.41'
TCP_PORT = 9000


def build_frame_to_send(payload):
    cabecalho = b'STX'
    rodape = b'ETX'
    tamanho = int.to_bytes(len(payload) + 1, 2, 'big')
    checksum = convert.calcula_checksum(payload).to_bytes(1, 'big')
    frame =  cabecalho + tamanho + payload + checksum 
    return frame

def build_frame_to_send_sem_cabecalho(payload):
    checksum = convert.calcula_checksum(payload).to_bytes(1, 'big')
    frame =  payload + checksum 
    return frame

def enviarframe(payload):
	frame = build_frame_to_send_sem_cabecalho(payload)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	print("ENVIANDO HEX  :", frame)
	print(convert.fmtByte_to_Str(frame,' '))
	s.sendall(frame)
	resposta = s.recv(4096)
	s.close()
	return resposta


teste_cadastrar_cartao()
#teste_ler_dispositivo()