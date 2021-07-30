import socket, selectors
import time
import libserver, libevents
import controlers

def process_event(frame):
    print("PROCESS EVENT")
    controler = controlers.get_controler(frame)
    ## vaidade event ##
    if (controler.command == 4):
        print(controler.evttype( ))

    # return_event = validate_event(controler)
        # executa comando (event)
    # send_event   
    controler.whoiam()
    # tipo de evento #controler.event_type()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    frame = conn.recv(1024)  # Should be ready
    if frame and libevents.validade_header(frame):
        print('echoing', repr(frame), 'to', conn)
        return_event = process_event(frame)
        #conn.send(return_event)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

def process_request(address):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(3) 
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select(timeout=15)
        time.sleep(1)
        for key, mask in events:
            callback = key.data
            print("FUNCAO ",callback)
            callback(key.fileobj, mask)
                

if __name__ == '__main__':
    address = libserver.parse_command_line("star server")
    sel = selectors.DefaultSelector()
    process_request(address)