#!/usr/bin/env python3

import argparse
from devices.shell import Shell


def parse_argument():
    description = "Monitor if your services are available."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('configuration_file', metavar='configuration_file',
                        type=str, help='The configuration file path')
    args = parser.parse_args()
    return args


def main():
    arguments = parse_argument()
    shell = Shell(arguments.configuration_file)
    shell.run()


if __name__ == "__main__":
    main()
