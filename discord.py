
from pypresence import Presence
import time
import config

SETTINGS = config.get_config()

client_id = SETTINGS['application_id']

RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop

def update_activity(details,state,large_image=None,large_text=None,small_image=None,small_text=None):
    if state == "":
        state = None
    if large_image == "":
        large_image = None
    if large_text == "":
        large_text = None
    if small_image == "":
        small_image = None
    if small_text == "":
        small_text = None
    RPC.update(details=details, state=state, start=time.time(),large_image=large_image,large_text=large_text,small_image=small_image,small_text=small_text)  # Set the presence


if __name__ == "__main__":
    while True:
        update_activity("Console","Game","segacd",None,None,None)
        time.sleep(100000)