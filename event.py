import controlers
import bd
import command
import libbit
import time

def process_event(frame, conn, sel):
    print("PROCESS EVENT")
    device = controlers.discover(frame)
    if (device.keeplive):
        print("Keep Alive")
    elif (device.command == "event"):
        print("evento   :", device.evttype())
        print("serial   :", device.serial)
        print("data     :", device.evtdate())
        print("device   :", device.devicetype())
        print("setor    :", device.sector())
        print("device int:", device.device_type)
        print("leitora  :", device.receptor())
        print("Evento   :", device.evtread())
        print("Bateria  :", device.battery())
        print("info     :", device.evtinfo())
        if (device.controler == "CONTROL2"):
            print("Endereco :", device.deviceid() )

        if (device.evttype() == "Dispositivo Acionado"):
            if (device.serial in bd.AUTORIZADOS):
                print("ACIONAMENTO AUTORIZADO")
                COMANDO = device.acionamento()
                print(COMANDO)
                print(libbit.fmtByte_to_Str(COMANDO,' '))
                conn.send(COMANDO)
                # print("FECHADNO", conn)
                # print("================")
                # sel.unregister(conn)
                # conn.close()
                # time.sleep(5)
                # print("xxxxxxxxxxxxxxxxx")
                # print("COMANDADNDO A PORRA TODA DE NOVO")
                # conn.send(COMANDO)

            else:
                print("ACIONAMENTO NAO AUTORIZADO")

    else:
        if (device.command):
            print("COMANDO ",device.command)
        else:
            print("COMANDO  NAO CATALOGADO", frame[6])

