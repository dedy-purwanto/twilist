#!/usr/bin/env python

import argparse

class Twilist():

    parser = None
    args = None

    def __init__(self, *args, **kwargs):
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers()

        add_subparser = subparsers.add_parser('add')
        add_subparser.add_argument('text')

        send_subparser = subparsers.add_parser('send')
        send_subparser.add_argument('target', nargs='?',
                help='first, last, rand, or index from list')

        subparsers.add_parser('list')

        self.parser = parser


    def process(self):
        self.args = self.parser.parse_args()


if __name__ == "__main__":
    twilist = Twilist()
    twilist.process()
