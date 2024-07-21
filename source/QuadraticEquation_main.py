from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

from list_themes import *
import QuadraticEquation


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('QuadraticEquation.ui')
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.lineEdit_1.returnPressed.connect(self.handleCalc)
        self.ui.lineEdit_2.returnPressed.connect(self.handleCalc)
        self.ui.lineEdit_3.returnPressed.connect(self.handleCalc)

    def handleCalc(self):
        self.ui.textBrowser.clear()
        a = int(self.ui.lineEdit_1.text())
        b = int(self.ui.lineEdit_2.text())
        c = int(self.ui.lineEdit_3.text())
        x = QuadraticEquation.funEquation(a, b, c)
        self.ui.textBrowser.append(x)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[12], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
