from replacer import find_iterator, replace_iterator

import argparse
import os

parser = argparse.ArgumentParser(prog='replacer', description="Perform find and replace operations throughout the current directory.")

parser.add_argument('-v',
                    '--version',
                    action='version',
                    version='%(prog)s 0.1.0')
parser.add_argument('-f',
                    '--find',
                    help='Count the number of times that a string appears in the current directory.',
                    metavar='find',
                    type=str,)
parser.add_argument('-r',
                    '--replace',
                    help='Find every instance of a string in the current directory and replace it with a new string.',
                    metavar=('find', 'replace'),
                    nargs=2,
                    type=str)

args = parser.parse_args()

directory = os.path.abspath(os.path.curdir)

if __name__ == '__main__':

    if args.find:
        find_iterator(directory, args.find)

    elif args.replace:
        replace_iterator(directory, args.replace[0], args.replace[1])
