import controlers

def process_event(frame):
    print("PROCESS EVENT")
    controler = controlers.discover(frame)
    if (controler.keeplive):
        print("Keep Alive")
    elif (controler.command == "event"):
        print(controler.evttype( ))
    else:
        print("COMANDO ",controler.command)
    # return_event = validate_event(controler)
        # executa comando (event)
    # send_event   
    controler.whoiam()
    # tipo de evento #controler.event_type()

