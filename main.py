# main.py
import cv2
from emotion_model import EmotionModel

def main():
    # Load emotion detection model
    model_path = "emotion_detection_model.h5"  # Path to your pre-trained emotion detection model
    emotion_detector = EmotionModel(model_path)

    # Initialize the camera
    camera = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use OpenCV's built-in Haar cascade classifier for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Draw rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Extract the face ROI for emotion prediction
            face_roi = gray_frame[y:y+h, x:x+w]

            # Predict emotion
            predicted_emotion = emotion_detector.predict_emotion(face_roi)

            # Display the predicted emotion
            cv2.putText(frame, predicted_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Emotion Detection', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
