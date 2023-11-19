from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtCore import QTimer
import time

class AutoCloseMessageBox(QMessageBox):
    def __init__(self, timeout=3, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.setWindowTitle("Processing")
        self.setText("Calculating the moves...")
        self.setStandardButtons(QMessageBox.NoButton)