import libbit as convert
from datetime import datetime


class MG3000():
    def __init__(self, frame):

        commands = {
            4 : "event",
        }

        self.tab_evttype = [
            "Dispositivo Acionado",
            "Passagem",
            "Equipamento Ligado",
            "Desperta Porteiro",
            "Mudança de Programação",
            "Acionamento pela Botoeira",
            "Acionamento pelo PC",
        ]

        self.frame    = frame
        self.token    = self.__gettoken__(frame)
        self.command  = commands.get(frame[6])
        self.evtsize  = frame[4]
        self.keeplive = True if self.token else False
        self.serial   = convert.fmtByte_to_Str(frame[9:11 + 1], separador='')
        self.receptor = self.iddevice()


    def __gettoken__(self, frame):
        if (frame[0] == 64 and frame[13] == 64):
            return str(frame).split("@") 

    def evttype(self):
        b1 = self.frame[8]
        self.b1_high = (b1 & 0xF1) >> 4
        return self.tab_evttype[self.b1_high]

    def evtdate(self):
        hora =  convert.bcd2int(self.frame[12])
        minuto = convert.bcd2int(self.frame[13])
        segundo = convert.bcd2int(self.frame[14])
        dia = convert.bcd2int(self.frame[15])
        mes = convert.bcd2int(self.frame[16])
        ano = convert.bcd2int(self.frame[17])
        data = datetime(int(ano), int(mes), int(dia), int(hora), int(minuto), int(segundo))
        return (datetime.strftime(data, "%d/%m/%y %H:%M:%S"))

    def device(self):
        b11 = self.frame[18]
        nibbleH = (b11 >> 4)
        if nibbleH == 1:
            return "RF"
        elif nibbleH == 3:
            return "CARTAO"
        else:
            return "NAO IMPLEMENTADO"

    def sector(self):
        b11 = self.frame[18] 
        nibleL = (b11 & 0x0F)
        return nibleL + 1

    def battery(self):
        b22 = self.frame[22]
        battery = convert.onebit(b22, 7)
        if battery == 0:
            return 'bateria OK'
        else:
            return 'bateria fraca'

    def iddevice(self):
        b22 = self.frame[22]
        value = convert.bits2int(b22, 5, 4)  # bit2:1
        return value + 1

    def evtread(self):
        b22 = self.frame[22]
        if convert.onebit(b22, 6) == 0:
            return 'Evento não lido'
        else:
            return 'evento já lido '

    def evtinfo(self):
        evttype = self.b1_high
        b16 = self.frame[23]

        nibleL = (b16 & 0x0F)
        # ver documentacao sensores
        # bit0 = receptor 1
        # bit1 = receptor 2
        # bit2 = receptor 3
        # bit3 = receptor 4
        i = self.receptor - 1
        value = convert.onebit(b16, i)
        print("bit  ==valor =>>>> :  ",value)
        evttype = self.b1_high
        if (evttype == 0):
            if (b16 == 170):
                info = "Fora de Horario"
            else:
                if (value == 0):
                    info = "Sensor Aberto"
                else:
                    info = "Sensor Fechado" 
        return info

