# simple midi reader (windows tested)
# uses pygame (pip install pygame)

import time
import pygame.midi as pm

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
pressed = {}  # active notes

def note_name(n):
    # basic mapping
    return NOTE_NAMES[n % 12] + str((n // 12) - 1)  # C4 = 60

def list_devices():
    count = pm.get_count()
    if count <= 0:
        print("No midi devices found")
        return
    print("Devices:")
    for i in range(count):
        interf, name, is_in, is_out, opened = pm.get_device_info(i)
        try:
            interf = interf.decode()
        except: pass
        try:
            name = name.decode()
        except: pass
        print(f"  {i}: IN={is_in} OUT={is_out}  {interf} :: {name}")

def pick_input():
    # choose input device
    count = pm.get_count()
    if count <= 0:
        raise RuntimeError("no midi input devices available")

    # find first input
    first_input = None
    for i in range(count):
        info = pm.get_device_info(i)
        is_input = info[2]
        if is_input == 1:
            first_input = i
            break

    # ask user
    choice = input("enter midi INPUT device index (or 'list'): ").strip()

    if choice.lower() == "list":
        list_devices()
        choice = input("enter midi INPUT device index: ").strip()

    if choice == "":
        if first_input is None:
            raise RuntimeError("no midi input devices available")
        print(f"(using first input index: {first_input})")
        return first_input

    # fallback
    try:
        return int(choice)
    except ValueError:
        print("not a number, using first input")
        if first_input is None:
            raise RuntimeError("no midi input devices available")
        return first_input

def parse(status, d1, d2):
    # returns ('on' or 'off', note, velocity) or (None, None, None)
    s = status & 0xF0
    if s == 0x90:  # note on (vel 0 = off)
        if d2 > 0:
            return ("on", d1, d2)
        else:
            return ("off", d1, 0)
    elif s == 0x80:  # note off
        return ("off", d1, d2)
    return (None, None, None)

def main():
    pm.init()
    try:
        list_devices()
        idx = pick_input()
        print(f"opening input {idx} ...")
        inp = pm.Input(idx)
        print("ready. Ctrl+C to stop.\n")

        while True:
            if not inp.poll():
                time.sleep(0.001)
                continue

            events = inp.read(16)  # (data, timestamp) pairs
            for data, _ts in events:
                st, d1, d2, _d3 = data
                ev, note, vel = parse(st, d1, d2)
                if ev is None:
                    continue

                name = note_name(note)

                if ev == "on":
                    if note not in pressed:
                        pressed[note] = time.time()
                    print(f"ON  {name} {note} vel={vel}")
                elif ev == "off":
                    start = pressed.pop(note, None)
                    held = None
                    if start is not None:
                        held = time.time() - start
                    if held is not None:
                        # round to 2 dp (good enough)
                        print(f"OFF {name} {note} vel={vel} held {held:.2f}s")
                    else:
                        print(f"OFF {name} {note} vel={vel}")  # no start? just print it

    except KeyboardInterrupt:
        print("\nbye.")
    finally:
        try:
            inp.close()
        except:
            pass
        pm.quit()

if __name__ == "__main__":
    main()

