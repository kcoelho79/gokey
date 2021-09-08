import libbit as convert
from datetime import datetime
import libevents
from controlers.frame_evt import FrameEvt
import bd

class MG3000():
    def __init__(self, frame, conn):

        self.frame = frame
        self.conn = conn
        self.controler = "MG3000"
        commands = {
            4 : self.__pc_event4,
            33: self.__pc_event33,
            46: self.__pc_evento_nao_cadastrado,
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

        self.tab_device = [
			0,
			"RF",
			2,
			"CARTAO"
		]
        self.token    = self.__gettoken__(frame)
        self.command  = commands.get(frame[6])
        self.keeplive = True if self.token else False

    def run_commmand(self):
        if (self.keeplive == False):
            if (self.command):
                comando = self.command
                comando()
            else:
                print("COMANDO  NAO CATALOGADO", frame[6])
        else:
            print("KeepLive")

    def __gettoken__(self, frame):
        if (frame[0] == 64 and frame[13] == 64):
            return str(frame).split("@")    

    def __print_event(self, event):
        print("evento   :", self.tab_evttype[event.evttype])
        print("serial   :", event.serial)
        print("data     :", event.date)
        print("device   :", self.tab_device[event.device])
        print("setor    :", event.sector)
        print("leitora  :", event.receptor)
        print("info     :", event.info)  
    
    # PC COMANDOS EVENTOS

    def __pc_evento_nao_cadastrado(self):
        print("Evento NAO CADASTRADO FUNCAO")

    def __pc_event4(self):
        print("COMANDO EVENTO 4")
        frameevento =  self.frame[8: 23 + 1]
        self.__process_event(frameevento)
    
    def __pc_event33(self):
        print("COMANDO EVENTO 33")
        frameevento =  self.frame[7: 22 + 1]
        self.__process_event(frameevento)
    
    def __process_event(self, frameevento):
        event = FrameEvt(frameevento, self.controler)
        if (event.evttype == 0): 
            if (event.serial in bd.AUTORIZADOS):
                resposta = self.conn.send(self.acionamento(event))
                print("RESPOSTA ->",resposta)
            else:
                print("ENTRADA NAO AUTORIZADO")
        self.__print_event(event)

    
    # PC COMANDOS EXECUTANDO

    def acionamento(self, event):
        #commando/tipo_disp/num_disp/saida/evt
        print("Comando Acionamento")
        disp =  event.device
        num_disp = event.sector - 1
        saida = event.receptor
        geraevt = 1
        payload = bytearray()
        payload += b'\x00\x0d'
        payload.append(disp)
        payload.append(num_disp)
        payload.append(saida)
        payload.append(geraevt)
        cs = convert.calcula_checksum(payload)
        payload.append(cs) 
        return(payload)