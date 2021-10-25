import argparse
"""
Module for rss_reader utility
"""


def get_argparser():
    """This function parses and process arguments input from console. Made with built-in library argparse.
    Returns Namespace-type object
    :return: args
    """
    ver = 'Iteration I'
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
                        help='Outputs verbose status messages', default=False)
    parser.add_argument('--limit',
                        type=int,
                        help='Limit news topics if this parameter provided. For \
    example: --limit 4. Note: --limit -1 shows all available feed',
                        default=-1)
    parser.add_argument('source',
                        help='RSS feed URL',
                        nargs='?',
                        default=None)
    args = parser.parse_args()
    if args.version:
        print(f'Program version: {ver}')
        if args.source is None:
            exit()
    return args
