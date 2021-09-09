import paramiko
from time import sleep
import json
import config
import ssh
import mister
import cores
import logger
import discord

SETTINGS = config.get_config()
maps = cores.read_file_map()


RECENTS_FOLDER = '/media/{}/config/'.format(SETTINGS['core_storage'])


last_game = None
last_core = None


def replace_text(core, game, displayname, text):
    return text.replace("{core}", core).replace("{game}", game).replace("{displayname}", displayname)


while True:
    try:
        core = mister.get_running_core()
        map_core = cores.get_map(core)
        game = mister.get_last_game(core)

        displayname = core
        state_text = SETTINGS['state_text']
        details_text = SETTINGS['details_text']
        small_text = SETTINGS['small_text']
        small_image = SETTINGS['small_image']
        large_image = SETTINGS['large_image']
        large_text = SETTINGS['large_text']

        if "state_text" in map_core:
            state_text = map_core["details_text"]

        if "details_text" in map_core:
            details_text = map_core["details_text"]

        if "display_name" in map_core:
            displayname = map_core["display_name"]

        if "small_text" in map_core:
            if map_core["small_text"] != "":
                small_text = map_core["small_text"]
        
        if "small_image" in map_core:
            if map_core["small_image"] != "":
                small_image = map_core["small_image"]

        if "large_text" in map_core:
            if map_core["large_text"] != "":
                large_text = map_core["large_text"]

        if "large_image" in map_core:
            if map_core["large_image"] != "":
                large_image = map_core["large_image"]

        state_text = replace_text(core,game,displayname,state_text)
        details_text = replace_text(core,game,displayname,details_text)

        if game != "" and game != last_game:
            discord.update_activity(details_text,state_text,large_image,large_text,small_image,small_text)
                        
        if core != last_core:
            discord.update_activity(details_text,state_text,large_image,large_text,small_image,small_text)

        last_core = core
        last_game = game

    except Exception as e:
        logger.error(repr(e))
    sleep(int(SETTINGS["refresh_rate"]))

client.close()
