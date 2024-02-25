from flask import Flask, jsonify, request
import numpy as np
import tensorflow as tf
from keras.models import load_model
import base64

app = Flask(__name__)

# Load the trained model (Adjust the path as necessary)
#model_path = 'C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024(2)\\brishackapp\\FruitModel.keras'
model_path = './FruitModel.keras'
model = load_model(model_path)
IMAGE_SIZE = 100
#All possible fruits
tr_class_names = ['Apple Braeburn',
 'Apple Crimson Snow',
 'Apple Golden 1',
 'Apple Golden 2',
 'Apple Golden 3',
 'Apple Granny Smith',
 'Apple Pink Lady',
 'Apple Red 1',
 'Apple Red 2',
 'Apple Red 3',
 'Apple Red Delicious',
 'Apple Red Yellow 1',
 'Apple Red Yellow 2',
 'Banana',
 'Banana Lady Finger',
 'Banana Red',
 'Cherry 1',
 'Cherry 2',
 'Cherry Rainier',
 'Cherry Wax Black',
 'Cherry Wax Red',
 'Cherry Wax Yellow',
 'Grape Blue',
 'Grape Pink',
 'Grape White',
 'Grape White 2',
 'Grape White 3',
 'Grape White 4',
 'Grapefruit Pink',
 'Grapefruit White',
 'Guava',
 'Lychee',
 'Pineapple',
 'Pineapple Mini',
 'Rambutan',
 'Raspberry',
 'Redcurrant',
 'Salak']
@app.route('/upload', methods=['POST'])
def upload():
    string = request.json
    if "," in string:
        string = string.split(",")[1]
    print(request.json, flush=True) 
    path = "./real_assets/Assets/test.jpeg"
    bdata= base64.b64decode(string)
    print(bdata, flush=True)
    with open(path, "wb") as f:
        f.write(bdata)
    
    res = classify_images()
    return {"upload": res}

def classify_images():
    # Specify the directory containing images (Adjust the path as necessary)
    #test_subset = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024(2)\\brishackapp\\real_assets"
    test_subset = "./real_assets"
    test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        test_subset,
        seed=42,
        shuffle=True,
        image_size=(IMAGE_SIZE, IMAGE_SIZE),
        batch_size=1  
    )

    predictions = []
    for images, _ in test_dataset.take(1):  # Adjust the number of images as needed
        img_array = tf.keras.preprocessing.image.img_to_array(images[0])
        img_array = tf.expand_dims(img_array, 0)  # Model expects a batch of images
        preds = model.predict(img_array)
        predicted_class = tr_class_names[np.argmax(preds[0])]
        confidence = round(100 * (np.max(preds[0])), 2)
        if confidence > 85:
            predictions.append({"class": predicted_class, "confidence": confidence})
        else:
            predictions.append({"class": "No Fruit Detected", "confidence": 0})
    return jsonify(predictions)

@app.route('/test')
def test():
    return {"test": ["Blurb..."]}

if __name__ == '__main__':
    app.run(debug=True)
