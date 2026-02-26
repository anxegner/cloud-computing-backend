from flask import Flask
from flask import request
import pickle
import sklearn

app = Flask(__name__)

with open("sentiment_model.plk", "wb") as file:
    loaded_data = pickle.load(file)

@app.route("/")
def health():
    return {"message": "Hello, World!"}

@app.route("/api", methods=["POST", "GET"])
def sentiment_api():
 
    data = request.get_json()
    return {"sentence": "The sky looks great today!", "sentiment": "positive"}