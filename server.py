from flask import Flask, Response, jsonify

app = Flask(__name__)

@app.route("/")
def getRandomMeme(methods=['GET']):
    return jsonify(url="abc.xyz")


app.run()
