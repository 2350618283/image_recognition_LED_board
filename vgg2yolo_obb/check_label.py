import cv2
import numpy as np
import os

# 配置
IMAGE_DIR = "images_board"    # 你的图片路径
LABEL_DIR = "labels_txt"   # 你的txt标签路径
OUTPUT_DIR = "check_results" # 输出可视化结果
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 遍历图片
for img_name in os.listdir(IMAGE_DIR):
    if not img_name.endswith('.jpg'):
        continue

    img_path = os.path.join(IMAGE_DIR, img_name)
    txt_name = os.path.splitext(img_name)[0] + '.txt'
    txt_path = os.path.join(LABEL_DIR, txt_name)

    if not os.path.exists(txt_path):
        continue

    # 读取图片
    img = cv2.imread(img_path)
    h, w = img.shape[:2]

    # 读取标签
    with open(txt_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) != 9:
            continue
        # class_id = int(parts[0])
        coords = list(map(float, parts[1:]))

        # 将归一化坐标转为像素坐标
        points = []
        for i in range(0, 8, 2):
            x = int(coords[i] * w)
            y = int(coords[i+1] * h)
            points.append([x, y])

        pts = np.array(points, dtype=np.int32)

        # 绘制多边形（黄色边框）
        cv2.polylines(img, [pts], isClosed=True, color=(0, 255, 255), thickness=3)
        # 绘制顶点（红色小圆点）
        for p in pts:
            cv2.circle(img, tuple(p), 5, (0, 0, 255), -1)

    # 保存结果
    out_path = os.path.join(OUTPUT_DIR, img_name)
    cv2.imwrite(out_path, img)
    print(f"已生成: {out_path}")

print("验证完成！请打开 check_results 文件夹查看。")