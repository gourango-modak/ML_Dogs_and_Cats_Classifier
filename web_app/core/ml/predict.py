import tensorflow
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from .config import configuration
from sklearn.linear_model import SGDClassifier
import numpy as np
import os
import joblib
from django.conf import settings
import cv2

def predict_cat_vs_dog(image):
    trained_model = settings.BASE_DIR / "core/ml/output/cats_and_dogs_detection.sav"

    # image = load_img(imagePath, target_size=(224, 224))
    image = cv2.resize(image, (224, 224))
    # image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    model = ResNet50(weights="imagenet", include_top=False)

    features = model.predict(image)
    features = features.reshape((features.shape[0], 100352))


    model = joblib.load(trained_model)
    predicted = model.predict(features)
    return predicted[0]