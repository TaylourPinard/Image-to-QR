'''
    My implementation of an image to qr code generator
    Project takes the name of an image in the same directory
    as image_to_qr.py and uploads it to imgbb.com using an api key
    project then converts that image url into a qr code that
    when scanned will take you directly to the image
'''

import requests
import base64
import qrcode
from sys import argv


url = "https://api.imgbb.com/1/upload"
api_key = "your api key here"


def main():
    b64 = convert()
    img_url = image_upload(url, api_key, b64)
    qr_code(img_url)


# convert the image to base64
def convert():
    with open("b64.txt", "wb") as out:
        with open(argv[1], "rb") as file:
            base_64 = base64.b64encode(file.read())
    return base_64


# uploads the image to imgbb.com and returns the
# link to the image
def image_upload(url, api_key, b64):
    r = requests.post(url, params = {"key" : api_key}, data = {"image": b64})
    r = r.json()
    return r["data"]["url"]


# generate qr code for the image url
def qr_code(url):
    qr = qrcode.make(url)
    qr.save("qr_code.png")


if __name__ == "__main__":
    main()