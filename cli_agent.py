#!/usr/bin/env python3

import argparse
import logging
import pexpect
from time import sleep

class CLIAgent(object):
    def __init__(self, program, command_delay=0):
        super(CLIAgent, self).__init__()
        self.program = program
        self.command_delay = command_delay
        self._proc = pexpect.spawn(program, encoding='utf-8')

    def clean_recv_buffer(self, buff):
        # remove first and last lines
        lines = buff.split('\n')
        buff = '\n'.join(lines[1:len(lines)-1])
        return buff

    def receive(self, timeout=0.1):
        if self.command_delay:
            sleep(self.command_delay)

        output = ""
        for i in range(5):
            try:
                b = self._proc.read_nonblocking(size=100000, timeout=timeout)
                if b and len(b) > 0:
                    output += b
            except pexpect.exceptions.TIMEOUT as e:
                logging.debug(F"RECV-NONBLOCK: TIMEOUT {i} times")
        return self.clean_recv_buffer(output)

    def send(self, line, reset_output=False):
        if reset_output:
            recv_buff = self.receive()
            if len(recv_buff):
                logging.warning("RECV: stdout/stderr has data")

        self._proc.sendline(line)
        recv_buff = self.receive()

        logging.info(F"SEND: {line} RECV:\n" + "-"*20 + F"\n{recv_buff}\n" + "-"*20)

        return recv_buff

    def send_lines(self, lines):
        output = {}
        for line in lines:
            output[line] = self.send(line)
        return output

class ImishAgent(CLIAgent):
    def __init__(self, program, command_delay):
        super(ImishAgent, self).__init__(program, command_delay)
        assert('imish' in program)

    def send_enable(self):
        return self.send('enable')

    def send_terminal_no_monitor(self):
        return self.send('terminal no monitor')

    def send_configure_terminal(self):
        return self.send('configure terminal')

    def send_commit(self):
        return self.send('commit')

    def send_commands(self, commands):
        return self.send_lines(commands)

    def send_configs(self, commands, commit):
        self.send_enable()
        self.send_terminal_no_monitor()
        self.send_configure_terminal()

        self.send_commands(commands)

        if commit:
            self.send_commit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log-level', type=int, default=0)
    parser.add_argument('-p', '--program', default='imish')
    parser.add_argument('-c', '--commands', action='append', default=[])
    parser.add_argument('-d', '--command-delay', type=float, default=0)
    parser.add_argument('--imish-commit', action='store_true')
    parser.add_argument('--imish-config', action='store_true')
    parser.set_defaults(imish_commit=False)
    parser.set_defaults(imish_config=False)
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)

    if args.program in ['imish', '/root/os_bin/imish']:
        agent = ImishAgent(program='/root/os_bin/imish', command_delay=args.command_delay)
        if args.imish_config:
            agent.send_configs(args.commands, commit=args.imish_commit)
        else:
            agent.send_commands(args.commands)
    else:
        agent = CLIAgent(program=args.program, command_delay=args.command_delay)
        agent.send_lines(args.commands)
