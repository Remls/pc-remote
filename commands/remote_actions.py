from pynput.keyboard import Key, Controller
from pynput.mouse import Controller as MouseController
import time
import config


def press_key(key):
    def perform():
        keyboard = Controller()
        keyboard.press(key)
        keyboard.release(key)
    return perform

def mouse_twitch():
    mouse = MouseController()
    mouse.position = (100, 100)
    time.sleep(0.5)
    mouse.move(100, 100)

def vlc_change_speed(speed):
    def perform():
        # Reset speed to x1.0
        press_key('=')()
        # Get no. of increments of +0.1
        incr = round((float(speed) - 1) / 0.1)
        for i in range(incr):
            press_key(']')()
    return perform

def vlc_increment_speed():
    press_key(']')()

def vlc_decrement_speed():
    press_key('[')()

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
    "sil": { "label": "Silent mode", "action": toggle_silent_mode, "reply": "" },
    "spd": { "label": "🏃‍-", "action": vlc_decrement_speed, "reply": "Decrementing playback speed by 0.1 ..." },
    "sp1": { "label": "x1", "action": vlc_change_speed(1), "reply": "Setting playback speed to x1 ..." },
    "sp1.5": { "label": "x1.5", "action": vlc_change_speed(1.5), "reply": "Setting playback speed to x1.5 ..." },
    "sp2": { "label": "x2", "action": vlc_change_speed(2), "reply": "Setting playback speed to x2 ..." },
    "sp3": { "label": "x3", "action": vlc_change_speed(3), "reply": "Setting playback speed to x3 ..." },
    "sp4": { "label": "x4", "action": vlc_change_speed(4), "reply": "Setting playback speed to x4 ..." },
    "spu": { "label": "🏃‍+", "action": vlc_increment_speed, "reply": "Incrementing playback speed by 0.1 ..." }
}

KEYBOARD_LAYOUT = [[get_label(button) for button in row] for row in [
    ["f", "f_off"],
    ["rw", "p", "ff"],
    ["vd", "m", "vu"],
    ["np", "s"],
    ["spd", "sp1", "sp1.5", "sp2", "sp3", "sp4", "spu"],
    ["sil"]
]]