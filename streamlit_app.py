import streamlit as st
import cv2
from PIL import Image
import numpy as np

st.title('OpenCV with Streamlit Example')

# Function to apply a grayscale filter
def grayscale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

# Function to apply a blur filter
def blur(img):
    blurred = cv2.GaussianBlur(img, (11,11), 0)
    return blurred

# Function to apply a edge detection filter
def canny(img):
    edges = cv2.Canny(img, 100, 200)
    return edges

# Function to apply a custom filter (you can customize it as per your needs)
def custom_filter(img):
    # Example custom filter
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    filtered = cv2.filter2D(img, -1, kernel)
    return filtered

# Main function
def main():
    st.sidebar.title("Choose an Option")
    choice = st.sidebar.radio("", ("Grayscale", "Blur", "Canny Edge Detection", "Custom Filter"))

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        img_array = np.array(image)

        st.image(image, caption="Original Image", use_column_width=True)

        if choice == 'Grayscale':
            modified_image = grayscale(img_array)
            st.image(modified_image, caption="Grayscale Image", use_column_width=True)

        elif choice == 'Blur':
            modified_image = blur(img_array)
            st.image(modified_image, caption="Blurred Image", use_column_width=True)

        elif choice == 'Canny Edge Detection':
            modified_image = canny(img_array)
            st.image(modified_image, caption="Canny Edge Detection", use_column_width=True)

        elif choice == 'Custom Filter':
            modified_image = custom_filter(img_array)
            st.image(modified_image, caption="Custom Filter Applied", use_column_width=True)

if __name__ == '__main__':
    main()
