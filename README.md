# PC Remote

Pass keyboard shortcuts to your PC via a Telegram bot.

This is intended for use with Netflix on a browser being the active window. It also works just fine for VLC (other than the Skip intro button).

## How to run

1. You must have Python 3 installed. This bot is written in Python 3.7.

2. Libraries needed are specified in **requirements.txt**: `pip install -r requirements.txt`

3. Create a bot using [BotFather](http://t.me/BotFather). Commands list and short descriptions (for use when setting up the bot) is given [here](docs/commands.txt).

4. Create a file named **secrets.py** and populate the values specified using [the template provided](secrets.py.template).

4. Run **bot.py**: `python bot.py`