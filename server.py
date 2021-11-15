from flask import Flask, Response, jsonify, send_file, request

import imageUtils

app = Flask(__name__)


@app.route("/")
def getRandomMeme(methods=['GET']):
    return jsonify(url="abc.xyz")


@app.route("/image/<imageId>")
def getPngImage(imageId, methods=['GET']):
    if imageId.endswith(".png"):
        return send_file(f"images/{imageId}")
    else:
        return send_file(f"images/{imageId}.png")


@app.route("/jpg-to-png")
def img_to_png():
    url = request.args.get("url")

    endId = imageUtils.imgToJPG(url)
    return jsonify(id=endId, url=f"/image/{endId}.png")


app.run()
