import codecs
import string
from typing import Tuple

escape_char = "!"
_encode_table = {
    escape_char:  escape_char,
    #replace illegal chars
    "\\": "{",
    "/":  "}",
    "<":  "[",
    ">":  "]",
    ":":  ";",
    "*":  "+",
    "?":  "`",
    "\"": "'",
    "|":  "~",
    #avoid filename extension confusion
    ".":  ","
}
_decode_table = {v: k for k, v in _encode_table.items()}


#Put the escape character in front of literal characters.
def url_as_file_encode(url: str) -> Tuple[str, int]:
    l = []
    for x in url:
        if x in _decode_table.keys():
            l.append(escape_char + x)
        elif x in _encode_table.keys():
            l.append(_encode_table[x])
        else:
            l.append(x)
    return ''.join(l), len(url)

def url_as_file_decode(text: str) -> Tuple[str, int]:
    out = []
    is_escaped = False
    for c in text:
        if c in _decode_table:
            if is_escaped:
                out.append(c)
                is_escaped = False
            elif c == escape_char:
                is_escaped = True
            else:
                out.append(_decode_table[c])
        else:
            out.append(c)
            #is_escaped = False
    return ''.join(out), len(text)

def url_as_file_search_function(encoding_name):
    return codecs.CodecInfo(url_as_file_encode, url_as_file_decode, name='url-as-file')

codecs.register(url_as_file_search_function)