

class MG3000():
    def __init__(self, frame):

        self.tab_evttype = [
            "Dispositivo Acionado",
            "Passagem",
            "Equipamento Ligado",
            "Desperta Porteiro"
        ]
        self.frame = frame
        self.command = frame[6]
        self.evtsize = frame[4]

    def evttype(self):
        byte1 = self.frame[8]
        print("tipoEvento ==byte =>>>> :  ", byte1)
        byte1_high = (byte1 & 0xF1) >> 4
        print("tipoEvento ==valor =>>>> :  ", byte1_high)
        return self.tab_evttype[byte1_high]


    def whoiam(self):
        print("whoiam EU SOU O MG3000")

    