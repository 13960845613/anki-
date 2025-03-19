import pyautogui
import time
import os
import pyperclip

# 设置工作目录
os.chdir(r"C:\Users\Qfyun\Desktop\anki卡片制作\创建anki字段")

def parse_positions(filename):
    """解析坐标文件"""
    positions = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().replace('，', ',')  # 统一逗号格式
            if '位置1' in line:
                x = int(line.split('x=')[1].split(',')[0])
                y = int(line.split('y=')[1])
                positions['position1'] = (x, y)
            elif '位置2' in line:
                x = int(line.split('x=')[1].split(',')[0])
                y = int(line.split('y=')[1])
                positions['position2'] = (x, y)
            elif '位置3' in line:
                x = int(line.split('x=')[1].split(',')[0])
                y = int(line.split('y=')[1])
                positions['position3'] = (x, y)
    return positions

def parse_contents(filename):
    """解析内容文件"""
    contents = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip().replace('\ufeff', '')
            fields = clean_line.split('\t')
            contents.extend(fields)
    return [c for c in contents if c.strip()]  # 过滤空内容

def click_position(x, y):
    """点击指定坐标"""
    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()
    print(f"✅ 已点击 ({x}, {y})")
    time.sleep(0.5)

def type_content(content):
    """通过剪贴板输入内容"""
    # 清空输入框
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(0.2)
    
    # 切换至中文输入法（示例：按Shift切换）
    pyautogui.press('shift')
    time.sleep(0.5)
    
    # 使用剪贴板粘贴
    pyperclip.copy(content)
    pyautogui.hotkey('ctrl', 'v')
    print(f"📝 已输入内容: {content}")
    time.sleep(0.2)

def execute_workflow(positions, contents):
    """执行自动化流程"""
    try:
        for idx, content in enumerate(contents, 1):
            print(f"\n====== 处理第 {idx}/{len(contents)} 条 ======")
            click_position(*positions['position1'])
            click_position(*positions['position2'])
            type_content(content)
            click_position(*positions['position3'])
            print(f"✔️ 完成 {idx}/{len(contents)}")
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    # 读取配置
    positions = parse_positions("位置.txt")
    contents = parse_contents("水平排列_无词性.txt")
    
    # 启动准备
    print("=== 系统检查 ===")
    print(f"定位到坐标数: {len(positions)}")
    print(f"待处理内容数: {len(contents)}")
    input("按 Enter 开始执行（5秒后启动，请聚焦目标窗口）...")
    time.sleep(5)
    
    # 执行主流程
    execute_workflow(positions, contents)
    print("\n🎉 所有内容处理完成！")