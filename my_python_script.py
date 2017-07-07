#!/usr/bin/python3 -B

from __future__ import print_function

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--output', '-o')
parser.add_argument('input')
args = parser.parse_args()

out = open(args.output, 'w')

print("I ignore my input, but that does not matter", file=out)
