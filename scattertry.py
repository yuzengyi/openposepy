# import sys
# import random
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# from PyQt5.QtChart import QScatterSeries, QChart, QChartView, QPolarChart
# # from PyQt5.QtChart.QChart
#
# class MyScatterWindow(QWidget):
#     def __init__(self, parent=None):
#         super(MyScatterWindow, self).__init__(parent)
#         self.resize(800, 600)
#         chart = QChart()
#         chartView = QChartView()
#
#         print(PYQT_VERSION_STR)
#
#         scatter = QScatterSeries()
#         for value in range(1, 500):
#             scatter.append(value, random.random() * 10)
#             # scatter.append(QPointF(value, random.random()*10))
#
#         scatter.setName("散点图")
#         scatter.setMarkerSize(8)  # 标记大小
#         # scatter.setMarkerShape(QScatterSeries.MarkerShapeRectangle) #方形标记
#         scatter.setMarkerShape(QScatterSeries.MarkerShapeCircle)  # 圆形标记
#         pen = QPen()
#         pen.setColor(Qt.red)
#         pen.setWidth(2)
#         scatter.setPen(pen)
#
#         chart.addSeries(scatter)
#         chart.createDefaultAxes()
#
#         chartView.setChart(chart)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(chartView)
#
#         self.setLayout(vbox)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     win = MyScatterWindow()
#     win.show()
#     sys.exit(app.exec_())