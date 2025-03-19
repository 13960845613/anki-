import csv

def generate_horizontal_data():
    """生成水平排列数据（忽略词性，按意思层级横向扩展）"""
    data = []
    headers = []
    row = []
    
    # 生成n=1到5的意思层级
    for n in range(1, 6):
        # 每个n对应6个意思（示例）
        for m in range(1, 7):
            # 添加意思和中英解释
            headers.extend([f"意思{n}.{m}", f"中英解释{n}.{m}"])
            row.extend([f"意思{n}.{m}", f"中英解释{n}.{m}"])
            
            # 每个意思生成6组词组和例句
            for g in range(1, 7):
                headers.extend([f"词组{n}.{m}.{g}", f"例句{n}.{m}.{g}"])
                row.extend([f"词组{n}.{m}.{g}", f"例句{n}.{m}.{g}"])
    
    data.append(headers)
    data.append(row)
    return data

def save_csv(data, filename="C:/Users/Qfyun/Desktop/anki卡片制作/试验品.csv"):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"文件已生成：{filename}")

if __name__ == "__main__":
    # 生成数据
    table_data = generate_horizontal_data()
    
    # 打印前20列示例
    print("表头示例:", table_data[0][:20])
    print("数据示例:", table_data[1][:20])
    
    # 保存文件
    save_csv(table_data)
