import tensorflow as tf
import os
import numpy as np
class_names = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy']

def process_image(image_path):
    # Load your .h5 model
    model_path = 'apples.h5'
    model = tf.keras.models.load_model(model_path)
    
    # Load and preprocess the image
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(256, 256, 3))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    
    
    img_array = tf.expand_dims(img_array, 0)

    # Make predictions
    predictions = model.predict(img_array)

    # Process predictions and return result
    predicted_class = class_names[np.argmax(predictions[0])]
    # (e.g., convert to human-readable format)
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

    
