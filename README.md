# IdenReco

身份识别，使用ResNet50网络。



## 数据集

### 简易版数据集：

​	idenreco-jpg.7z，可直接用

### 完整版数据集：

​	完整版数据集：idenreco-dataset.7z，见百度网盘。

​	完整版标注集：idenreco-mark.7z。

​	直接可训练的数据集：training_set.7z，见百度网盘。

## Note：

## 1、数据集准备阶段

### 1、tools（训练数据集的准备）

1.1、gen_training_data.py，根据标注，从idenreco-dataset.7z数据集中截取出训练集，运行脚本之前需先将idenreco.7z解压后复制出一份，重命名为 IdenReco数据集2。

1.2、gen_old_data_process.py，将idenreco-jpg.7z中数据集分类重命名。

1.3、执行完前两步之后，手动将数据集整理成training_set.7z的目录结构，并执行util.py脚本进行训练集和测试集的拆分。

### 2、其他办法

​	也可直接下载training_set.7z数据集，并执行util.py脚本进行训练集和测试集的拆分。

## 2、训练阶段

​	运行station_personnel.py脚本进行训练。

