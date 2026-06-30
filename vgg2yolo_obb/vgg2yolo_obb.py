import json
import os
from PIL import Image

# ===== 配置 =====
JSON_PATH = "annotations_board.json"         # 你的VGG JSON文件名
IMAGE_DIR = "./images_board"                # 存放所有图片的文件夹
OUTPUT_LABEL_DIR = "./labels_txt"         # 输出的txt标签文件夹

# 类别映射（你的数据中只有一个类别"board"，索引为0）
CLASS_MAPPING = {"board": 0}

# ===== 创建输出目录 =====
os.makedirs(OUTPUT_LABEL_DIR, exist_ok=True)

# ===== 读取JSON =====
with open(JSON_PATH, 'r') as f:
    data = json.load(f)

# ===== 遍历每张图片 =====
for filename, info in data.items():
    if not filename.endswith(('.jpg', '.png', '.jpeg')):
        continue

    img_path = os.path.join(IMAGE_DIR, filename)
    if not os.path.exists(img_path):
        print(f"警告：图片 {img_path} 不存在，跳过")
        continue

    # 读取图片尺寸
    with Image.open(img_path) as img:
        img_w, img_h = img.size

    regions = info.get("regions", {})
    if not regions:
        print(f"注意：{filename} 没有标注，跳过")
        continue

    lines = []
    for region_id, region in regions.items():
        shape = region.get("shape_attributes", {})
        if shape.get("name") != "polygon":
            continue

        x_points = shape["all_points_x"]
        y_points = shape["all_points_y"]

        # ---------- 关键修改：处理闭合点 ----------
        # 如果首尾相同，去掉最后一个点（闭合点）
        if len(x_points) == len(y_points) and len(x_points) >= 2:
            if x_points[0] == x_points[-1] and y_points[0] == y_points[-1]:
                x_points = x_points[:-1]
                y_points = y_points[:-1]

        # 如果点数多于4，只取前4个（假设矩形）
        if len(x_points) != 4 or len(y_points) != 4:
            if len(x_points) >= 4 and len(y_points) >= 4:
                x_points = x_points[:4]
                y_points = y_points[:4]
                print(f"信息：{filename} 的 {region_id} 原为{len(x_points)+1}个点，取前4个")
            else:
                print(f"警告：{filename} 的 {region_id} 点数不足4，跳过")
                continue

        # 获取类别
        region_attrs = region.get("region_attributes", {})
        class_name = region_attrs.get("label", "board")
        class_id = CLASS_MAPPING.get(class_name, 0)

        # 归一化坐标
        norm_points = []
        for x, y in zip(x_points, y_points):
            norm_x = x / img_w
            norm_y = y / img_h
            norm_points.append(f"{min(max(norm_x, 0.0), 1.0):.6f}")
            norm_points.append(f"{min(max(norm_y, 0.0), 1.0):.6f}")

        line = f"{class_id} " + " ".join(norm_points)
        lines.append(line)

    if lines:
        txt_name = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(OUTPUT_LABEL_DIR, txt_name)
        with open(txt_path, 'w') as f:
            f.write("\n".join(lines))
        print(f"已生成 {txt_path}  (共{len(lines)}个目标)")
    else:
        print(f"警告：{filename} 没有有效标注，跳过")

print("转换完成！")