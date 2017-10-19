"""
Getting images from URL
Created by Bartosz Kosakowski
Small app to test getting images off of a url containing an image
"""
# import requests
# import io
# from PIL import Image

# def getimage(url):
# 	response = requests.get(url)
# 	img = Image.open(io.BytesIO(response.content));
# 	print(type(img));
# 	img.show();
# getimage("https://www.serebii.net/sunmoon/pokemon/150.png")

from PIL import Image
import urllib.request

URL = 'https://www.serebii.net/sunmoon/pokemon/150.png'

with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')

img.show()