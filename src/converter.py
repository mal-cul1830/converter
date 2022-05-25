#!/usr/bin/env python3

import sys
import re
from PIL import Image

l = len(sys.argv) #length of argument list
file = sys.argv[1]
filepath = "".join(re.split("\.", file)[0:-1])
img = Image.open(file)

for i in range(2, l):
    format = sys.argv[i]
    img.save(filepath + "." + format)
    print(filepath + "." + format + " created. \nCONVERSION COMPLETE ...")
