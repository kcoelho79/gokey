import socket, selectors
import time
import libserver, libevents
from event import process_event
import libbit as convert
import controlers

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    frame = conn.recv(1024)  # Should be ready
    if frame and libevents.validade_header(frame):
        print('echoing', repr(frame), 'to', conn)
        print(convert.fmtByte_to_Str(frame,"/"))
        controler = controlers.discover(frame, conn)
        controler.run_commmand()
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