import pydirectinput
import time
import pyautogui
import pyperclip
import tkinter as tk
import threading
from plyer import notification

def hold_key(key, duration):
    pydirectinput.keyDown(key)
    time.sleep(duration)
    pydirectinput.keyUp(key)

def mainspam(text, many):
    time.sleep(2)  # 切り替え猶予
    notify_start()
    for i in range(many):
        pyautogui.moveTo(1004, 1349)
        pydirectinput.click()
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        hold_key('enter', 0.1)

def start():
    try:
        text = entry_text.get()
        many = int(entry_count.get())
    except:
        print("入力エラー")
        return

    # スレッドで実行（GUIフリーズ防止）
    threading.Thread(target=mainspam, args=(text, many), daemon=True).start()

def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")
def notify_start():
    notification.notify(
        title="Spathe",
        message="スパムを開始しました",
        timeout=2
    )

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.lift()
root.focus_force()
root.geometry("300x350")
root.configure(bg="#222327")

frame = tk.Frame(root, bg="#222327")
frame.pack(expand=True)
font=("Consolas", 10)


root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

label = tk.Label(root, text="Spathe", font=("Arial", 20), bg="#222327", fg="#FFFFFF")
label.pack(pady=10)

label1 = tk.Label(root, text="spam text\n(spam text)", fg="red", bg="#222327")
label1.pack()

entry_text = tk.Entry(root, bg="#333", fg="white", insertbackground="white")
entry_text.pack(pady=5)

label2 = tk.Label(root, text="spam time\n(spam time)", fg="red", bg="#222327")
label2.pack()

entry_count = tk.Entry(root, bg="#333", fg="white", insertbackground="white")
entry_count.pack(pady=5)

start_btn = tk.Button(
    frame,
    text="Start",
    command=start,
    bg="#550000",
    fg="red",
    activebackground="#770000",
    relief="flat",
    borderwidth=0
)
start_btn.pack(pady=15, ipadx=10, ipady=5)

exit_btn = tk.Button(
    frame,
    text="Exit",
    command=root.destroy,
    bg="#333",
    fg="white",
    relief="flat"
)
exit_btn.pack(pady=5)

root.mainloop()
