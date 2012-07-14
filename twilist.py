#!/usr/bin/env python

import argparse

class Twilist():
    parser = None
    args = None

    def __init__(self, *args, **kwargs):
        self.parser = argparse.ArgumentParser()

    def process(self):
        self.args = self.parser.parse_args()


if __name__ == "__main__":
    twilist = Twilist()
    twilist.process()
