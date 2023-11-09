import sys

from PyQt5.QtWidgets import QApplication

from Mediabofang import myMainWindow
from Thresholding import Kmeans_threshold
from ctp import getctp
from dtp import getdtp
from itp import getitp
from openposeframe import openpose_i_j

Ctp = []
Dtp = []
Itp = []
#第i帧
for i in range(0,100):
    keypoints_matrix=openpose_i_j(i,0)
    # 提取x坐标
    x = [point[0] for point in keypoints_matrix]
    # 提取y坐标
    y = [point[1] for point in keypoints_matrix]
    # 提取置信度
    c = [point[2] for point in keypoints_matrix]
    #阈值
    threshold = Kmeans_threshold(c)
    # print(threshold)
    Ctp.append(getctp(x, c, threshold))
    Dtp.append(getdtp(y, c, threshold))
    Itp.append(getitp(y, c, threshold))

print(Itp)
CTP=sum(Ctp)
DTP=sum(Dtp)
ITP=sum(Itp)
print(ITP)
app = QApplication(sys.argv)
vieo_gui = myMainWindow()
vieo_gui.show()
sys.exit(app.exec_())