# MIDI Note Recognition 🎹  

A lightweight Python tool for **real-time MIDI input reading on Windows**.  
It listens to your connected MIDI keyboard and prints out the **note name, velocity, and how long each key was held** directly in the terminal.  

Perfect for learning how MIDI works, debugging keyboards, or as a base for music-related projects.  

---

## ✨ Features
- Lists all available MIDI input devices  
- Prints **Note On/Off** events, note name, velocity, and duration  
- Uses `pygame.midi` (simple, no compiler headaches on Windows)  
- Runs instantly — no extra setup needed  

---

## 📦 Installation

Clone this repository and install the only dependency:

```bash
git clone https://github.com/zakariakubica/midi-note-recognition.git
cd midi-note-recognition
pip install pygame
