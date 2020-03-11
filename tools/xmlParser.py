
import xml.dom.minidom

'''
    xml解析：解析标注文件，从原图中截取指定内容
'''


dom = xml.dom.minidom.parse("../IdenReco-mark/20200108080005.2.6577.0.33.10.0.5-2.mpg_frame_0120.xml")

root = dom.getElementsByTagName("path")
print(root)

# database=datalist.getElementsByTagName('database')