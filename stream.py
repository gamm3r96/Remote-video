import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Video Streamer by Gamm3r96")  # Include your name

# Create input fields for IP, port, and interface
ip_label = tk.Label(root, text="IP Address:")
ip_label.pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

port_label = tk.Label(root, text="Port:")
port_label.pack()
port_entry = tk.Entry(root)
port_entry.pack()

interface_label = tk.Label(root, text="Interface:")
interface_label.pack()
interface_entry = tk.Entry(root)
interface_entry.pack()

# Create a canvas for displaying the video stream
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Function to start streaming
def start_stream():
    ip = ip_entry.get()
    port = int(port_entry.get())
    interface = interface_entry.get()
    
    # Create a video capture object
    cap = cv2.VideoCapture(f'udp://{ip}:{port}?localaddr={interface}')
    
    # Continuously capture and display frames
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Convert the frame to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame_rgb))
        
        # Update the canvas with the new frame
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.photo = photo  # Keep a reference to prevent garbage collection
    
    # Release the video capture object when done
    cap.release()

# Create a button to start streaming
start_button = tk.Button(root, text="Start Streaming", command=start_stream)
start_button.pack()

# Start the main loop
root.mainloop()
