
from pypresence import Presence
import time
import config

SETTINGS = config.get_config()

client_id = SETTINGS['application_id']

RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop

def update_activity(details,state):
    if state == "":
        state = None
    RPC.update(details=details, state=state, start=time.time())  # Set the presence