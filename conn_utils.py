#!/usr/bin/env python3

import argparse, socket, sys
import BitHandler as convert
import domain


def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock

def create_cli_connection(address):
    """ create socket and connect server at address """
    sock = create_socket()
    sock.connect(address)
    print("===================================+===========")
    print(">> create_cli_connection >> ")
    print('>> create_cli_connection >> connected at {}'.format(sock.getpeername()))
    print("===================================+===========")

    return sock

def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = create_socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print("===================================+===========")
    print(">> create_srv_socket >> ")
    print('>> Listening at {}'.format(address))
    print("===================================+===========")

    return listener

def accept_connections_forever(listener):
    """Forever answer incoming connections on a listening socket."""
    while True:
        sock, address = listener.accept()
        print("===================================+===========")
        print(">> accept_connection_forever >> ")
        print('>> connection from {}'.format(address))      
        print("===================================+===========")
        handle_conversation(sock, address)

def handle_conversation(sock, address):
    """Converse with a client over `sock` until they are done talking."""
    try:
        while True:
            handle_request(sock, address)
    except EOFError:
        print("===================================+===========")
        print(">> handle_conversation >> ")
        print('>> Client socket to {} has closed'.format(address))
        print("===================================+===========")

    except Exception as e:
        print('>> handle_conversation >> Client {} error: {}'.format(address, e))
    finally:
        sock.close()

def handle_request(sock, address):
    """Receive a single client request on `sock` and send the answer."""
    frame = recv_until(sock)
    print("===================================+===========")
    print(">> handle_request >>")
    print(">> frame received: {}:".format(address))
    print(">> original : ", frame)
    print(">> conv-str :",convert.fmtByte_to_Str(frame,separador='/'))
    print("===================================+===========")

    return_event = domain.eval_input(frame)
   # print("Resposta do servidor", resposta)
   # sock.sendall(return_event)

def recv_until(sock):
    """Receive bytes over socket `sock` until we receive the `suffix`."""
    frame = sock.recv(4096)
    if not frame:
        raise EOFError('socket closed')
    return frame

def close_connection(sock):
    print("finish connection from {}".format(address))
