import base64
import sys
import os
import argparse
import pathlib

import magic



def encode_string(s: str) -> str:
    return base64.b64encode(s.encode(sys.getfilesystemencoding())).decode('ASCII')

def decode_string(s: str) -> str:
    return base64.b64decode(s.encode(sys.getfilesystemencoding())).decode(sys.getfilesystemencoding())

def encode_file(inp: pathlib.Path, out: pathlib.Path) -> None:
    with (
        open(inp, 'rb') as i,
        open(out, 'wb') as o
    ):
        base64.encode(i, o)

def decode_file(inp: pathlib.Path, out: pathlib.Path) -> None:
    with (
        open(inp, 'rb') as i,
        open(out, 'wb') as o
    ):
        base64.decode(i, o)
    ext = magic.from_buffer(open(out, "rb").read(2048), mime=True)

    match ext:
        case None:
            return
        case 'text/plain':
            os.rename(out, f"{out}.txt")
        case _ :
            os.rename(out, f"{out}.{ext.split('/')[1].lower()}")
        
def main() -> None:
    parser = argparse.ArgumentParser(
        prog='base64',
        description='bse64 encoder/decoder')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-es', dest='encode_string', metavar='S', type=str, nargs=1, 
                        help='Encode string to base64 format.')
    group.add_argument('-ds', dest='decode_string', metavar='S', type=str, nargs=1, 
                        help='Decode string from base64 format.')
    group.add_argument('-ef', dest='encode_file', metavar='F', type=pathlib.Path, nargs=2, 
                        help='Encode file to base64 format. First - source, second - destination.')
    group.add_argument('-df', dest='decode_file', metavar='F', type=pathlib.Path, nargs=2, 
                        help='Decode file from base64 format. Don\'t add extension to destination file, program will try to added automatically. First - source, second - destination.')

    args = parser.parse_args()

    if args.encode_string:
        print(encode_string(args.encode_string[0]))
    if args.decode_string:
        print(decode_string(args.decode_string[0]))
    if args.encode_file:
        encode_file(args.encode_file[0], args.encode_file[1])
    if args.decode_file:
        decode_file(args.decode_file[0], args.decode_file[1])


if __name__ == "__main__":
    main()