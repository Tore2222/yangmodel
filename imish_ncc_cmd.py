#!/usr/bin/env python3
import argparse
import logging
import socket
import os

def perror(message, exit_code=-1):
    logging.error(message)
    exit(exit_code)

class ImishNetconfClient_Connection(object):
  def __init__(self, pid, socket_path):
    super(ImishNetconfClient_Connection, self).__init__()
    self.pid = pid
    self.socket_path = socket_path

  def connect(self):
    try:
      self.client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
      self.client.connect(self.socket_path)
      return True
    except Exception as e:
      logging.debug(F"connected to NCC: {e}")
      return False

  def disconnect(self):
    self.client.close()
    logging.debug("disconnected to NCC")

  def send(self, message):
    res = self.client.sendall(message.encode())
    response = self.client.recv(1024)
    logging.info(F"SEND message:{message} return response:{response}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-level', type=int, default=0)
    parser.add_argument('--pid-path', default="/run/imish-ncc.pid")
    parser.add_argument('--socket-path', default="/run/imish-ncc.sock")

    parser.add_argument('--start', action='store_true')
    parser.add_argument('--stop', action='store_true')
    parser.add_argument('--synchronize-running-db-with-zebos', action='store_true')
    parser.add_argument('--check-candidate-db-change', action='store_true')
    parser.add_argument('--discard-candidate-db-change', action='store_true')
    parser.set_defaults(start=False)
    parser.set_defaults(stop=False)
    parser.set_defaults(synchronize_running_db_with_zebos=False)
    parser.set_defaults(check_candidate_db_change=False)
    parser.set_defaults(discard_candidate_db_change=False)
    parser.add_argument('-l', '--lock-db', default=None, choices=['running', 'candidate'])
    parser.add_argument('-u', '--unlock-db', default=None, choices=['running', 'candidate'])
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    try:
      with open(args.pid_path, 'r') as fp:
        pid = int(fp.read().strip())

      logging.info(F"NCC: is running with pid {pid} ({args.pid_path})")
    except FileNotFoundError as e:
      pid = 0
      logging.info(F"NCC: is not running")
    except Exception as e:
      perror(F"NCC-CMD: error reading NCC pid-file {e}")

    if (args.start and pid > 0):
      perror("Invalid options: imish-ncc already started !")
    elif (args.synchronize_running_db_with_zebos and \
         (args.check_candidate_db_change or args.discard_candidate_db_change)):
      perror("Invalid options: imish-ncc already started !")


    if args.start:
      os.system("imish-ncc &")

    conn = ImishNetconfClient_Connection(pid, args.socket_path)
    conn_success = conn.connect()
    if conn_success:
      if args.lock_db:
        conn.send("lock_db")

      if args.synchronize_running_db_with_zebos:
        conn.send("synchronize")

      if args.unlock_db:
        conn.send("unlock_db")

      if args.stop:
        conn.send("stop")

      conn.disconnect()

    logging.info("NCC: quit!")
