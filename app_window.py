import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtCore import QPropertyAnimation, QTimer, Qt, QPoint, QRect, QVariantAnimation, QTimeLine, QPointF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem

class Table(QWidget):
    def __init__(self):
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

        # Create a QGraphicsView to hold the table
        graphics_view = QGraphicsView()
        # Create a QGraphicsScene
        scene = QGraphicsScene()
        graphics_view.setScene(scene)
        graphics_view.setMinimumSize(500, 500)
        graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Set the number of rows and columns
        table_widget = QTableWidget()

        # Set the number of rows and columns
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        # Set the item size for table cells
        cell_size = 100  # Adjust this value as needed
        table_widget.verticalHeader().setDefaultSectionSize(cell_size)
        table_widget.horizontalHeader().setDefaultSectionSize(cell_size)

        # Populate the table with items (rectangular cells)
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem()
                table_widget.setItem(i, j, item)

        table_widget.resize(317, 325)
        scene.addWidget(table_widget)

        self.button = QPushButton('Start', clicked=self.animation)
        self.layout.addWidget(self.button)

        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: red;')
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.move(10, 10)
        self.frame.resize(100, 100)

    def animation(self):
        self.animation = QPropertyAnimation(self.frame, b'geometry')
        self.animation.setDuration(10000) # mm seconds
        self.animation.setStartValue(QRect(10, self.frame.y(), 100, 100))
        self.animation.setEndValue(QRect(10, self.frame.y(), 200, 200))
        self.animation.start()