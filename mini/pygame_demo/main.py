from pathlib import Path

# 获取当前路径
current_path = Path(__file__).parent

import cv2
import time
import random
import tkinter as tk
from ffpyplayer.player import MediaPlayer

import pgzrun


# =============================================
#                   初始化
# 其中包括
# - 初始化参数
# - 定义函数
# ==============================================

# -------------------
# @初始化：初始化参数
# -------------------
pedal_label = ""

WIDTH = 500
HEIGHT = 700

s = 0
score = 0
ss = Actor("图片13")
dudu = Actor("图片15")

# direction表示踏板2当前运动的方向和速度, 初始值为3
direction = 3

# -------------------
# @初始化：定义函数
# -------------------
# @intro: play video
def play_video(file):
    cap = cv2.VideoCapture(file)
    player = MediaPlayer(file)
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        _, val = player.get_frame(show=False)
        if val == "eof":
            break

        cv2.imshow(file, frame)

        elapsed = (time.time() - start_time) * 1000  # msec
        play_time = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        sleep = max(1, int(play_time - elapsed))
        if cv2.waitKey(sleep) & 0xFF == ord("q"):
            break

    player.close_player()
    cap.release()
    cv2.destroyAllWindows()


# @intro: Q&A
def question(question_text="", options_text=None):

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title("答一答")

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry("500x300")  # 这里的乘是小x

    # 第4步，在图形界面上创建一个标签label用以显示并放置
    var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
    var.set(None)
    l = tk.Label(window, bg="yellow", width=50, text=question_text)
    l.pack()

    # 第6步，定义选项触发函数功能
    def print_selection():
        l.config(text="你的选择是 " + var.get() + "   正确答案是A，你答对了吗？")

    # 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
    r1 = tk.Radiobutton(
        window, text=options_text[0], variable=var, value="A", command=print_selection
    )
    r1.pack()
    r2 = tk.Radiobutton(
        window, text=options_text[1], variable=var, value="B", command=print_selection
    )
    r2.pack()
    r3 = tk.Radiobutton(
        window, text=options_text[2], variable=var, value="C", command=print_selection
    )
    r3.pack()

    # 第7步，主窗口循环显示
    window.mainloop()


# =============================================
#                 设置和运行游戏
# ==============================================
music.play("背景音乐")


bricks = []
for i in range(5):
    n = random.randint(1, 4)
    b = Actor("踏板" + str(n))
    min_x = b.width // 2
    max_x = WIDTH - b.width // 2
    b.x = random.randint(min_x, max_x)
    b.y = 140 * (i + 1)
    bricks.append(b)
    if i == 2:
        dudu.x = b.x
        dudu.bottom = b.top
        b.image = "踏板1"


def draw():
    ques = "今天你想听党史小故事吗?\n如果想的话，请点击左右键\n让我跳动起来。当我落在相\n应的故事积木上时，你就可\n以听到有趣的故事了！"
    dudu.draw()
    global score, s
    screen.blit("背景", [0, 0])
    if s == 0:
        ss.draw()
        screen.draw.text(ques, (40, 450), fontname="a.ttf", fontsize=30, color="orange")
    if s == 1:
        dudu.draw()
        for brick in bricks:
            brick.draw()


def update():
    global score, direction, s, pedal_label
    change = True
    if dudu.image == "图片15":
        score += 1
        on_brick = 0
        for b in bricks:
            b.y -= 3
            if b.image == "踏板2":
                b.x += direction
                if b.right >= WIDTH:
                    direction = -3
                elif b.left <= 0:
                    direction = 3
            if b.y < 0:
                n = random.randint(1, 4)
                b.image = "踏板" + str(n)
                b.y = HEIGHT
                min_x = b.width // 2
                max_x = WIDTH - b.width // 2
                b.x = random.randint(min_x, max_x)
        if s == 1:
            for b in bricks:
                if dudu.colliderect(b) and dudu.bottom < b.bottom:
                    dudu.bottom = b.top
                    on_brick = 1
                    # 当嘟嘟踩在踏板2上时,跟随踏板一起左右移动
                    if b.image == "踏板2":
                        dudu.x += direction
                    if b.image == "踏板3":
                        if pedal_label == "真理的味道有点甜":
                            change = False
                        pedal_label = "真理的味道有点甜"
                        while True:
                            if not change:
                                break
                            play_video(str(current_path.joinpath("declaration.mp4")))
                            question(
                                question_text="陈望道翻译的马克思主义文献是《  》？",
                                options_text=["共产党宣言", "国际歌", "马克思选集"],
                            )
                            break
                    if b.image == "踏板4":
                        if pedal_label == "七子之歌":
                            change = False
                        pedal_label = "七子之歌"
                        while True:
                            if not change:
                                break
                            play_video(
                                str(current_path.joinpath("song of seven sons.mp4"))
                            )
                            question(
                                question_text="七子之歌的作者是？",
                                options_text=["闻一多", "毛泽东", "陈独秀"],
                            )
                            break

            if on_brick == 0:
                if dudu.y < 600:
                    dudu.y += 4
        if keyboard.left:
            s = 1
            if dudu.left > 0:
                dudu.x -= 5
        if keyboard.right:
            s = 1
            if dudu.right < WIDTH:
                dudu.x += 5


def on_key_down(key):
    if key == keys.SPACE and dudu.image == "嘟嘟哭":
        global score, bricks
        music.play("背景音乐")
        dudu.image = "图片15"
        bricks = []
        score = 0
        for i in range(5):
            n = random.randint(1, 4)
            b = Actor("踏板" + str(n))
            min_x = b.width // 2
            max_x = WIDTH - b.width // 2
            b.x = random.randint(min_x, max_x)
            b.y = 140 * (i + 1)
            bricks.append(b)
            if i == 2:
                b.image = "踏板1"
                dudu.x = b.x
                dudu.bottom = b.top


pgzrun.go()
