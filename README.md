*Sign Language Detection*
This project focuses on creating a machine learning model that detects and recognizes sign language gestures. The model is trained to predict specific known words using images or real-time video input. The application is designed to operate within a defined time period, such as from 6 PM to 10 PM, providing flexibility for scheduled use.

Features:
Image Upload: Users can upload images containing sign language gestures for the model to recognize.
Real-time Video Detection: The model can also detect and classify sign language gestures in real-time through video input.
Customizable Time Window: The application operates during a specific time period (e.g., 6 PM - 10 PM), ensuring the model runs only when needed.
Intuitive GUI: The user interface is built using Tkinter for ease of use, featuring simple controls for both image upload and live video feed detection.
Technologies Used:
Machine Learning: The model is trained using a neural network-based approach to classify known sign language words.
OpenCV: Used for video capture and real-time processing of gestures.
Tkinter: Provides the GUI, allowing users to interact with the model through image uploads or live video detection.
PIL: Handles image loading and processing.
.h5 Model: Pre-trained model loaded for predictions.
How to Use:
Install Dependencies: Ensure all required libraries such as OpenCV, Tkinter, and PIL are installed.
Run the Application: Launch the GUI to either upload an image or use real-time video to detect gestures.
Time-based Operation: The application is restricted to run between 6 PM and 10 PM, aligning with the defined schedule.
View Results: The detected words will be displayed on the screen, with real-time feedback during video capture.
