import libbit as convert
from datetime import datetime

def validade_header(frame):
    if ((frame[0] == 64 and frame[13] == 64) or (frame[0] == 83 and frame[1] == 84 and frame [2] == 88)):
        return True

def get_serial(frame):
    return convert.fmtByte_to_Str(frame, separador='')

def wiegand_to_hex(serial):
    s1, s2 = serial.split('-')          # separa o prefixo 2 algarismo e o  sufixo 4 algarismo do serial
    s1 = int(s1).to_bytes(1, 'big')     #converte inteiro para byte
    s2 = int(s2).to_bytes(2, 'big')
    return s1 + s2

def label_to_bcd(label, max_char):
    label = str.encode(label) # converte str para bytes
    for i in range(max_char - len(label)):
        label += b'\x00'
    print("LABEL", label)
    return label

def get_date(frame, bcd=True):
    if (bcd):
        hora =  convert.bcd2int(frame[0])
        minuto = convert.bcd2int(frame[1])
        segundo = convert.bcd2int(frame[2])
        dia = convert.bcd2int(frame[3])
        mes = convert.bcd2int(frame[4])
        ano = convert.bcd2int(frame[5])
    else:
        hora =  frame[0]
        minuto = frame[1]
        segundo = frame[2]
        dia = frame[3]
        mes = frame[4]
        ano = frame[5]
    data = datetime(int(ano), int(mes), int(dia), int(hora), int(minuto), int(segundo))
    return (datetime.strftime(data, "%d/%m/%y %H:%M:%S"))
