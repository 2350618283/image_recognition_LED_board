import os
import random
import shutil

# ===== 配置路径 =====
source_images = "./images_board"      # 你所有图片所在的文件夹
source_labels = "./labels_txt"      # 你所有标签所在的文件夹
train_ratio = 0.8             # 训练集比例

# 目标文件夹（YOLO标准结构）
os.makedirs("datasets/images/train", exist_ok=True)
os.makedirs("datasets/images/val", exist_ok=True)
os.makedirs("datasets/labels/train", exist_ok=True)
os.makedirs("datasets/labels/val", exist_ok=True)

# 获取所有图片文件名（不含后缀）
all_files = [f.replace('.jpg', '') for f in os.listdir(source_images) if f.endswith('.jpg')]
random.shuffle(all_files)

split_idx = int(len(all_files) * train_ratio)
train_files = all_files[:split_idx]
val_files = all_files[split_idx:]

print(f"总图片数: {len(all_files)}，训练集: {len(train_files)}，验证集: {len(val_files)}")

# 移动训练集
for name in train_files:
    shutil.copy(os.path.join(source_images, f"{name}.jpg"), f"datasets/images/train/{name}.jpg")
    shutil.copy(os.path.join(source_labels, f"{name}.txt"), f"datasets/labels/train/{name}.txt")

# 移动验证集
for name in val_files:
    shutil.copy(os.path.join(source_images, f"{name}.jpg"), f"datasets/images/val/{name}.jpg")
    shutil.copy(os.path.join(source_labels, f"{name}.txt"), f"datasets/labels/val/{name}.txt")

print("数据集划分完成！")