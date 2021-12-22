import keyboard

def start():
    keyboard.send('ctrl+shift+esc')

keyboard.add_hotkey("f5", start)

keyboard.wait()