
#!/usr/bin/env python3
import sys
import logging
import argparse
import cli_agent
from xml.etree import ElementTree
from yangson import DataModel
from vht.impl.translators import XMLRootTranslator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log-level', type=int, default=0)
    parser.add_argument('-y', '--yang-module-define', default='/etc/yang-library.json')
    parser.add_argument('-Y', '--yang-module-path', action='append', default=["/usr/share/yuma/modules/vht",
                                                                              "/usr/share/yuma/modules/ietf",
                                                                              "/root/vht/yang/modules",
                                                                              "../test-yangson/yangson/yang-modules/ietf"])
    parser.add_argument('-c', '--candidate', default=None)
    parser.add_argument('-r', '--running', default=None)
    parser.add_argument('-e', '--extra-commands', action='append', default=[])
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--test-get-cli-only', action='store_true')
    parser.set_defaults(dry_run=False)
    parser.set_defaults(test_get_cli_only=False)
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level)


    dm = DataModel.from_file(args.yang_module_define, args.yang_module_path)

    if args.candidate:
        logging.debug("[CANDIDATE]: at {args.candidate}")
    else:
        logging.debug("[CANDIDATE 1]: at {args.candidate}")

    if args.running:
        logging.debug("[RUNNING]: at {args.running}")
    else:
        logging.debug("[RUNNING 1]: at {args.running}")

    #try:
    #    agent = cli_agent.ImishAgent(program='/root/os_bin/imish', command_delay=0.1)
    #    file.write("hello app5")
    #except:
    #    file.write("hello app6")
    #    exit(1)

    with open (args.candidate, 'r') as file:
        before_data = file.read()
    with open (args.running , 'r') as file:
        after_data = file.read()

    logging.debug(before_data)
    logging.debug(after_data)
    p = XMLRootTranslator(dm, candidate=after_data, running=before_data)
    commands = p.process()

    logging.debug("[CLI] commands sent to IMISH: >>>>{commands}<<<<")


        #if not args.test_get_cli_only:
        #    agent.send_configs(args.commands, commit=args.dry_run)

    #elif args.extra_commands:
    #    logging.debug("[CLI] commands sent to IMISH: {args.extra_commands}")
    #    if not args.test_get_cli_only:
    #        agent.send_lines(args.extra_commands)