from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np

#Use tensorflow/keras
from tensorflow.keras.applications.mobilenet_v2 import (MobileNetV2, preprocess_input, decode_predictions)

from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = MobileNetV2(weights="imagenet") #same as in docker file

@app.route('/health', methods=['GET'])
def health():
  return {"status": "ok"}, 200

@app.route("/predict", methods=['POST'])
def predict():
  #get the image from the request
  img_file = request.files.get('image')
  if not img_file :
    return jsonify({"error": "No image provided"}), 400
  
  #Preprocess the image
  img = Image.open(io.BytesIO(img_file.read()))
  img = img.resize((224, 224))
  img_array = image.img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)
  img_array = preprocess_input(img_array)

  #Make a prediction
  preds = model.predict(img_array)
  decoded = decode_predictions(preds, top=3)[0]

  #return the predictions
  return jsonify(decoded)

if __name__ == '__main__':
  #this is the dev server, production server uses gunicorn
  app.run(host='0.0.0.0', port=9000, debug=False)
  #curl -X POST http://localhost:8080/predict \
  #-F image=@360_F_236992283_sNOxCVQeFLd5pdqaKGh8DRGMZy7P4XKm.jpg