import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtCore import QPropertyAnimation, QTimer, Qt, QPoint, QRect, QVariantAnimation, QTimeLine, QPointF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem

class Table(QWidget):  
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        super().__init__()
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 30px;
            }
        ''')        

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button = QPushButton('Start', clicked=self.animation)
        self.layout.addWidget(self.button)

        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: red;')
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.move(10, 10)
        self.frame.resize(100, 100)
        
        table_widget = QTableWidget()

        # Set the number of rows and columns
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)
        
        cell_size = 100
        
        for i in range(3):
            table_widget.setColumnWidth(i, cell_size)
            table_widget.setRowHeight(i, cell_size)

        # Populate the table with items (rectangular cells)
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem()
                table_widget.setItem(i, j, item)

        self.layout.addWidget(table_widget)
        self.window.setLayout(self.layout)  # Set the layout for the main window
        self.window.setWindowTitle("3x3 Table Example")

    def animation(self):
        self.animation = QPropertyAnimation(self.frame, b'geometry')
        self.animation.setDuration(10000) # mm seconds
        self.animation.setStartValue(QRect(10, self.frame.y(), 100, 100))
        self.animation.setEndValue(QRect(10, self.frame.y(), 200, 200))
        self.animation.start()