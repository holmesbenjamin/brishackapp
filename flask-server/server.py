from flask import Flask, jsonify, request
import numpy as np
import tensorflow as tf
from keras.models import load_model
import base64
from io import BytesIO
from rembg import remove 
from PIL import Image
from openai import OpenAI
app = Flask(__name__)

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who is the prime minister of the UK",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.choices[0].message.content)
# Load the trained model (Adjust the path as necessary)
#model_path = 'C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024(2)\\brishackapp\\FruitModel.keras'
# model_path = './FruitModel.keras'
# model = NewModel()
# IMAGE_SIZE = 100
# #All possible fruits
# tr_class_names = ['Apple Braeburn',
#  'Apple Crimson Snow',
#  'Apple Golden 1',
#  'Apple Golden 2',
#  'Apple Golden 3',
#  'Apple Granny Smith',
#  'Apple Pink Lady',
#  'Apple Red 1',
#  'Apple Red 2',
#  'Apple Red 3',
#  'Apple Red Delicious',
#  'Apple Red Yellow 1',
#  'Apple Red Yellow 2',
#  'Banana',
#  'Banana Lady Finger',
#  'Banana Red',
#  'Cherry 1',
#  'Cherry 2',
#  'Cherry Rainier',
#  'Cherry Wax Black',
#  'Cherry Wax Red',
#  'Cherry Wax Yellow',
#  'Grape Blue',
#  'Grape Pink',
#  'Grape White',
#  'Grape White 2',
#  'Grape White 3',
#  'Grape White 4',
#  'Grapefruit Pink',
#  'Grapefruit White',
#  'Guava',
#  'Lychee',
#  'Pineapple',
#  'Pineapple Mini',
#  'Rambutan',
#  'Raspberry',
#  'Redcurrant',
#  'Salak']

def get_message(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Give me the nutritional values of 1 {fruit} and the health benefits of these molecules.


@app.route('/upload', methods=['POST'])
def upload():
    # Parse the uploaded image
    string = request.json
    if "," in string:
        string = string.split(",")[1]
    path = "./real_assets/Assets/test.jpeg"
    bdata = base64.b64decode(string)
    # Make the image transparent (white bg)
    og_file = Image.open(BytesIO(bdata))
    transparent_file = remove(og_file).convert("RGBA")
    background = Image.new('RGBA', transparent_file.size, (255, 255, 255))
    alpha_composite = Image.alpha_composite(background, transparent_file).convert("RGB")
    alpha_composite.save(path, "JPEG")
    # Run the image through the model
    res = classify_images()
    # Get GPT message
    message = get_message("Give me the nutritional values of 1 " + res + " and the health benefits of these molecules.")
    return {"upload": message}

def classify_images():
    return "Apple"
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
    return predictions

@app.route('/test')
def test():
    return {"test": ["Blurb..."]}

if __name__ == '__main__':
    app.run(debug=True)
