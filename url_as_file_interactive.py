import url_as_file #adds url-as-file to codecs
import codecs

enc = lambda x : codecs.encode(x, encoding='url-as-file')
dec = lambda x : codecs.decode(x, encoding='url-as-file')
input_encoded = map(enc, iter(input, ""))
input_decoded = map(dec, iter(input, ""))
print("Enter url text to get it encoded. Enter nothing to move to decode mode.")
[print(i) for i in input_encoded]
print("Enter encoded text to get it decoded. Enter nothing to quit.")
[print(i) for i in input_decoded]