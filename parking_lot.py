from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QMenu, QAction
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QContextMenuEvent
from random import randint
from car import Car
from parking_space import ParkingSpace

class ParkingLot(QWidget):
    def __init__(self, parser):
        super().__init__()
        self.parser = parser
        self.parking_spaces = []
        self.cars = []
        self.parking_width = int(parser.parking_spot_width) * 50
        self.parking_height = int(parser.parking_spot_height) * 50
        self.num_rows = int(parser.parking_spots_rows)
        self.num_cols = int(parser.parking_spots_cols)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.view = QGraphicsView(self)
        self.layout.addWidget(self.view)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.addGrid()


        window_width = (self.num_cols + 1) * self.parking_width
        window_height = (self.num_rows + 1) * self.parking_height

        # Set the fixed window size
        self.setFixedSize(window_width, window_height)

    def contextMenuEvent(self, event):
        pos = event.pos()
        contextMenu = QMenu(self)
        addCar = QAction('Add Car', self)
        addCar.triggered.connect(lambda: self.addCar(pos))
        contextMenu.addAction(addCar)
        contextMenu.exec_(event.globalPos())

    def addGrid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                x = col * self.parking_width
                y = row * self.parking_height
                parking_space = ParkingSpace(x, y, self.parking_width, self.parking_height)
                self.parking_spaces.append(parking_space)
                self.scene.addItem(parking_space)  # Add it to the scene


    def addCar(self, position):
        x = int((position.x() - self.parking_width / 2) 
                // self.parking_width * self.parking_width + 5)
        y = int((position.y() - self.parking_height / 2) // 
                self.parking_height * self.parking_height + 5)
        car = Car(x, y, self.parking_width - 10, self.parking_height - 10, self.parser.speed)
        self.cars.append(car)
        self.scene.addItem(car)