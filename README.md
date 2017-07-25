# kodi-telegram

A telegram bot for controlling Kodi Media Center

## Installation

```
git clone https://github.com/ritiek/kodi-telegram
cd kodi-telegram
pip install -r requirements.txt
```

- Edit [kodi_bot.py](kodi_bot.py) to whatever IP address or Port your Kodi webserver is running on.

- For security purposes, you should also note down your telegram `chat_id` and restrict access only to it by editing the script accordingly.

- Now you should be safe to run the script by `python kodi_telegram.py`.

## Available Commands

Send the following commands to the bot preceeding `/` before them (example: `/start`).

```
start - Start Kodi
stop - Exit Kodi
```

Anything that does not preceed with `/` will be sent as text to the webserver.

## License

`The MIT License`
