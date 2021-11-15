from flask import Flask
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def getRandomMeme():
    return jsonify(url="abc.xyz")


app.run()