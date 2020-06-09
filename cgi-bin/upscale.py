#!/usr/bin/python3

import cgi, os
import random
import string
from ISR.models import *
import numpy as np
from PIL import Image
log_file = "log_file"

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(stringLength))

form = cgi.FieldStorage()
file = form['file'].file
token = randomString(4)
open(f"data{os.sep}{token}.png", "wb").write(file.read())

img = Image.open(f"data{os.sep}{token}.png")
lr_img = np.array(img)

#rrdn = RRDN(weights='gans')
rdn = RDN(weights='psnr-small')
sr_img = rdn.predict(lr_img)
img = Image.fromarray(sr_img)

img.save(f"data{os.sep}{token}_res.png")

print("Content-Type: text/plain")
print()#end headers
print(token)

