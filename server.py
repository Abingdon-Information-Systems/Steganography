import os
import threading
import PIL
from flask import Flask, jsonify, send_file, request, abort
import imageUtils
import imgurRandomMeme

app = Flask(__name__)

getRandomImage = imgurRandomMeme.getRandomImage()
lock = threading.Lock()


@app.route("/")
def getRandomMeme(methods=['GET']):
    with lock:
        url = next(getRandomImage)
    return jsonify(url=url)


@app.route("/meme")
def getMeme():
    with lock:
        url = next(getRandomImage)

    imId = imageUtils.getImageID("".join(url.replace(".png", "").split("//")[-1]))
    imageUtils.savePNG(imageUtils.getImageFromUrl(url), imId)

    return getPngImage(imId)


@app.route("/image/<imageId>")
def getPngImage(imageId, methods=['GET']):
    file_path = f"images/{imageId}" if imageId.endswith(".png") else f"images/{imageId}.png"

    if not os.path.isfile(file_path):
        abort(404)

    return send_file(file_path)


@app.route("/jpg-to-png")
def img_to_png():
    url = request.args.get("url")
    endId = ""
    try:
        endId = imageUtils.imgToJPG(url)
    except PIL.UnidentifiedImageError:
        abort(400)  # if the url is invalid a 400 error should be thrown (I think it should be 400 at least)

    return jsonify(id=endId, url=f"/image/{endId}.png")


app.run()
