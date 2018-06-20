# keras.applications-GUI

****
|Author|HoshinoKun|
|---|---
|E-mail|hoshinokun@346pro.club
****

## 目录
* [介绍](#介绍)
* [准备](#准备)
* [运行](#运行)

介绍
------
这是基于keras.applications的imagenet编写的imagenet调用图片识别程序，该程序可以调用imagenet库所训练好的五个图像识别模型，分别是'VGG16', 'VGG19', 'InceptionV3', 'Xception', 'ResNet50'这五种。使用命令行形式打开，输入图片后会显示用对应模型所识别出来的五种可能性最高的物品以及其概率

准备
------
使用该Python文件，你需要在系统中安装：anaconda、以TensorFlow为后端的keras、OpenCv。本程序测试通过环境为：Anaconda 5.1.0 + TensorFlow 1.8.0 + Keras 2.2.0 + opencv-python 3.4.1.15 + ArchLinux以及Anaconda 5.1.0 + TensorFlow 1.8.0 + Keras 2.2.0 + opencv-python 3.4.1.15 + Windows 10。注意，本文件路径以及输入图片路径不可为中文

运行
------
```
python GUI.py
```