import matplotlib
matplotlib.rcParams.update(matplotlib.rcParamsDefault)  # 恢复默认设置
from ultralytics import YOLO

# 加载一个YOLO11 OBB的配置文件
# model = YOLO('yolo11s-obb.yaml')  # 从头构建模型
# 或者加载预训练权重开始微调（推荐）
model = YOLO('yolo11s-obb.pt')

# 开始训练
results = model.train(
    data='my_ad_datasets/data.yaml',  # 你的数据集配置
    epochs=100,                # 训练轮数
    imgsz=640,                 # 输入图片尺寸
    batch=16,                  # 批次大小
    device='cpu',                  # 使用GPU，CPU则设为 'cpu'
    project='runs/train',      # 结果保存路径
    name='ad_detection_board'        # 本次实验名称
)


# 在终端中，确保当前目录在 my_ad_dataset 的上一级，然后运行：
#

# yolo train model=yolo11s-obb.pt data=my_ad_dataset/data.yaml epochs=100 imgsz=640