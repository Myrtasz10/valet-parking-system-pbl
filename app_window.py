import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QGraphicsView, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QColor, QBrush, QPainter
from PyQt5.QtCore import QPropertyAnimation, QTimer, Qt, QPoint, QRect, QVariantAnimation, QTimeLine, QPointF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem

class TableExample:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.initUI()
        self.x = 0
        self.y = 0

    def initUI(self):
        layout = QVBoxLayout()

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
        
        # Create a red rectangle (QGraphicsRectItem) and add it to the scene
        # self.red_rect = QGraphicsRectItem(120, 128, 90, 90)
        # self.red_rect.setBrush(QBrush(QColor(255, 0, 0)))  # Red color
        # scene.addItem(self.red_rect)

        self.red_rect = QGraphicsRectItem(120, 128, 90, 90)
        self.red_rect.setBrush(QBrush(QColor(255, 0, 0)))  # Red color
        scene.addItem(self.red_rect)

        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.animateRedRectPosition)
        self.animation_duration = 10000  # Animation duration in milliseconds
        self.animation_steps = 100  # Number of animation steps
        self.step = 0

        # Start the animation timer
        self.animation_timer.start(self.animation_duration // self.animation_steps)

    def animateRedRectPosition(self):
        if self.step < self.animation_steps:
            # Calculate the new x position for the red rectangle
            new_x = 120 + (self.step / self.animation_steps) * 100  # Change 100 based on desired horizontal distance

            # Set the new position
            self.red_rect.setPos(new_x, 128)

            self.step += 1
        else:
            # Animation is complete, stop the timer
            self.animation_timer.stop()

        
        '''
    def animate(self):
        self.child = QWidget()
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(90, 90)
        self.animation = QPropertyAnimation(self.child, b"pos")
        self.animation.setEndValue(QPoint(400, 400))
        self.animation.setDuration(1500)
        self.animation.start()
        '''
    def start_animation(self, x, y):
        # Set the end value for the animation and start it
        self.animation.setEndValue(QPoint(x, y))
        self.animation.start()

    def animateRedRectPosition(self, pos):
        self.red_rect.setPos(pos)
        
    def run(self):
        self.window.show()
        self.app.exec_()

class RedRectangleWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(120, 128, 90, 90, QColor(255, 0, 0))  # Red color