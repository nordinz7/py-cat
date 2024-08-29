#!/usr/bin/python3

import sys
from utils import parse_args

# file name optional '-' or empty #support mulitple files
# if filename empty read from stdin
# -n print number lines
# -b print number non-blank lines

args = sys.argv[1:]

options = parse_args(args)

if not options['files']:
    piped = sys.stdin.read()
    piped_list = piped.split('\n')
    counter = 0
    for item in piped_list:
        current_increment = 0 if options['numbering_non_blank'] and not item else 1
        counter += current_increment
        print(f"{counter if options['numbering'] or current_increment else ''} {
            item.replace('\n', '')}")
else:
    for file in options['files']:
        with open(file, 'r') as f:
            print(f.read())
