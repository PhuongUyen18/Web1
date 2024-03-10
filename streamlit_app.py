import streamlit as st
import cv2
import os

# Function to take a photo
def take_photo():
    # Open webcam
    cap = cv2.VideoCapture(0)

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Save the captured frame
    if ret:
        cv2.imwrite("C:/Users/Admin/Pictures/Camera Roll/photo.jpg", frame)
        st.success("Photo captured and saved successfully!")

    # Release the camera
    cap.release()

# Streamlit app
def main():
    st.title("Webcam Photo Capture")

    # Button to take photo
    if st.button("Take Photo"):
        take_photo()

if __name__ == "__main__":
    main()
