import sys
from qtpy.QtWidgets import QApplication, QMainWindow
from qtcalendarlib.ui import Ui_MainWindow

app = QApplication(sys.argv)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

main_window = MainWindow()
main_window.show()

sys.exit(app.exec_())