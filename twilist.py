#!/usr/bin/env python

import argparse
import os

class Twilist():

    parser = None
    subparsers = None
    filepath = 'twilist'
    file = None
    text_max_length = 150

    def __init__(self, *args, **kwargs):
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers()

        add_subparser = subparsers.add_parser('add')
        add_subparser.add_argument('text')
        add_subparser.add_argument('action', nargs='?', default='draft',
                help="'draft' (default) or 'send'")
        add_subparser.set_defaults(func=self.add_subparser)

        send_subparser = subparsers.add_parser('send')
        send_subparser.add_argument('target', nargs='?', 
                default='first',
                help="'first' (default), 'last', 'rand'"\
                     ", or index from list")

        subparsers.add_parser('list')

        self.parser = parser
        self.subparsers = subparsers

        self.file = open(self.filepath, 'a')

    def add_subparser(self, namespace):
        text = namespace.text
        action = namespace.action

        if len(text) > self.text_max_length:
            print "Text longer than %s characters!" % self.text_max_length
            return

        if action == 'draft':
            self.file.write("%s%s" % (text, os.linesep))
            print 'Saved as draft.'

        elif action == 'send':
            print 'Sending tweet without saving..'
            self.send_tweet(text)

    def send_tweet(self, text):
        print 'Sent'

    def process(self):
        cmd = self.parser.parse_args()
        cmd.func(cmd)


if __name__ == "__main__":
    twilist = Twilist()
    twilist.process()
