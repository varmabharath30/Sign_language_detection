import tkinter as tk
from tkinter import filedialog
from tkinter import Label
import numpy as np
from PIL import Image, ImageTk
import tensorflow as tf
import datetime

# Load the trained model
model = tf.keras.models.load_model(r'C:\Users\bhara\OneDrive\Desktop\als-alphabet\my_trained_model.h5')

# Dictionary to map predicted labels to letters
labels = {i: chr(65 + i) for i in range(26)}  # Mapping 0-25 to A-Z

def preprocess_image(image_path):
    """
    Preprocess the image to be compatible with the model.
    Resizes it to 28x28 and normalizes the pixel values.
    """
    image = Image.open(image_path).convert('L')  
    image = image.resize((28, 28))  
    image = np.array(image) / 255.0  
    image = np.expand_dims(image, axis=-1)  
    image = np.expand_dims(image, axis=0) 
    return image

def predict_sign(image_path):
    image = preprocess_image(image_path)
    prediction = model.predict(image)
    predicted_label = np.argmax(prediction, axis=1)[0]
    return labels[predicted_label]

def is_valid_time():
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(18, 0)  
    end_time = datetime.time(22, 0) 
    return start_time <= current_time <= end_time

def upload_image():
    if not is_valid_time():
        result_label.config(text="Predictions are allowed only between 6 PM and 10 PM.")
        return
    
    file_path = filedialog.askopenfilename()
    if file_path:
        # Display uploaded image
        img = Image.open(file_path)
        img.thumbnail((200, 200))  
        img = ImageTk.PhotoImage(img)
        panel.configure(image=img)
        panel.image = img  

        # Show the prediction
        result = predict_sign(file_path)
        result_label.config(text=f'Predicted Sign: {result}')

# Create GUI
root = tk.Tk()
root.title("Sign Language Detection")
root.geometry("400x400")

# Upload button
upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=20)

# Panel to display uploaded image
panel = Label(root)
panel.pack(pady=20)

# Label to display the result
result_label = Label(root, text="Predicted Sign: ", font=("Helvetica", 16))
result_label.pack(pady=20)

# Main loop
root.mainloop()

