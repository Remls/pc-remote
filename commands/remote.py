from telegram import ReplyKeyboardMarkup
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController
from secrets import USERS
import config
import random, logging, time

logger = logging.getLogger(__name__)


def press_key(key):
    def press():
        keyboard = Controller()
        keyboard.press(key)
        keyboard.release(key)
    return press

def mouse_twitch():
    mouse = MouseController()
    mouse.position = (100, 100)
    time.sleep(0.5)
    mouse.move(100, 100)

def toggle_silent_mode():
    config.SILENT_MODE = not config.SILENT_MODE

REMOTE_ACTIONS = {
    "f": { "label": "💻 Fullscreen", "action": press_key('f'), "reply": "Fullscreen" },
    "f_off": { "label": "💻 Fullscreen off", "action": press_key(Key.esc), "reply": "Fullscreen off" },
    "rw": { "label": "⏪", "action": press_key(Key.left), "reply": "Rewinding by 10s ..." },
    "p": { "label": "⏯", "action": press_key(Key.space), "reply": "Playing/pausing ..." },
    "ff": { "label": "⏩", "action": press_key(Key.right), "reply": "Fast-forwarding by 10s .." },
    "vd": { "label": "🔈-", "action": press_key(Key.down), "reply": "Decreasing volume ..." },
    "m": { "label": "🔈🚫", "action": press_key('m'), "reply": "Toggling mute ..." },
    "vu": { "label": "🔈+", "action": press_key(Key.up), "reply": "Increasing volume ..." },
    "np": { "label": "🖱 Now playing", "action": mouse_twitch, "reply": "🖱" },
    "s": { "label": "⏭ Skip intro", "action": press_key('s'), "reply": "Skipping intro ..." },
    "sil": { "label": "Silent mode", "action": toggle_silent_mode, "reply": "" }
}

def get_label(action_key):
    return REMOTE_ACTIONS[action_key]["label"]

def get_action_from_label(label):
    for action in REMOTE_ACTIONS:
        if REMOTE_ACTIONS[action]["label"] == label:
            return REMOTE_ACTIONS[action]
    return None


def send_remote(bot, update):
    sender = update.effective_user.id
    if sender in USERS.values():
        keyboard = [
            ["f", "f_off"],
            ["rw", "p", "ff"],
            ["vd", "m", "vu"],
            ["np", "s"],
            ["sil"]
        ]
        keyboard = [[get_label(button) for button in row] for row in keyboard]
        update.message.reply_text(
            text = "Sent remote.",
            reply_markup = ReplyKeyboardMarkup(keyboard),
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
            if input_text == REMOTE_ACTIONS["sil"]["label"]:
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