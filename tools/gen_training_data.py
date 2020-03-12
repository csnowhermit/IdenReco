import os
import xml.dom.minidom
from PIL import Image
import matplotlib.pyplot as plt
import uuid
import time

'''
    生成训练数据
'''

base_mark_dir = "D:/idenreco-mark/"

def get_rect_info(filename):
    dom = xml.dom.minidom.parse(filename)

    path = dom.getElementsByTagName("path")[0].childNodes[0].data

    objectList = dom.getElementsByTagName("object")
    d = {}
    for obj in objectList:
        name = obj.getElementsByTagName("name")[0].childNodes[0].data
        box = obj.getElementsByTagName("bndbox")[0]

        xmin = box.getElementsByTagName("xmin")[0].childNodes[0].data
        ymin = box.getElementsByTagName("ymin")[0].childNodes[0].data
        xmax = box.getElementsByTagName("xmax")[0].childNodes[0].data
        ymax = box.getElementsByTagName("ymax")[0].childNodes[0].data

        d[name] = (xmin, ymin, xmax, ymax)
    return path, d

if __name__ == '__main__':
    for filename in os.listdir(base_mark_dir):
        filepath, details = get_rect_info(os.path.join(base_mark_dir, filename))
        # print(filepath, details)

        if os.path.exists(filepath) is False:
            print("WARNING:", filepath, " not Exists")

        img = Image.open(filepath)
        for name in details.keys():
            crop_position = details[name]
            # print(name, int(crop_position[0]), int(crop_position[1]), int(crop_position[2]), int(crop_position[3]))
            # print(type(crop_position))
            # print(crop_position[0])
            # 开始截取标注部分
            rect = img.crop((int(crop_position[0]), int(crop_position[1]), int(crop_position[2]), int(crop_position[3])))
            # print("rect:", type(rect))
            # plt.figure(name)
            # plt.imshow(rect)
            # plt.show()
            rect_name = "D:/IdenReco预处理/" + str(name) + "_" + str(uuid.uuid1()) + ".jpg"
            rect.save(rect_name, quality=95)
            time.sleep(0.1)
