#!/usr/bin/env python

import argparse
import os
from random import randint
from subprocess import call

class TwilistException(Exception): pass


class Twilist():

    parser = None
    subparsers = None
    filepath = 'twilist'
    text_max_length = 150
    list = None

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
        send_subparser.set_defaults(func=self.send_subparser)

        list_subparser = subparsers.add_parser('list')
        list_subparser.set_defaults(func=self.list_subparser)

        self.parser = parser
        self.subparsers = subparsers

        try:
            file = open(self.filepath, 'r')
            self.list = [line.replace(os.linesep, '') for line in file]
            file.close()
        except IOError:
            self.list = []

    def append_list(self, text):
        self.list.append(text)
        self.save_list()

    def pop_list(self, index):
        if len(self.list) == 0:
            raise TwilistException("You don't have list of tweets")

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

    def send_subparser(self, namespace):
        target = namespace.target
        text = None

        try:

            if target == 'first':
                text = self.pop_list(0)
                print 'Sending first tweet..\r\n%s' % text

            elif target == 'last':
                text = self.pop_list(len(self.list)-1)
                print 'Sending latest tweet..\r\n%s' % text
            
            elif target == 'rand':
                index = randint(0, len(self.list)-1)
                text = self.pop_list(index)
                print 'Sending tweet #%s\r\n%s' % (index, text) 

            else:
                try:
                    index = int(target)
                    text = self.pop_list(index)
                    print 'Sending tweet #%s\r\n%s' % (index, text) 
                except ValueError:
                    print "Provide a valid index, -h for help"

        except TwilistException, e:
            print e

        else:
            if text:
                self.send_tweet(text)

    def list_subparser(self, namespace):
        print "List of draft tweets:"
        print "ID\tTweet"
        print "=========================="
        for index, text in enumerate(self.list):
            print "%s\t%s" % (index, text)

    def send_tweet(self, text):
        command = ['twidge', 'update', text]
        call(command)

    def process(self):
        cmd = self.parser.parse_args()
        cmd.func(cmd)


if __name__ == "__main__":
    twilist = Twilist()
    twilist.process()
