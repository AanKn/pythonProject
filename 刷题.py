import pyautogui
from time import sleep
import re
import pyperclip
import threading
from pynput.keyboard import Key, Listener
counts = 0


def do_python():
    global counts
    counts = int(pyautogui.prompt('请输入题目数：'))
    if not counts:
        exit()
    location1 = pyautogui.locateCenterOnScreen('img1.png', confidence=0.9)
    location2 = pyautogui.locateCenterOnScreen('img2.png', confidence=0.9)
    location3 = pyautogui.locateCenterOnScreen('img3.png', confidence=0.9)
    location4 = pyautogui.locateCenterOnScreen('img4.png', confidence=0.9)
    # location5 = pyautogui.Point(x=1796, y=181)如果电脑分辨率是1920，1080，可以用下面的
    # location1, location2 = pyautogui.Point(x=1368, y=251), pyautogui.Point(x=1094, y=250)
    # location3, location4 = pyautogui.Point(x=1789, y=257), pyautogui.Point(x=925, y=256)
    while counts > 0:
        pyautogui.click(location1.x, location1.y)
        sleep(0.5)
        pyautogui.click(location3.x+7, location3.y-76)  # 这个目的是关闭评判结果弹窗，关闭不了的话，数值可以改改
        sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.5)
        pyautogui.click(location2.x, location2.y)
        pyautogui.click(location2.x, location2.y + 50)
        raw_answer = pyperclip.paste()
        a = re.compile(r'(?<=(仅限平台内使用，\s\n)).[\s\S]*?(?=累计已接收)')
        try:
            answer = a.search(raw_answer).group()
        except AttributeError:
            pyautogui.click(location4.x, location4.y)
            continue
        else:
            pyperclip.copy(answer)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'v')
            # sleep(1)
            pyautogui.click(location3.x, location3.y)
            pyautogui.click(location4.x, location4.y)
            sleep(0.5)
            counts -= 1


def on_release(key):
    if key == Key.esc:
        global counts
        counts = 0


def start_listen():
    with Listener(on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    t1 = threading.Thread(target=do_python)
    t1.start()
    start_listen()
