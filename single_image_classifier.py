import numpy as np
import tensorflow as tf
from keras.models import load_model
import matplotlib.pyplot as plt
from keras import layers

# Loadtrained model
#For Ben's computer
# model_path = 'C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\FruitModel.keras'
#For your computer change to location of the model
model_path = 'C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\FruitModel.keras'
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

BATCH_SIZE = 3
#For Ben's computer
#test_subset="C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\real_assets"
#For your computer change to location of the test images
test_subset="C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\real_assets"

test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
   test_subset,
    seed=42,
    shuffle=True,
    image_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE
)

def predict(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array(images[i].numpy())
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = tr_class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

for images, labels in test_dataset.take(12):
    for i in range(BATCH_SIZE):
        if i >= len(images):
            break

        ax = plt.subplot(6, 6, i + 1)
        image = tf.image.resize(images[i], (100, 100))
        plt.imshow(image.numpy().astype("uint8"))
        predicted_class, confidence = predict(model, images[i].numpy())
        plt.title(f"Predicted: {predicted_class}.\n Confidence: {confidence}%", fontsize=8)
        plt.axis("off")

    if i >= BATCH_SIZE - 1:
        break

for i in range(i + 1, BATCH_SIZE):
    plt.subplot(6,6, i + 1)
    plt.axis("off")

plt.tight_layout()
plt.show()































# image_path = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\fruits-360_dataset\\fruits-360\\test\\Banana\\12_100.jpg"

# def load_and_preprocess_image(image_path):
#     img = tf.io.read_file(image_path)
#     img = tf.image.decode_jpeg(img, channels=3)
#     img = tf.image.resize(img, (100, 100))  # Resize the image to the expected input size of the model
#     img = img / 255.0  # Scale image values to [0,1]
#     return img

# def predict_single_image(model, image_path):
#     img = load_and_preprocess_image(image_path)
#     img_array = tf.keras.preprocessing.image.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)  # Model expects a batch of images

#     predictions = model.predict(img_array)
#     predicted_class = ts_class_names[np.argmax(predictions[0])]
#     confidence = round(100 * np.max(predictions[0]), 2)
    
#     return predicted_class, confidence

# # Example usage
# predicted_class, confidence = predict_single_image(model, image_path)
# print(f"Predicted class: {predicted_class}, Confidence: {confidence}%")