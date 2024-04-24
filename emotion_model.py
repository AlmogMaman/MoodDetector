# emotion_model.py
import tensorflow as tf
from keras.models import load_model

class EmotionModel:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def predict_emotion(self, image):
        # Preprocess the image (resize and normalize)
        resized_img = tf.image.resize(image, (48, 48))
        normalized_img = resized_img / 255.0
        expanded_img = tf.expand_dims(normalized_img, axis=0)

        # Predict emotion
        predictions = self.model.predict(expanded_img)
        emotion_label = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
        predicted_emotion = emotion_label[predictions.argmax()]
        return predicted_emotion
