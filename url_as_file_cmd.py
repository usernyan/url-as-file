import argparse
#for encoding/decoding
import url_as_file
import codecs
#for input streams
import io
import sys

parser = argparse.ArgumentParser(description="encode or decode urls to valid filenames")
parser.add_argument('-d', '--decode', action='store_true', help="use decode mode instead of encode mode")
parser.add_argument('url', type=str, default="", nargs="?",
                    help='the url to encode/decode. (default value is the empty string. put this inside single quotes to avoid the shell parsing its contents).')
parser.add_argument('-f', '--file', type=str, help='read input from a specified file')
parser.add_argument('-s', '--stdin', action='store_true',
                    help='read input from stdin. (this is often user input. enter Ctrl+d on Linux/Unix or Ctrl+z on Windows to stop the program.)')
args = parser.parse_args()

def instream_parse(in_stream, decode):
    if decode:
        func = codecs.decode
    else:
        func = codecs.encode
    for url in in_stream:
        res = func(url, 'url-as-file')
        print(res, end='')

if args.stdin:
    instream_parse(sys.stdin, args.decode)
elif args.file:
    with open(args.file, 'r', encoding='utf-8') as user_file:
        instream_parse(user_file, args.decode)
else:
    instream_parse(io.StringIO(args.url), args.decode)
