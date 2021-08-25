

class MG3000():
    def __init__(self, frame):

        commands = {
            4 : "event",
        }

        self.tab_evttype = [
            "Dispositivo Acionado",
            "Passagem",
            "Equipamento Ligado",
            "Desperta Porteiro"
        ]

        self.frame = frame
        self.token = self.__gettoken__(frame)
        self.command = commands.get(frame[6])
        self.evtsize = frame[4]
        self.keeplive = True if self.token else False

    def __gettoken__(self, frame):
        if (frame[0] == 64 and frame[13] == 64):
            return str(frame).split("@") 

    def evttype(self):
        byte1 = self.frame[8]
        print("tipoEvento ==byte =>>>> :  ", byte1)
        byte1_high = (byte1 & 0xF1) >> 4
        print("tipoEvento ==valor =>>>> :  ", byte1_high)
        return self.tab_evttype[byte1_high]


    def whoiam(self):
        print("whoiam EU SOU O MG3000")

    