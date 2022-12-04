#答案解析坐标 1369，253
#编写代码1120 250
#代码位置1184 447
#提交代码Point(x=1784, y=260)
#下一题919 261
# 复制起始位置1056 331
#复制结束位置1884 1014
import pyautogui
import time
count = 1
while count>0:
    pyautogui.moveTo(1369,253,0.1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1056,331,0.1)
    pyautogui.dragTo(1845, 1053, 2, button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.moveTo(1120,250,0.1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1056,331,0.1)
    pyautogui.dragTo(1845,1053, 2, button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.moveTo(1784, 260,0.1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(919,261,0.1)
    pyautogui.click()
    time.sleep(2)
    count-=1


