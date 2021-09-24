import libbit as convert
from datetime import datetime
import libevents
import librule
from controlers.frame_evt import FrameEvt
import controlers.mg3000conf as conf
import bd
from api.models import Events

class MG3000():
    def __init__(self, frame, conn):

        commands = {
            4 : self.__pc_event4,
            33: self.__pc_event33,
            46: self.__pc_evento_nao_cadastrado,
        }
        self.frame = frame
        self.conn = conn
        self.controler = "MG3000"
        self.token    = self.__gettoken__(frame)
        self.command  = commands.get(frame[6])

    def __iskeeplive(self):
        return print("==> KeepLive <==") if self.token else False

    def run_commmand(self):
        if (self.__iskeeplive() == False):
            if (self.command):
                comando = self.command
                comando()
            else:
                print("COMANDO NAO CATALOGADO", frame[6])

    def __gettoken__(self, frame):
        if (frame[0] == 64 and frame[13] == 64):
            return str(frame).split("@")    

    def __print_event(self, event):
        print("====  MG3000   ====")
        print("evento   :", conf.tab_evttype[event.evttype])
        print("serial   :", event.serial)
        print("data     :", event.date)
        print("device   :", conf.tab_device[event.device])
        print("setor    :", event.sector)
        print("leitora  :", event.receptor)
        print("info     :", event.info)
        print("Acesso   :", event.access)
        print("Resposta :", event.resposta)
        self.__save_db(event)


    def __save_db(self, event):
        Events(
            frame=self.frame,
            controler = self.controler,
            data = event.date,
            serial = event.serial,
            access = event.access,
            receptor = event.receptor,
            resident = "NULO",
        ).save()
    
# PC COMANDOS EVENTOS

    def __pc_evento_nao_cadastrado(self):
        print("Evento NAO CADASTRADO FUNCAO")
        print("CONSULTANDO banco de dados")
        serial = '0000' + convert.fmtByte_to_Str(self.frame[10:12+1])
        if (librule.isresident(serial)):
            print("SERIAL CADASTRADO AUTORIZADO")
        else:
            print("SERIAL NAO AUTORIZADO")

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
           # if (librule.isresident(event.serial)):
            if (event.serial in bd.AUTORIZADOS):
                event.resposta = self.conn.send(self.acionamento(event))
                print("RESPOSTA ->", event.resposta)
                event.access = 'Autorizado'
            else:
                print("ENTRADA NAO AUTORIZADO")
                event.access = 'Nao Autorizado'
        self.__print_event(event)

# PC COMANDOS EXECUTANDO

    def acionamento(self, event):
        #commando/tipo_disp/num_disp/saida/evt
        print("Comando Acionamento")
        disp =  event.device
        num_disp = event.sector - 1
        saida = event.receptor
        geraevt = 0
        payload = bytearray()
        payload += b'\x00\x0d'
        payload.append(disp)
        payload.append(num_disp)
        payload.append(saida)
        payload.append(geraevt)
        cs = convert.calcula_checksum(payload)
        payload.append(cs) 
        return(payload)

    def crud_device(self, op, serial, receptor):
        #comando 67 0x00+0x43
        #comando/opcao/frame_dev/cs
        #opcao,serial,label,receptor
        op = 0 # cadastro
        receptor = 2 # can2
        print("Comando Acionamento")
        payload = bytearray()
        payload += b'\x00\x43'
        payload.append(op) # operacao CRUD 0=Cad
        payload.append(60) # x30 = device(bHigh)=3 e disp_dev(bLow)=0 
        payload.extend(libevents.wiegand_to_hex(serial))
        payload += b'\x00\x00' # byte 5+6 contadorHL
        payload += b'\x00\x00' # byte 7+8 UnidadeHL
        payload += b'\x00'     # byte 9 bloco
        payload += b'\x01'     # grupo 1 Horario
        payload.append(receptor)
        payload.extend(libevents.label_to_bcd(label, max_char=18))
        payload += b'\x40'     #flags'
        payload += b'\x00\x00\x20\x20\x20\x20\x20\x20\x20'

