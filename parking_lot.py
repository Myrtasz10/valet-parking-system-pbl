from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QMenu, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QContextMenuEvent
from random import randint
from car import Car

class ParkingLot(QWidget):
    def __init__(self, parser):
        super().__init__()
        self.parser = parser
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.view = QGraphicsView(self)
        self.layout.addWidget(self.view)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.addGrid()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        addCar = QAction('Add Car', self)
        addCar.triggered.connect(lambda: self.addCar(event.pos()))
        contextMenu.addAction(addCar)
        contextMenu.exec_(event.globalPos())

    def addGrid(self):
        cell_size = 100
        num_rows = int(self.parser.parking_spots)
        num_cols = int(self.parser.parking_spots)
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * cell_size
                y = row * cell_size
                self.scene.addRect(x, y, cell_size, cell_size)

    def addCar(self, position):
        cell_size = 100
        x = position.x() // cell_size * cell_size + (cell_size - 90) / 2
        y = position.y() // cell_size * cell_size + (cell_size - 90) / 2
        car = Car(x, y, 90, 90)
        self.scene.addItem(car)