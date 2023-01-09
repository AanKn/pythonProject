import pygame
import sys
from pygame.locals import QUIT
import numpy as np
import easygui
import random


pygame.init()
screen_color = [248, 164, 83]  # 设置画布颜色,[238,154,73]对应为棕黄色
line_color = [0, 0, 0]  # 设置线条颜色，[0,0,0]对应黑色
over_pos = []  # 表示已经落子的位置
white_color = (255, 255, 255)  # 白棋颜色
black_color = (0, 0, 0)  # 黑棋颜色
red = (200, 30, 30)
blue = (30, 30, 200)
light = (170, 170, 170)
dark = (100, 100, 100)
font2 = pygame.font.SysFont('SimHei', 53)
font1 = pygame.font.SysFont('SimHei', 30)
font = pygame.font.SysFont('SimHei', 35)
text = font.render('退出游戏', True, line_color)
text1 = font.render('新的一局', True, line_color)
text2 = font.render('悔棋', True, line_color)
mp = np.zeros([15, 15], dtype=int)
a = []
patten = easygui.choicebox(msg='请选择对战方式', title='选择框 ', choices=('人人对战', '人机对战'))


def check_win(over_pos):  # 判断五子连心
    if len(over_pos) == 0:
        return [0, []]
    x = int((over_pos[-1][0][0]-27)/44)
    y = int((over_pos[-1][0][1]-27)/44)  # 标准位置转化成15内坐标
    if over_pos[-1][1] == white_color:
        mp[x][y] = 2  # 表示白子
    else:
        mp[x][y] = 1  # 表示黑子
    a.append([x, y])
    #  一列
    count = -1
    for i in mp:
        count += 1
        pos1 = []
        pos2 = []
        qizi = str(i).strip('[]').replace(' ', '')
        if '11111' in qizi:
            index = qizi.find('11111')
            pos1.append([count, index])
            pos1.append([count, index + 1])
            pos1.append([count, index + 2])
            pos1.append([count, index + 3])
            pos1.append([count, index + 4])
            return [1, pos1]
        elif '22222' in qizi:
            index = qizi.find('22222')
            pos2.append([count, index])
            pos2.append([count, index + 1])
            pos2.append([count, index + 2])
            pos2.append([count, index + 3])
            pos2.append([count, index + 4])
            return [1, pos1]
    # 一行
    for j in range(15):
        pos1 = []
        pos2 = []
        for i in range(15):
            if mp[i][j] == 1:
                pos1.append([i, j])
            else:
                pos1 = []
            if mp[i][j] == 2:
                pos2.append([i, j])
            else:
                pos2 = []
            if len(pos1) >= 5:
                return [1, pos1]
            if len(pos2) >= 5:
                return [2, pos2]
    # 左上到右下
    for i in range(15):
        for j in range(15):
            pos1 = []
            pos2 = []
            for k in range(15):
                if i+k >= 15 or j+k >= 15:
                    break
                if mp[i+k][j+k] == 1:
                    pos1.append([i+k, j+k])
                else:
                    pos1 = []
                if mp[i+k][j+k] == 2:
                    pos2.append([i+k, j+k])
                else:
                    pos2 = []
                if len(pos1) >= 5:
                    return [1, pos1]
                if len(pos2) >= 5:
                    return [2, pos2]
    # 右上到左下
    for i in range(15):
        for j in range(15):
            pos1 = []
            pos2 = []
            for k in range(15):
                if i+k >= 15 or j-k < 0:
                    break
                if mp[i+k][j-k] == 1:
                    pos1.append([i+k, j-k])
                else:
                    pos1 = []
                if mp[i+k][j-k] == 2:
                    pos2.append([i+k, j-k])
                else:
                    pos2 = []
                if len(pos1) >= 5:
                    return [1, pos1]
                if len(pos2) >= 5:
                    return [2, pos2]
    return [0, []]


def to_pos(x, y):  # 找到显示的可以落子的位置
        x1 = (x - 27) // 44  # 取商
        y1 = (y - 27) // 44
        if (x - 27) % 44 > 22:
            x1 += 1
        if (y - 27) % 44 > 22:
            y1 += 1
        return x1*44+27, y1*44+27


def check_downable(x, y, over_pos):  # 检查当前的位置是否已经落子
    for val in over_pos:
        if val[0][0] == x and val[0][1] == y:
            return False
    return True  # 表示没有落子


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))


def remake():
    over_pos.pop(-1)
    over_pos.pop(-1)
    x1, y1 = a.pop(-1)
    x2, y2 = a.pop(-1)
    mp[x1][y1] = 0
    mp[x2][y2] = 0


def ai():
    ai1, ai2 = random.randint(0, 14), random.randint(0, 14)
    return ai1 * 44 +27, ai2 * 44 +27


def run_game():
    screen = pygame.display.set_mode((670, 770))
    pygame.display.set_caption('五子棋')
    while True:
        for event in pygame.event.get():  # 获取事件，如果鼠标点击右上角关闭按钮，关闭
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 <= x <= 190 and 700 <= y <= 740:
                    pygame.quit()
                if 230 <= x <= 370 and 700 <= y <= 740:
                    global over_pos
                    over_pos = []
                    global mp
                    mp = np.zeros([15, 15], dtype=int)
                    run_game()
                if 410 <= x <= 480 and 700 <= y <= 840:
                    remake()

        screen.fill(screen_color)  # 清屏
        pygame.draw.line(screen, line_color, [27 - 4, 27 - 4], [670 - 27 + 4, 27 - 4], 4)
        pygame.draw.line(screen, line_color, [27 - 4, 27 - 4], [27 - 4, 670 - 27 + 4], 4)
        pygame.draw.line(screen, line_color, [670 - 27 + 4, 27 - 4], [670 - 27 + 4, 670 - 27 + 4], 4)
        pygame.draw.line(screen, line_color, [27 - 4, 670 - 27 + 4], [670 - 27 + 4, 670 - 27 + 4], 4)
        for i in range(27, 670, 44):
            pygame.draw.line(screen, line_color, [i, 27], [i, 670 - 27], 2)
            pygame.draw.line(screen, line_color, [27, i], [670 - 27, i], 2)
        # 在棋盘中心画个小圆表示正中心位置
        pygame.draw.circle(screen, line_color, [27 + 44 * 3, 27 + 44 * 3], 8, 0)
        pygame.draw.circle(screen, line_color, [27 + 44 * 7, 27 + 44 * 7], 8, 0)
        pygame.draw.circle(screen, line_color, [27 + 44 * 11, 27 + 44 * 3], 8, 0)
        pygame.draw.circle(screen, line_color, [27 + 44 * 3, 27 + 44 * 11], 8, 0)
        pygame.draw.circle(screen, line_color, [27 + 44 * 11, 27 + 44 * 11], 8, 0)
        for val in over_pos:  # 显示所有落下的棋子
            pygame.draw.circle(screen, val[1], val[0], 20, 0)  # (,颜色，位置，半径，实心）
        # 获取鼠标坐标信息
        x, y = pygame.mouse.get_pos()
        # x, y = to_pos(x, y)
        if 50 <= x <= 190 and 700 <= y <= 740:
            pygame.draw.rect(screen, light, [50, 700, 140, 40])
        else:
            pygame.draw.rect(screen, dark, [50, 700, 140, 40])
        if 230 <= x <= 370 and 700 <= y <= 740:
            pygame.draw.rect(screen, light, [230, 700, 140, 40])
        else:
            pygame.draw.rect(screen, dark, [230, 700, 140, 40])
        if 410 <= x <= 480 and 700 <= y <= 740:
            pygame.draw.rect(screen, light, [410, 700, 70, 40])
        else:
            pygame.draw.rect(screen, dark, [410, 700, 70, 40])
        screen.blit(text, (50, 700))
        screen.blit(text1, (230, 700))
        screen.blit(text2, (410, 700))
        if len(over_pos) % 2 == 0:
            print_text(screen, font1, 50, 650, '当前回合：黑子', blue)
        else:
            print_text(screen, font1, 50, 650, '当前回合：白子', blue)
        x, y = to_pos(x, y)
        if patten == "人人对战":
            keys_pressed = pygame.mouse.get_pressed()  # 获取鼠标按键信息
            if keys_pressed[0] and (20 < x < 670) and (20 < y < 670):
                if check_downable(x, y, over_pos):  # 判断是否可以落子，再落子
                    if len(over_pos) % 2 == 0:  # 黑子,因为黑子先下
                        over_pos.append([[x, y], black_color])
                    else:
                        over_pos.append([[x, y], white_color])
        elif patten == "人机对战":
            if len(over_pos) % 2 == 0:
                keys_pressed = pygame.mouse.get_pressed()  # 获取鼠标按键信息
                if keys_pressed[0] and (20 < x < 670) and (20 < y < 670):
                    if check_downable(x, y, over_pos):
                        over_pos.append([[x, y], black_color])
            elif len(over_pos) % 2 == 1:  # 用else的话，黑子赢不了
                x, y = ai()
                if check_downable(x, y, over_pos):
                    over_pos.append([[x, y], white_color])

                # 开始判断输赢
        res = check_win(over_pos)  # [[[x, y], black_color],[[x, y], white_color]],函数返回值[1,[黑子位置集合]]
        if res[0] == 1:
            a = list(map(lambda x: x * 44 + 27, [res[1][0][0], res[1][0][1]]))
            b = list(map(lambda x: x * 44 + 27, [res[1][4][0], res[1][4][1]]))
            pygame.draw.line(screen, [255, 0, 0], a, b, 2)
            print_text(screen, font2, 280, 650, '黑子获胜', red)
        if res[0] == 2:
            a = list(map(lambda x: x * 44 + 27, [res[1][0][0], res[1][0][1]]))
            b = list(map(lambda x: x * 44 + 27, [res[1][4][0], res[1][4][1]]))
            pygame.draw.line(screen, [255, 0, 0], a, b, 2)
            print_text(screen, font2, 280, 650, '白子获胜', red)
        pygame.display.update()


run_game()
