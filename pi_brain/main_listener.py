import serial
import subprocess
import os
import time
from gemini_vision import solve_math  

SECRET_CODE = ["4", "1", "6", "7"]
input_history = []
mode = "CALC" # Modes: CALC, MENU, GEMINI, PDF, GAME

# PICO CONNECTIVITY
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

def launch_game():
    print("Launching RetroPie...")
    # EmulationStation
    subprocess.run(["sudo", "systemctl", "start", "emulationstation"])

def open_pdf(filename):
    print(f"Opening {filename}...")
    subprocess.run(["python3", "pdf_viewer.py", filename])

def handle_key(key):
    global mode, input_history
    
    if mode == "CALC":
        input_history.append(key)
        if input_history[-4:] == SECRET_CODE:
            mode = "MENU"
            print("--- SECRET MENU UNLOCKED ---")
            # Logic to display menu on screen
        
    elif mode == "MENU":
        if key == "1": mode = "GEMINI"
        if key == "2": launch_game()
        if key == "3": open_pdf("textbook.pdf")
        if key == "AC": mode = "CALC" # Emergency hide functionality

while True:
    if ser.in_waiting > 0:
        key_pressed = ser.readline().decode('utf-8').strip()
        handle_key(key_pressed)
    time.sleep(0.01)