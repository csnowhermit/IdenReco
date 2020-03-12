import os
import shutil

'''
    旧数据处理，合并成训练集
'''

origin_dir = "../station_data/"
targetpath = "D:/IdenReco预处理/"

for typedir in os.listdir(origin_dir):
    fullpath = os.path.join(origin_dir, typedir)
    for filename in os.listdir(fullpath):
        filepath = os.path.join(fullpath, filename)
        targetname = filename.split("-")[0] + "_" + str(filename.__hash__()) + ".jpg"
        shutil.copyfile(filepath, os.path.join(targetpath, targetname))



