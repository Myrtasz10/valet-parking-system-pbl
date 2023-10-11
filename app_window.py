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

        # Create a QGraphicsView to display the grid
        self.view = QGraphicsView(self)
        self.view.setGeometry(10, 10, 317, 325)  # Adjust the geometry as needed

        # Create a QGraphicsScene and set it in the view
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        # Add a grid of items to the scene
        self.addGrid()
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: red;')
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.move(124, 128)
        self.frame.resize(90, 90)
        
    def addGrid(self):
        cell_size = 100
        num_rows = 3
        num_cols = 3

        for row in range(num_rows):
            for col in range(num_cols):
                x = col * cell_size
                y = row * cell_size
                rect_item = QGraphicsRectItem(x, y, cell_size, cell_size)
                rect_item.setPen(QColor(Qt.black))  # Grid lines' color
                self.scene.addItem(rect_item)

    def animation(self):
        self.animation = QPropertyAnimation(self.frame, b'geometry')
        self.animation.setDuration(1000) # mm seconds
        self.animation.setStartValue(QRect(124, 128, 90, 90))
        self.animation.setEndValue(QRect(224, 128, 90, 90))
        self.animation.start()