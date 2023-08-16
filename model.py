import numpy as np
import tensorflow as tf
from tensorflow import keras
import psutil
import tkinter as tk
from tkinter import Label, Button

# Define a function to get system data and make predictions
def get_system_data():
    system_cpu = psutil.cpu_percent(interval=1)
    system_ram = psutil.virtual_memory().percent
    
    system_data_label.config(text=f"System CPU Usage: {system_cpu:.2f}%\nSystem RAM Usage: {system_ram:.2f}%")
    
    new_data = np.array([[system_cpu, system_ram]])
    predictions = model.predict(new_data)
    status = "High CPU Usage" if predictions > 0.5 else "Normal"
    predicted_status_label.config(text=f"Predicted Status: {status}")

# Create the main window
root = tk.Tk()
root.title("System Monitoring Bot")

# Generate synthetic data for demonstration
data_size = 1000
input_memory = data_size
np.random.seed(42)
cpu_usage = np.random.uniform(0, 100, size=data_size)
ram_usage = np.random.uniform(0, 100, size=data_size)
labels = (cpu_usage > 80).astype(int)  # Simulate high CPU usage

# Split data
split_ratio = 0.8
split_index = int(data_size * split_ratio)
train_cpu = cpu_usage[:split_index]
train_ram = ram_usage[:split_index]
train_labels = labels[:split_index]
test_cpu = cpu_usage[split_index:]
test_ram = ram_usage[split_index:]
test_labels = labels[split_index:]

# TensorFlow model
model = keras.Sequential([
    keras.layers.Input(shape=(2,)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x=np.column_stack((train_cpu, train_ram)), y=train_labels, epochs=10, batch_size=32)

# Create GUI components
system_data_label = Label(root, text="", font=("Helvetica", 12))
predicted_status_label = Label(root, text="", font=("Helvetica", 12))
get_data_button = Button(root, text="Get System Data", command=get_system_data)

# Place GUI components on the window
system_data_label.pack(pady=10)
predicted_status_label.pack(pady=10)
get_data_button.pack()

# Start the GUI event loop
root.mainloop()
