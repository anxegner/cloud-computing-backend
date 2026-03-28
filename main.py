from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app) # Enable CORS for frontend integration

# Load the trained model at startup
try:
    with open("model.plk", "rb") as file:
        loaded_model = pickle.load(file)
except FileNotFoundError:
    print("Error: sentiment_model.plk not found.")
    loaded_model = None
except Exception as e:
    print(f"Error loading model: {e}")
    loaded_model = None

@app.route("/")
def health():
    return {"message": "Sentiment Analysis API is running", "model_loaded": loaded_model is not None}

@app.route("/api", methods=["POST", "GET"])
def sentiment_api():
    if not loaded_model:
        return jsonify({"error": "Model not loaded on server"}), 500

    # Accept JSON POST with {"sentence": "..."}
    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
        sentence = payload.get("sentence")
        if not sentence:
            return jsonify({"error": "No sentence provided. Expected JSON: {\"sentence\": \"your text here\"}"}), 400
    else:
        # Fallback for GET request (testing/debugging)
        sentence = request.args.get("sentence") or "The sky looks great today!"

    try:
        pred = loaded_model.predict([sentence])
        sentiment = pred[0]
        
        # Calculate confidence score if the model supports it
        confidence = None
        if hasattr(loaded_model, "predict_proba"):
            proba = loaded_model.predict_proba([sentence])
            confidence = float(proba.max())

        return jsonify({
            "sentence": sentence,
            "sentiment": str(sentiment),
            "confidence": confidence,
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # OpenShift uses port 8080 by default for non-root containers
    app.run(host="0.0.0.0", port=8080)