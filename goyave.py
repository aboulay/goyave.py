#!/usr/bin/env python3

import argparse
from devices.shell import Shell
from devices.webapp.server import WebServer


def parse_argument():
    description = "Monitor if your services are available."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('configuration_file', metavar='configuration_file',
                        type=str, help='The configuration file path')
    parser.add_argument('--webapp', action='store_true',
                        help='Enable web mode')
    args = parser.parse_args()
    return args


def main():
    arguments = parse_argument()
    if arguments.webapp is True:
        webapp = WebServer(arguments.configuration_file)
        webapp.run()
    else:
        shell = Shell(arguments.configuration_file)
        shell.run()


if __name__ == "__main__":
    main()
