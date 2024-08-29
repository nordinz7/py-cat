from typing import List


def parse_args(args: List[str]) -> dict:
    options = {'files': [], 'numbering': False, 'numbering_non_blank': False}
    for arg in args:
        if arg == '-n':
            options['numbering'] = True
            options['numbering_non_blank'] = False
        elif arg == '-b':
            options['numbering'] = False
            options['numbering_non_blank'] = True
        elif arg != '-':
            options['files'].append(arg)
    return options
