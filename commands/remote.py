from telegram import ReplyKeyboardMarkup
from secrets import USERS
import config
from commands.remote_actions import KEYBOARD_LAYOUT, get_action_from_label, toggling_silent_mode
import logging

logger = logging.getLogger(__name__)


def send_remote(bot, update):
    sender = update.effective_user.id
    if sender in USERS.values():
        update.message.reply_text(
            text = "Sent remote.",
            reply_markup = ReplyKeyboardMarkup(KEYBOARD_LAYOUT),
            quote = False
        )


def answer_remote(bot, update):
    sender = update.effective_user.id
    if sender in USERS.values():
        input_text = update.message.text
        input_action = get_action_from_label(input_text)
        if (input_action):
            # Perform action by calling the function
            input_action["action"]()
            logger.info("{} pressed".format(input_text))
            if toggling_silent_mode(input_text):
                update.message.reply_text(
                    text = "Silent mode {}.".format("activated" if config.SILENT_MODE else "deactivated"),
                    quote = False
                )
            elif not config.SILENT_MODE:
                # Send reply only if not in silent mode
                update.message.reply_text(
                    text = input_action["reply"],
                    quote = False
                )