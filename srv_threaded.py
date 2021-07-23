# workd many thread to receive several connection

import conn_utils as utils
from threading import Thread

def start_threads(listener, worker=4):
    t = (listener,)
    for i in range(worker):
        Thread(target=utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = utils.parse_command_line('multi-threaded server')
    listener = utils.create_srv_socket(address)
    start_threads(listener)