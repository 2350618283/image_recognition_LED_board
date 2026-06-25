from ultralytics import YOLO

# 1. 加载预训练模型
model = YOLO('yolo11s-obb.pt')  # 首次运行会自动下载权重

# 2. 对单张图片进行推理
results = model('original\inference\8e8bc314f22ceef19788fa9ee4a2ff6.jpg')

# 3. 查看结果
for r in results:
    # 打印检测到的旋转框信息
    print(r.obb.xyxyxyxy) # 输出四个角点坐标
    print(r.obb.conf)     # 输出置信度
    print(r.obb.cls)      # 输出类别ID

#命令打框 yolo predict model=yolo11s-obb.pt source='original\inference\8e8bc314f22ceef19788fa9ee4a2ff6.jpg'