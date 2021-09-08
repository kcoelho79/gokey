import libbit as convert
from datetime import datetime

class CONTROL2():
    def __init__(self, frame):
        commands = {
            116 : "event",
            117  : "acionamento",
        }

        tab_device = [
            0,
            "RF",
            2,
            "CARTAO"
        ]

        self.controler = "CONTROL2"
        self.cod_acionamento = b'\x00\x75'
        self.frame    = frame
        self.keeplive = False
        self.command  = commands.get(frame[6])
       # self.evtsize  = frame[4]
        self.serial   = convert.fmtByte_to_Str(frame[12:16 + 1], separador='')
        self.device_type = tab_device[self.devicetype()]

        self.tab_evttype = [
            'Dispositivo Acionado',
            'Passagem',
            'Equipamento Ligado',
            'Desperta Porteiro',
            '4',
            'Acionamento Guarita',
            'Acionamento PC',
            'Receptores nao atualizados',
            'tentativa clonagem',
            'Panico',
            'a',
            'b',
            'c',
            'd',
            'e',
            'Não cadastrado'
        ]

        self.tab_evtinfo = [
        [
            'SUB_LOG_ACIONAMENTO_ENTRADA',
            'SUB_LOG_ACIONAMENTO_SAIDA',
            'SUB_LOG_ACIONAMENTO_BOTAO_1',
            'SUB_LOG_ACIONAMENTO_BOTAO_2',
            'SUB_LOG_ACIONAMENTO_BOTAO_3',
            'SUB_LOG_ACIONAMENTO_BOTAO_4',
            'SUB_LOG_AGUARDANDO_SEGUNDA_VALIDACAO'],
        [
            'SUB_LOG_PASSAGEM_ENTRADA_1',
            'SUB_LOG_PASSAGEM_SAIDA_1',
            'SUB_LOG_PASSAGEM_ENTRADA_2',
            'SUB_LOG_PASSAGEM_SAIDA_2',
            'SUB_LOG_PASSAGEM_ENTRADA_3',
            'SUB_LOG_PASSAGEM_SAIDA_3',
            'SUB_LOG_PASSAGEM_ENTRADA_4',
            'SUB_LOG_PASSAGEM_SAIDA_4',
            'SUB_LOG_PASSAGEM_TOUT',
            'SUB_LOG_PASSAGEM_SAIDA_LIVRE',
            'SUB_LOG_PASSAGEM_BOTAO_1',
            'SUB_LOG_PASSAGEM_BOTAO_2',
            'SUB_LOG_PASSAGEM_BOTAO_3',
            'SUB_LOG_PASSAGEM_BOTAO_4',
            'SUB_LOG_PASSAGEM_ENTRADA_APB_DESLIGADO',
            'SUB_LOG_PASSAGEM_SAIDA_APB_DESLIGADO'
        ],

        ['2 SEM USO'],

        ['SUB_LOG_HABILITACAO_SEM_VAGAS'],

        ['4 SEM USO'],

        [
            'SUB_LOG_ACIONAMENTO_REMOTO_OK',
            'SUB_LOG_ACIONAMENTO_REMOTO_ERRO',
            'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_OK',
            'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_ERRO',
            'SUB_LOG_ACIONAMENTO_REMOTO_RELE_5',
            'SUB_LOG_ACIONAMENTO_REMOTO_RELE_6'
        ],

        [
            'SUB_LOG_ACIONAMENTO_REMOTO_OK',
            'SUB_LOG_ACIONAMENTO_REMOTO_ERRO',
            'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_OK',
            'SUB_LOG_ACIONAMENTO_REMOTO_COM_ID_ERRO',
        ],

        ['SUB_LOG_INCONSISTENCIA_ENTRE_BASES_DE_DADOS'],

        ['8 SEM USO'],

        [
            'SUB_LOG_PANICO',
            'SUB_LOG_PANICO_NAO_ATENDIDO',
            'SUB_LOG_PANICO_CANCELADO',
            'SUB_LOG_PANICO_2X_CARTAO',
            'SUB_LOG_PANICO_IMEDIATO',
            'SUB_LOG_PANICO_TEMPORIZADO',
            'SUB_LOG_PANICO_DISPOSITIVO'
        ],

        ['10 SEM USO'],

        ['11 SEM USO'],

        [
            'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_1',
            'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_2',
            'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_3',
            'SUB_LOG_ERRO_GRAVAÇÃO_BIOMETRIA_4',
            'SUB_LOG_ATUALIZAÇÃO_CANCELADA_ERROS'
        ],

        [
            '0',
            '1',
            '2',
            'SUB_LOG_BACKUP_AUTO_SETUP_OK'
        ],

        ['14 SEM USO'],

        [
            '',
            'SUB_LOG_NAO_CADASTRADO',
            'SUB_LOG_LEITORA_EXPEDIDORA'],

        [
            'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_1',
            'SUB_LOG_DUPLA_PASSAGEM_SAIDA_1',
            'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_2',
            'SUB_LOG_DUPLA_PASSAGEM_SAIDA_2',
            'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_3',
            'SUB_LOG_DUPLA_PASSAGEM_SAIDA_3',
            'SUB_LOG_DUPLA_PASSAGEM_ENTRADA_4',
            'SUB_LOG_DUPLA_PASSAGEM_SAIDA_4'],

        [
            '0=VALIDO',
            '1=INVALIDO_NAO_CADASTRADO',
            '2=INVALIDO_LEITORA_COFRE',
            '3=INVALIDO_ANTI_PASSBACK',
            '4=INVALIDO_SEM_CREDITOS',
            '5=INVALIDO_DATA_VALIDADE_EXPIRADA',
            '6=INVALIDO_TEMPO_ANTICARONA',
            '7=INVALIDO_LEITORA_NAO_HABILITADA',
            '8=INVALIDO_FERIADO',
            '9=INVALIDO_JORNADA_TURNO',
            '10=INVALIDO_SEM_VAGAS_NIVEL',
            '11=INVALIDO_LEITORA_INIBIDA'
        ],

        ['18 SEM USO'],

        [
            'SUB_LOG_ALARME_ED_1',
            'SUB_LOG_ALARME_ED_2',
            'SUB_LOG_ALARME_ED_3',
            'SUB_LOG_ALARME_ED_4',
            'SUB_LOG_ARROMBAMENTO1',
            'SUB_LOG_ARROMBAMENTO2',
            'SUB_LOG_ARROMBAMENTO3',
            'SUB_LOG_ARROMBAMENTO4'],

        ['20 SEM USO'],

        [
            'SUB_LOG_ATUALIZACAO_FALHA_DE_GRAVACAO',
            'SUB_LOG_ATUALIZACAO_CONCLUIDA_COM_SUCESSO',
            'SUB_LOG_ATUALIZACAO_SERIAL_FORA_DO_LIMITE'

        ]
    ]


    def evttype(self):
        b1 = self.frame[9]
        self.b1_high = (b1 & 0x1f)
        return self.tab_evttype[self.b1_high]

    def sector(self): #porta can
        b1 = self.frame[9] 
        sector = convert.bits2int(b1, 7, 5)
        return sector + 1

    def operation_mode(self):
        b2 = self.frame[10]
        mode = convert.bits2int(b2, 6, 7)
        if (mode == 0):
            return "CATRACA"
        elif (mode == 1):
            return "PORTA"
        elif (mode == 2):
            return "CANCELA"

    def deviceid(self): #only controloladora II
        b2 = self.frame[10]
        id = convert.bits2int(b2, 5, 0)
        return id + 1

    def devicetype(self):
        b3 = self.frame[11]
        nibbleL = (b3 & 0x0F)
        if (nibbleL < 4):
            return nibbleL
        else:
            return 0

    def evtdate(self):
        hora =  convert.bcd2int(self.frame[17])
        minuto = convert.bcd2int(self.frame[18])
        segundo = convert.bcd2int(self.frame[19])
        dia = convert.bcd2int(self.frame[20])
        mes = convert.bcd2int(self.frame[21])
        ano = convert.bcd2int(self.frame[22])
        data = datetime(int(ano), int(mes), int(dia), int(hora), int(minuto), int(segundo))
        return (datetime.strftime(data, "%d/%m/%y %H:%M:%S"))

    def battery(self):
        b16 = self.frame[24]
        battery = convert.onebit(b16, 7)
        if battery == 0:
            return 'bateria OK'
        else:
            return 'bateria fraca'

    def receptor(self): 
        b16 = self.frame[24]
        value = convert.bits2int(b16, 5, 4) #bit 1,2 
        return value + 1

    def evtread(self):
        b16 = self.frame[24]
        if convert.onebit(b16, 6) == 0:
            return 'Evento não lido'
        else:
            return 'evento já lido '

    def evtinfo(self):
        b16 = self.frame[24]
        print("infoEvento ==byte =>>>> :  ",b16)
        valor_tipo = self.b1_high
        valor_info = convert.bits2int(b16, 7, 4)
        print("tipoEvento ==valor =>>>> :  ",valor_tipo)
        print("infoEvento ==valor =>>>> :  ",valor_info)
        info = self.tab_evtinfo[valor_tipo][valor_info]
        print('=>Info Evento  === info: ',info)
        return info

    def __build_frame(self, payload):
        cabecalho = b'STX'
        rodape = b'ETX'
        tamanho = int.to_bytes(len(payload) + 1, 2, 'big')
        checksum = convert.calcula_checksum(payload).to_bytes(1, 'big')
        frame = cabecalho + tamanho + payload + checksum + rodape
        return frame

    def acionamento(self):
        # 00+75+<dispositivo>+<endereçoPlaca>+<saida>+cs 
        dispositivo =  0
        endPlaca = self.deviceid() - 1
        saida = self.receptor()
        payload = bytearray()
        payload += b'\x00\x75'
        payload.append(dispositivo)
        payload.append(endPlaca)
        payload.append(saida) 
        return self.__build_frame(payload)


