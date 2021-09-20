# MiSTerRPI
Application to integrate MiSTer and Discord for Rich Presence

This app requires at least python 3+.

To install the python requirements run "pip install -r requirements.txt" in the root of this folder.
If you get an error about upgrading pip, run " -m pip install --upgrade pip"

You can find a compiled windows version built via pyinstaller in the releases section.



**You must enable the recents setting in your .ini file on the MiSTer** : recents=1              ; set to 1 to show recently played games

**Install the discord desktop application**

**Setup an appication in Discord that will be used for this integration**

* Navigate to https://discordapp.com/developers/
* Click “Create an Application.”
* Setup the application how you want, name in MiSTer , and give it a good image.
* Right under the name of your application, locate your Client ID. You will need this later.
* Lastly, save your application.


Update **config.json** with your details:

* mister_ip - ip address or hostname of MiSTer.
* mister_username - ssh username for MiSTer.
* mister_password - ssh password for MiSTer.
* debug - enable/disable debug logs.
* refresh_rate - polling rate of checking the core and game.
* core_storage - where the cores are stored fat for sd card and usbX for usb.
* applicationid - the client id for the app in Discord.
* state_text - the text that wil be displayed for the game. You can make this string whatever you want. {game} will be replaced with the game name.
* details_text - the text that will be displayed for the core. You canmake this whatever you want. {displayname} will be replaced with the displayname in the config for the core or {core} will replace the core name.

**The following will be used if the cores.json ones are either empty or not there**
* large_image - The large image that will be displayed. Must be added to the art assets in Discord. If the image is not uploaded to Discord, it will not be displayed.
* large_text -  The hover text for the large image.
* small_image - The small image that will be displayed. Must be added to the art assets in Discord. If the image is not uploaded to Discord, it will not be displayed.
* small_text - The hover text for the small image.
* buttons - an array of up to 2 buttons. Each button is a json object with 2 values, label and url. The buttons will show at the bottom of the info section.

```json
{
        "mister_ip": "MiSTer",
        "mister_username": "root",
        "mister_password": "1",
        "debug":false,
        "refresh_rate": "1",
        "core_storage": "fat",
        "applicationid":"000000000000000000",
        "state_text": "{game}",
        "details_text": "{displayname}",
        "small_text": "",
        "small_image": "",
        "large_text": "",
        "large_image": "misterkun",
        "buttons": [{"label": "MiSTerRPI Github", "url": "https://github.com/christopher-roelofs/misterrpi"}]
}
```

**cores.json**

* "GBA" - core name. This has to match the name of the rbf without the datestamp.The script removes the datestamp before it does the lookup.
* "description" - description of the core. Not required but added by default on first run.
* "display_name" - This allows you to set a better looking name for the core.
* large_image - The large image that will be displayed. Must be added to the art assets in Discord. If the image is not uploaded to Discord, it will not be displayed.
* large_text -  The hover text for the large image.
* small_image - The small image that will be displayed. Must be added to the art assets in Discord. If the image is not uploaded to Discord, it will not be displayed.
* small_text - The hover text for the small image.

```json
{
    "GBA": {   
        "description": "GBA Core",
        "display_name": "Nintendo Gameboy Advanced",
        "large_image": "",
        "large_text": "",
        "small_text": "",
        "small_image": ""
    }
}
```

