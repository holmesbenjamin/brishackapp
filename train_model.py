import pandas as pd 
import numpy as np

import matplotlib.pyplot  as plt


import os 
import shutil
import tensorflow as tf
from keras.models import Sequential
from keras import layers
from keras.losses import sparse_categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator

dataset_path = 'C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\fruits-360_dataset\\fruits-360'
training_folder_path = os.path.join(dataset_path, 'Training')
test_folder_path = os.path.join(dataset_path, 'Test')

# Counting total labels
# def count_labels(folder_path):
#     label_count = 0
#     for _, dirs, _ in os.walk(folder_path):
#         label_count += len(dirs)
#         break  # Only count the top-level directories and exit the loop
#     return label_count

# num_labels = count_labels(training_folder_path)
# print(f"Number of labels (folders) in the training dataset: {num_labels}")

# # Get a list of all labels (subfolder names) within the training folder
# labels = [label for label in os.listdir(training_folder_path) if os.path.isdir(os.path.join(training_folder_path, label))]

# # Sort the labels alphabetically
# sorted_labels = sorted(labels)

# # Print the list of labels
# print("Sorted Labels:")
# for label in sorted_labels:
#     print(label)

# creating a folder for filtered dataset in the working directory

# def create_folders(destination_path):
#     # Create "filtered_dataset" folder directly
#     os.makedirs(destination_path, exist_ok=True)

#     # Create "training" and "test" folders within "filtered_dataset"
#     training_path = os.path.join(destination_path, "training")
#     test_path = os.path.join(destination_path, "test")
#     os.makedirs(training_path, exist_ok=True)
#     os.makedirs(test_path, exist_ok=True)

# if __name__ == "__main__":
#     destination_path = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024"
#     create_folders(destination_path)

#     print(f"filtered_dataset folder created successfully in {destination_path}")
#     print(f"Training folder created successfully in {destination_path}.")
#     print(f"Test folder created successfully in {destination_path}.")
    
def copy_selected_folders(source_path, destination_path, selected_fruits):
    if not os.path.exists(source_path):
        print("Source path does not exist.")
        return

    source_folders = os.listdir(source_path)
    for fruit_pattern in selected_fruits:
        fruit_pattern = fruit_pattern.lower()  # Make sure the fruit pattern is in lowercase
        fruit_folder_matches = [f for f in source_folders if f.lower().startswith(fruit_pattern)]

        if not fruit_folder_matches:
            print(f"No variants found for '{fruit_pattern}'.")
            continue

        for source_folder in fruit_folder_matches:
            fruit_name = source_folder
            source_folder = os.path.join(source_path, source_folder)
            destination_folder = os.path.join(destination_path, fruit_name)
            try:
                shutil.copytree(source_folder, destination_folder)
                print(f"Fruit '{fruit_name}' copied successfully in {destination_path}.")
            except FileExistsError:
                print(f"Fruit '{fruit_name}' already exists in the destination path.")
                
# copy fruit folders to training folder
if __name__ == "__main__":
    source_path = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\fruits-360_dataset\\fruits-360\\Training"
    destination_path = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\training"
    
    # Selecting the fruit names to copy all variants
    selected_fruits = ["Apple","Banana", "Cherry","Guava","Grape","Lychee","Pineapple","Rambutan","Raspberry","Redcurrant","Salak"]
  
    copy_selected_folders(source_path, destination_path, selected_fruits)
                
if __name__ == "__main__":
    source_path = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\fruits-360_dataset\\fruits-360\\Test"
    destination_path = "C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\test"
    
    # Selecting the fruit names to copy all variants
    selected_fruits = ["Apple","Banana", "Cherry","Guava","Grape","Lychee","Pineapple","Rambutan","Raspberry","Redcurrant","Salak"] 
  
    copy_selected_folders(source_path, destination_path, selected_fruits)
    
training_subset="C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\training"
test_subset="C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\test"

# function to count images in each folder
def count_images_per_label(folder_path):
    label_counts = {
        label: len(os.listdir(os.path.join(folder_path, label)))
        for label in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, label))
    }

    return label_counts

if __name__ == "__main__":
    # Count images in training folders
    training_label_counts = count_images_per_label(training_subset)
    test_label_counts = count_images_per_label(test_subset)
    sorted_training_label_counts = sorted(training_label_counts.items(), key=lambda x: x[1], reverse=True)
    sorted_test_label_counts = sorted(test_label_counts.items(), key=lambda x: x[1], reverse=True)
print("Training Label Counts (sorted by count):")
for label, count in sorted_training_label_counts:
    print(f"{label}: {count}")
print("Test Label Counts (sorted by count):")
for label, count in sorted_test_label_counts:
    print(f"{label}: {count}")

#counting number of images
def count_total_images(folder_path):
    total_images = 0
    for _, _, files in os.walk(folder_path):
        total_images += len(files)
    return total_images

total_images_count = count_total_images(dataset_path)
total_train_images_count = count_total_images(training_subset)
total_test_images_count = count_total_images(test_subset)

#Display total number of images in each folder of the dataset
print(f"Total number of images in the main dataset: {total_images_count}")
print(f"Total number of images in the training dataset: {total_train_images_count}")
print(f"Total number of images in the test dataset: {total_test_images_count}")

# # Combine the training and test label counts into a single dictionary
# combined_label_counts = {
#     label: training_label_counts.get(label, 0) + test_label_counts.get(label, 0)
#     for label in set(list(training_label_counts.keys()) + list(test_label_counts.keys()))
# }

# # Create a DataFrame to hold the combined fruit counts
# df_fruit_counts = pd.DataFrame({"Fruit Labels": list(combined_label_counts.keys()), "Count": list(combined_label_counts.values())})

# # Sort the DataFrame by the counts in descending order
# df_fruit_counts = df_fruit_counts.sort_values(by="Count", ascending=False)

# # Select the top 15 fruit labels by count
# top_15_fruits = df_fruit_counts.head(15)

# # Plot the horizontal bar chart using Seaborn
# plt.figure(figsize=(10, 8))
# sns.barplot(x="Count", y="Fruit Labels", data=top_15_fruits, palette="YlOrRd")
# plt.xlabel("Count")
# plt.ylabel("Fruit Labels")
# plt.title("Top 15 Fruit Labels by Count")
# plt.show()

BATCH_SIZE = 32
IMAGE_SIZE = 100
CHANNELS = 3
EPOCHS = 10

# training dataset pipeline
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    training_subset,
    seed=42,
    shuffle=True,
    image_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE
)

tr_class_names = train_dataset.class_names
tr_class_names

# define a function to split the dataset 
def get_dataset_partitions_tf(ds, train_split=0.8, val_split=0.2, shuffle=True, shuffle_size=10000):
    assert (train_split + val_split) == 1

    ds_size = len(ds)

    if shuffle:
        ds = ds.shuffle(shuffle_size, seed=1234)

    train_size = int(train_split * ds_size)
    val_size = int(val_split * ds_size)

    train_ds = ds.take(train_size)
    val_ds = ds.skip(train_size).take(val_size)

    return train_ds, val_ds

train_ds, val_ds = get_dataset_partitions_tf(train_dataset)
#print length of each set
print("Training dataset length",len(train_ds))
print("Validation dataset length",len(val_ds))

# Optimization for Training and Validation Datasets by caching and shuffling
train_ds = train_ds.cache().shuffle(100).prefetch(buffer_size=tf.data.AUTOTUNE)
val_ds = val_ds.cache().shuffle(100).prefetch(buffer_size=tf.data.AUTOTUNE)

# resize and rescaling images to a specified size 
resize_and_rescale = tf.keras.Sequential([
  layers.experimental.preprocessing.Resizing(IMAGE_SIZE, IMAGE_SIZE),
  layers.experimental.preprocessing.Rescaling(1./255),
])

# prefetching the training data to optimize pipeline
train_ds = train_ds.prefetch(buffer_size=tf.data.AUTOTUNE)

# Defining the shape of the input data batch for CNN
input_shape = (BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, CHANNELS)

# Number of outputs
n_classes = len(tr_class_names)
n_classes

# CNN model
model = Sequential([
    resize_and_rescale,
    layers.Conv2D(32, kernel_size = (3,3), activation='relu', input_shape=input_shape),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(32, kernel_size = (3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, kernel_size =(3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, kernel_size =(3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, kernel_size = (3,3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.25),
    layers.Dense(n_classes, activation='softmax'),
])

model.build(input_shape=input_shape)
model.summary()

# specifying the optimizer and model metrics
model.compile(
    optimizer='rmsprop',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# saving the model training history
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=EPOCHS
)

model.save('C:\\Users\\benho\\OneDrive\\Desktop\\Ben\\Programs\\BH2024\\FruitModel.keras')

#Plotting train & validation loss
plt.figure()
plt.plot(history.history["loss"],label = "Train Loss", color = "black")
plt.plot(history.history["val_loss"],label = "Validation Loss", color = "blue", linestyle="dashed")
plt.title("Model Losses", color = "darkred", size = 15)
plt.legend()
plt.show()

#Plotting train & validation accuracy
plt.figure()
plt.plot(history .history["accuracy"],label = "Train Accuracy", color = "black")
plt.plot(history .history["val_accuracy"],label = "Validation Accuracy", color = "blue", linestyle="dashed")
plt.title("Model Accuracy", color = "darkred", size = 15)
plt.legend()
plt.show()


# test dataset pipeline
test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
   test_subset,
    seed=42,
    shuffle=True,
    image_size=(IMAGE_SIZE,IMAGE_SIZE),
    batch_size=BATCH_SIZE
)

ts_class_names = test_dataset.class_names
# Fetching model predictions for sample image in test dataset
plt.figure(figsize=(3, 3))
for images_batch, labels_batch in test_dataset.take(1):

    first_image = images_batch[0].numpy().astype('uint8')
    first_label = labels_batch[0].numpy()
    print("first image to predict")
    plt.imshow(first_image)
    print("actual label:",ts_class_names[first_label])

    batch_prediction = model.predict(images_batch)
    print("predicted label:",tr_class_names[np.argmax(batch_prediction[0])])