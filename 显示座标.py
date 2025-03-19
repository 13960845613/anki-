import pyautogui
import time

def display_mouse_coordinates():
    try:
        print("按 Ctrl+C 退出程序")
        while True:
            # 获取鼠标当前位置
            x, y = pyautogui.position()
            # 获取屏幕分辨率
            screen_width, screen_height = pyautogui.size()
            # 格式化输出坐标和屏幕分辨率
            print(f"鼠标坐标: X={x}, Y={y} | 屏幕分辨率: {screen_width}x{screen_height}", end="\r")
            # 刷新频率（0.1秒）
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n程序已退出")

if __name__ == "__main__":
    display_mouse_coordinates()