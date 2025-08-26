# MIDI Note Recognition

Python program for real-time MIDI input and output.  
Connect a MIDI keyboard and see the note, velocity, and duration printed in the terminal.

---

## Features
- Lists available MIDI input devices
- Displays note on/off with velocity and hold time
- Built using `pygame.midi` for simple Windows support

---

## Installation
```bash
git clone https://github.com/zakariakubica/midi-note-recognition.git
cd midi-note-recognition
pip install pygame
```

---

## Usage
```bash
python MNR 1.py
```

You will be prompted to select a MIDI input device.  
Press Enter to use the first one automatically.

---

## Example Output (highlighted)
```bash
devices:
  0: IN=0 OUT=1  MMSystem :: Microsoft MIDI Mapper
  1: IN=1 OUT=0  MMSystem :: MPK mini 3
  2: IN=0 OUT=1  MMSystem :: Microsoft GS Wavetable Synth
  3: IN=0 OUT=1  MMSystem :: MPK mini 3
enter midi INPUT device index (or 'list'):
(using first input index: 1)
opening input 1 ...
ready. Ctrl+C to stop.

ON  C4 60 vel=100
OFF C4 60 vel=0 held 0.42s
ON  F#3 54 vel=96
OFF F#3 54 vel=0 held 0.18s
```

---

## Example Output (plain, unbashed)
```
devices:
  0: IN=0 OUT=1  MMSystem :: Microsoft MIDI Mapper
  1: IN=1 OUT=0  MMSystem :: MPK mini 3
  2: IN=0 OUT=1  MMSystem :: Microsoft GS Wavetable Synth
  3: IN=0 OUT=1  MMSystem :: MPK mini 3

ON  C4 60 vel=100
OFF C4 60 vel=0 held 0.42s
```

---

## Roadmap
- Export note events to CSV with timestamps
- Add command-line flag for auto-selecting a device
- Optional audio playback of notes
- Cross-platform testing (macOS/Linux)

---

## License
MIT License © 2025 Zakaria Kubica
