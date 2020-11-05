from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController
import time
import config


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

def toggling_silent_mode(current_action_label):
    return current_action_label == ACTIONS_LIST["sil"]["label"]

def get_label(action_key):
    return ACTIONS_LIST[action_key]["label"]

def get_action_from_label(label):
    for action in ACTIONS_LIST:
        if ACTIONS_LIST[action]["label"] == label:
            return ACTIONS_LIST[action]
    return None

ACTIONS_LIST = {
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

KEYBOARD_LAYOUT = [[get_label(button) for button in row] for row in [
    ["f", "f_off"],
    ["rw", "p", "ff"],
    ["vd", "m", "vu"],
    ["np", "s"],
    ["sil"]
]]