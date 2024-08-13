#!/usr/bin/env python3
from netconf_client.connect import connect_ssh
from netconf_client.ncclient import Manager
import argparse
import logging
import socket
import os

class NetConfClient(object):
    def __init__(self, host, username, password):
        super(NetConfClient, self).__init__()
        self.host     = host
        self.username = username
        self.password = password

    def handler(message):
        logging.debug(F"[NCC] handler request <{message}>")
        if message == 'connect':
            self.connect()
        elif message == 'disconnect':
            self.disconnect()
        elif message == 'disconnect':
            self.disconnect()
        elif message == 'lock_db_candidate':
            self.lock_db(target='candidate')
        elif message == 'unlock_db_candidate':
            self.unlock_db(target='candidate')
        elif message == 'lock_db_running':
            self.lock_db(target='running')
        elif message == 'unlock_db_running':
            self.unlock_db(target='running')
        elif message == 'discard_changes':
            self.discard_changes()
        elif message == 'disconnect':
            self.disconnect()
    
    def connect(self):
        session = connect_ssh(host=self.host, port=830, username=self.username, password=self.password)
        self.mgr = Manager(session, timeout=120)    

    def disconnect(self):
        self.mgr.close_session()

    def lock_db(self, target='candidate'):
        self.mgr.lock(target)

    def unlock_db(self, target='candidate'):
        self.mgr.unlock(target)

    def discard_changes(self):
        self.mgr.discard_changes()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', type=int, default=0)
    parser.add_argument('--socket-path', default="/run/imish-ncc.sock")
    parser.add_argument('--host', default="0.0.0.0")
    parser.add_argument('--user', default="root")
    parser.add_argument('--password', default="TTTD@1234%")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    try:
        os.unlink(args.socket_path)
    except OSError:
        if os.path.exists(args.socket_path):
            raise

    try:
        ncc = NetConfClient(args.host, args.user, args.password)
        ncc.connect()
    except Exception as e:
        perror(e)

    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(args.socket_path)
    server.listen(1)

    logging.info('Server is listening for incoming connections...')
    while True:
        try:
            connection, client_address = server.accept()
            try:
                logging.info('[Connection from]:' + str(connection).split(", ")[0][-4:])

                # receive data from the client
                while True:
                    data = connection.recv(1024)
                    logging.info(F'[Received data]: {data.decode() if data is not None else data}')
                    if not data:
                        break

                    response = ncc.handler(data.decode())
                    connection.sendall(response.encode())
            except Exception as e:
                logging.error(e)
        finally:
            connection.close()
    
    os.unlink(args.socket_path)
