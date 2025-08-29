from flask import Flask, request, jsonify
from PIL import Image
import io
import numpy as np

#Use tensorflow/Keras
from tenserflow.keras.applications.mobilenet_v2 import (MobileNetV2, prepocess_input, decode_predictions)

from tensorflow.keras.processing import image

app = Flask(__name__)
model = MobileNetV2(weights='imagenet') #same as in docker file

@app.route('/health', methods=['GET'])
def health():
  return {'status': 'ok'}, 200

@app.route('/predict', methods=['POST'])
def predict():
  #Get the image from the request
  img_file = request.files.get('image')
  if not img_file:
    return jsonify({'error': 'No image provided' }), 400
  
  #Prepocess the image
  img = Image.open(io.BytesIO(img_file.read()))
  img = img.resize((224, 224))
  img_arry = image.img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)
  img_array = prepocess_input(img_array)

  #Make a prediction
  preds = model.predict(img_array)
  decoded = decode_predictions(preds, top=3)[0]

  #Return the predictions
  return jsonify(decoded)

if __name__ == '__main__':
  #this dev server; production server uses gunicorn
  app.run(host='0.0.0.0', port=8080, debug=False)
