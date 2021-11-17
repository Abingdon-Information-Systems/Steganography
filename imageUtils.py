from PIL import Image
import requests
from io import BytesIO
import os.path
import random


def getImageFromUrl(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def getImageID(source):
    if "//" in source:
        source = source.split("//")[1]  # remove protocol information
    source = source.replace("/", ".")
    while os.path.isfile(f"images/{source}.png"):  # make sure it is unique, don't overwrite currently written files
        source += str(random.randrange(0, 10))  # TODO add a check that means identical files are grouped.
    return source


def imgToJPG(url):
    endPath = getImageID("".join(url.split("//")[:-1]))

    jpgImage = getImageFromUrl(url)

    jpgImage.save(f"images/{endPath}.png", format="png")

    return endPath


def savePNG(image, id):
    image.save(f"images/{id}.png", format="png")
