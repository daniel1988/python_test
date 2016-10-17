#!/usr/bin/python

import re

text = "hello,there,i'm a big big girl,,,,"
print re.split("[,]+", text)

text = '"Hm... err -- are you sure?" he said, sounding insecure.'
print re.findall("[a-zA-Z]+", text)

text = 'Hello,{name}.this is {name}'
print re.sub('{name}', 'Daniel', text)