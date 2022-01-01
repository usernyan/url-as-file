# url-as-file
A Python program for encoding urls using filename-valid (Win/Mac/Lin) characters in a human-readable way.

## Purpose
This program was written to allow saving images from the web with their source url in the filename, so one can see their origin at a glance and visit it.

## Interactive Program
First, install python ([python.org](https://www.python.org/))

Next, run `url_as_file_interactive.py` and follow the prompts to encode or decode text in your terminal.

## Command-line Interface
Run `python url_as_file_cmd.py -h` in your terminal for help.

## Usage (For Programmers)
Import url_as_file and codecs to start decoding and encoding strings in python:

```python
import url_as_file
import codecs

my_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
result = codecs.encode(my_url, 'url-as-file')
print(result)
decode = codecs.decode(result, 'url-as-file')
print(decode)
```

Output:
```
https;}}www,youtube,com}watch`v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```