import libbit as convert
from datetime import datetime

def validade_header(frame):
    if ((frame[0] == 64 and frame[13] == 64) or (frame[0] == 83 and frame[1] == 84 and frame [2] == 88)):
        return True

def get_serial(frame):
    return convert.fmtByte_to_Str(frame, separador='')

def get_date(frame):
    hora =  convert.bcd2int(frame[0])
    minuto = convert.bcd2int(frame[1])
    segundo = convert.bcd2int(frame[2])
    dia = convert.bcd2int(frame[3])
    mes = convert.bcd2int(frame[4])
    ano = convert.bcd2int(frame[5])
    data = datetime(int(ano), int(mes), int(dia), int(hora), int(minuto), int(segundo))
    return (datetime.strftime(data, "%d/%m/%y %H:%M:%S"))
