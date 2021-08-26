import controlers

def process_event(frame):
    print("PROCESS EVENT")
    controler = controlers.discover(frame)
    if (controler.keeplive):
        print("Keep Alive")
    elif (controler.command == "event"):
        print("evento   :", controler.evttype())
        print("serial   :", controler.serial)
        print("data     :", controler.evtdate())
        print("device   :", controler.device())
        print("setor    :", controler.sector())
        print("leitora  :", controler.iddevice())
        print("Evento   :", controler.evtread())
        print("Bateria  :", controler.battery())
        print("info     :", controler.evtinfo())

    else:
        print("COMANDO ",controler.command)
    # return_event = validate_event(controler)
        # executa comando (event)
    # send_event   
    controler.whoiam()
    # tipo de evento #controler.event_type()

