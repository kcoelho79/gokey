import selectors
import socket
import time
import domain
import libserver


sel = selectors.DefaultSelector()

def acionamento(conn, evento):
    if (evento == b'@5410EC5B7909@kafe@0001\x00'):
        print("1 conexao - keep live")
    else:
        print("ACIONAMENTO: EVENTO")
        print("EVENTO :",evento)
        time.sleep(3)
        comando = bytearray(b'\x00\r\x03\x01\x01\x00\x12')
        resposta = conn.send(comando)  # Hope it won't block
        print("RESPOSTA", resposta)
    sel.unregister(conn)
    conn.close()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)
    

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        print("DATA", data)
        d = domain.eval_input(data)
        print("d",d)
        conn.send(d)
       # sel.modify(conn, selectors.EVENT_WRITE, data)
       #conn.send(comando)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

def process_events(address):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(3) 
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)

    while True:
        events = sel.select(timeout=15)
        time.sleep(2)
        for key, mask in events:
            print("FUNCAO ",callback)
            callback = key.data
            callback(key.fileobj, mask)
                

if __name__ == '__main__':
    address = libserver.parse_command_line("star server")
    process_events(address)