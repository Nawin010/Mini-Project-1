### Created By Nawin Pro ###

import pyqrcode
import png
from pyqrcode import QRCode
s =str (input("Enter Site : "))
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)


### Coping Is for Cowards ###
