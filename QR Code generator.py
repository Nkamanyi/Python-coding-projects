import pyqrcode
from pyqrcode import QRCode

def main():

    url = "https://www.youtube.com/watch?v=sWbUDq4S6Y8&t=303s"
    qrcod = pyqrcode.create(url)
    qrcod.svg("Youtube-link.svg", scale=8)

main()