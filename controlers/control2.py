import libbit as convert
from datetime import datetime
import controlers.control2conf as conf
from controlers.frame_evt import FrameEvt
import bd


class CONTROL2():
    def __init__(self, frame, conn):
        
        commands = {
            116 : self.__pc_event,
            117 : self.__pc_acionamento,
        }

        self.frame    = frame
        self.conn = conn
        self.controler = "CONTROL2"
        self.command  = commands.get(frame[6])

    def run_commmand(self):
        if (self.command):
            comando = self.command
            comando()
        else:
            print("COMANDO NAO CATALOGADO", self.frame[6])

    def __build_frame(self, payload):
        cabecalho = b'STX'
        rodape = b'ETX'
        tamanho = int.to_bytes(len(payload) + 1, 2, 'big')
        checksum = convert.calcula_checksum(payload).to_bytes(1, 'big')
        frame = cabecalho + tamanho + payload + checksum + rodape
        return frame

    def __print_event(self, event):
        print("==== CONTROLADORA II ====")
        print("evento   :", conf.tab_evttype[event.evttype])
        print("serial   :", event.serial)
        print("data     :", event.date)
        print("device_id:", event.device)
        print("device   :", conf.tab_device[event.device])
        print("setor    :", event.sector)
        print("leitora  :", event.receptor)
        print("info     :", conf.tab_evtinfo[event.evttype][event.info])  
        print("mode     :", conf.tab_mode[event.mode])
        print("num disp :", event.id_device)

    def __pc_event(self):
        print("COMANDO EVENTO 116")
        frameevento = self.frame[9:24 + 1]
        self.__process_event(frameevento)

    ## RULES
    def __process_event(self, frameevento):
        event = FrameEvt(frameevento, self.controler)
        if (event.evttype == 0): 
            if (event.serial in bd.AUTORIZADOS):
                resposta = self.conn.send(self.acionamento(event))
                print("RESPOSTA ->",resposta)
            else:
                print("ENTRADA NAO AUTORIZADO")
        self.__print_event(event)


    def __pc_acionamento(self):
        print("COMANDO ACIONAMENTO 117")

    def acionamento(self, event):
        # 00+75+<dispositivo>+<endereçoPlaca>+<saida>+cs 
        dispositivo =  0
        endPlaca = event.id_device - 1
        saida = event.receptor
        payload = bytearray()
        payload += b'\x00\x75'
        payload.append(dispositivo)
        payload.append(endPlaca)
        payload.append(saida) 
        return self.__build_frame(payload)


