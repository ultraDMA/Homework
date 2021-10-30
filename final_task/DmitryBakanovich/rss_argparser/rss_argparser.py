#!/usr/bin/env python
"""Console input parsing module for rss_reader utility"""

import argparse
import sys
import os
sys.path.append(os.getcwd())

def get_argparser():
    """This function parses and process arguments input from console. Made with built-in library argparse.
    Returns Namespace-type object
    :return: Namespace (args)
    """
    ver = '0.4.0'
    parser = argparse.ArgumentParser(
        prog='rss_reader.py',
        description='Pure Python command-line RSS reader.')
    parser.add_argument('--version', '--V',
                        action='store_true',
                        help='Print version info')
    parser.add_argument('--json',
                        action='store_true',
                        help='Print result as JSON in stdout')
    parser.add_argument('--verbose', '--v',
                        action='store_true',
                        help='Outputs verbose status messages')
    parser.add_argument('--limit',
                        type=int,
                        help='Limit news topics if this parameter provided. For \
    example: --limit 4. Note: --limit -1 shows all available feed',
                        default=-1)
    parser.add_argument('source',
                        help='RSS feed URL',
                        nargs='?',
                        default=None)
    parser.add_argument('--date',
                        help='The cashed news can be read with it. For example: `--date 20191020`\
                            The new from the specified day will be printed out.',
                        type=int,
                        default=None)
    parser.add_argument('--to-pdf',
                        help='Converts news to PDF format --to-pdf',
                        action='store_true',
                        )
    parser.add_argument('--to-html',
                        help='Converts news to HTML format --to-html',
                        action='store_true')
    args = parser.parse_args()
    if args.version:
        print(f'Program version: {ver}')
        if args.source is None:
            exit()

    return args
