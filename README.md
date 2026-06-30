# image_recognition_LED_board
这是一个基于YOLO11s-obb的图像识别项目，主要用于商家门头牌匾主题检测识别


train_LED为本项目训练目录

├─my_ad_datasets                                         训练数据集

│  ├─images

│  │  ├─train

│  │  └─val

│  └─labels

│      ├─train

│      └─val

├─runs                                                   模型训练数据保存

│  └─obb

│      └─runs

│          └─train

│              ├─ad_detection_board

│              │  └─weights

│              ├─ad_detection_board-2

│              │  └─weights
│              ├─ad_detection_board-3

│              │  └─weights

│              ├─ad_detection_board-4

│              │  └─weights

│              ├─ad_detection_board-5

│              │  └─weights

│              ├─ad_detection_board-6

│              │  └─weights
│              ├─ad_detection_board-7

│              │  └─weights

│              └─ad_detection_board-8

│                  └─weights

├─true_phone_picture                                     验证数据

│  ├─phone_photos

│  └─phone_results

└─vgg2yolo_obb                                           图像标记VGG导出数据转YOLO模型支持格式

    ├─check_results
    
    ├─datasets
    
    │  ├─images
    
    │  │  ├─train
    
    │  │  └─val
    
    │  └─labels
    
    │      ├─train
    
    │      └─val
    
    ├─images_board
    
    └─labels_txt




在线标注工具推荐https://www.makesense.ai/
