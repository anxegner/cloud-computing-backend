from flask import Flask, request
import pickle

app = Flask(__name__)


@app.route("/")
def health():
    return {"message": "Hello, World!"}

@app.route("/api", methods=["POST", "GET"])
def sentiment_api():
    # # Accept JSON POST with {"sentence": "..."}; fallback sample for GET
    # if request.method == "POST":
    #     payload = request.get_json(silent=True) or {}
    #     sentence = payload.get("sentence")
    #     if not sentence:
    #         return {"error": "no sentence provided"}, 400
    # else:
    sentence = "The sky looks great today!"


    # try:
    #     pred = loaded_model.predict([sentence])
    #     sentiment = pred[0]
    # except Exception as e:
    #     return {"error": str(e)}, 500

    return {"sentence": sentence, "sentiment": str(sentiment)}