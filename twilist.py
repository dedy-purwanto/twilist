#!/usr/bin/env python

import argparse
import os
from random import randint
from subprocess import call

class TwilistException(Exception): pass


class Twilist():

    parser = None
    subparsers = None
    default_file = 'twilist'
    filepath = None
    text_max_length = 150
    list = None

    def __init__(self, *args, **kwargs):
        parser = argparse.ArgumentParser()

        parser.add_argument('--file', default=self.default_file)

        subparsers = parser.add_subparsers()

        add_subparser = subparsers.add_parser('add')
        add_subparser.add_argument('text')
        add_subparser.add_argument('action', nargs='?', default='draft',
                help="'draft' (default) or 'send'")
        add_subparser.set_defaults(func=self.add_subparser)

        remove_subparser = subparsers.add_parser('remove')
        remove_subparser.add_argument('index')
        remove_subparser.set_defaults(func=self.remove_subparser)

        send_subparser = subparsers.add_parser('send')
        send_subparser.add_argument('target', nargs='?', 
                default='first',
                help="'first' (default), 'last', 'rand'"\
                     ", or index from list")
        send_subparser.set_defaults(func=self.send_subparser)

        list_subparser = subparsers.add_parser('list')
        list_subparser.set_defaults(func=self.list_subparser)

        self.parser = parser
        self.subparsers = subparsers


    def append_list(self, text):
        self.list.append(text)
        self.save_list()

    def pop_list(self, index):
        text = self.list.pop(index)
        self.save_list()
        return text

    def save_list(self):
        file = open(self.filepath, 'w')
        file.write((os.linesep).join(self.list))

    def add_subparser(self, namespace):
        text = namespace.text
        action = namespace.action

        if len(text) > self.text_max_length:
            print ("Text longer than %s characters!" % 
                    self.text_max_length)
            return

        if action == 'draft':
            self.append_list(text)
            print 'Saved as draft.'

        elif action == 'send':
            print 'Sending tweet without saving..'
            self.send_tweet(text)

    def remove_subparser(self, namespace):
        index = namespace.target

        try:
            index = int(index)
        except ValueError:
            print "Index must be an integer"
            return

        if index < 0 or index >= len(self.list):
            print "Index must be between 0 and %s" % len(self.list)
            return

        self.pop_list(index)

    def send_subparser(self, namespace):
        target = namespace.target
        index = None

        if len(self.list) == 0:
            print "You have no tweet in your list"

        if target == 'first':
            index = 0

        elif target == 'last':
            index = len(self.list)-1
        
        elif target == 'rand':
            index = randint(0, len(self.list)-1)

        else:
            try:
                index = int(target)
                if index <= 0 or index > len(self.list):
                    index = None

            except ValueError:
                print "Provide a valid index, -h for help"

        if index is not None:
            print "Tweet index: 0"
            text = self.list[index]
            if self.send_tweet(text) != 0:
                print "Failed to send tweet due to external error"
            else:
                self.pop_list(index)

    def list_subparser(self, namespace):
        print "List of draft tweets:"
        print "ID\tTweet"
        print "=========================="
        for index, text in enumerate(self.list):
            print "%s\t%s" % (index, text)

    def send_tweet(self, text):
        print "Tweeting: %s" % text
        command = ['twidge', 'update', text]
        return call(command)

    def process(self):
        cmd = self.parser.parse_args()

        self.filepath = cmd.file

        try:
            file = open(self.filepath, 'r')
            self.list = [line.replace(os.linesep, '') for line in file]
            file.close()
        except IOError:
            self.list = []

        cmd.func(cmd)


if __name__ == "__main__":
    twilist = Twilist()
    twilist.process()
