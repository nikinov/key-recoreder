import time
from pynput.keyboard import Key, Listener

def inb():
    inb.t1
    inb.t2
    print("sleep({0})".format(inb.t2 - inb.t1))

if __name__ == __name__:
    inb.t1 = time.time()

def on_press(key):
    if on_press.bol == 0:
        key = str(key)
        key = key.replace("'", "")
        key = key.replace("Key.", "")
        inb.t2 = time.time()
        inb()
        print('PressKey({0})'.format(
            key))
        on_press.bol = 1
        on_press.st = time.time()


on_press.bol = 0
def on_release(key):
    start = time.time()
    key = str(key)
    key = key.replace("'","")
    key = key.replace("Key.","")
    print("sleep({0})".format(start - on_press.st))
    print('ReleaseKey({0})'.format(
        key))
    on_press.bol = 0
    if on_press.bol == 0:
        inb.t1 = time.time()

    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

