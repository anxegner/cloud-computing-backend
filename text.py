import pickle
import sklearn

# Load the trained model (read-binary)
with open("sentiment_model.plk", "rb") as file:
    loaded_model = pickle.load(file)


sentence = "The sky looks great today!"

try:
    pred = loaded_model.predict([sentence])
    sentiment = pred[0]
    print(sentiment)

except Exception as e:
    print({"error": str(e)}, 500)