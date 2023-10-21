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
        self.initUI()
        self.selected_car = None

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.view = QGraphicsView(self)
        self.layout.addWidget(self.view)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.addGrid()

        num_rows = int(self.parser.parking_spots)
        num_cols = int(self.parser.parking_spots)

        cell_size = 100  # Assuming each parking space is 100x100 pixels
        window_width = (num_cols + 1) * cell_size
        window_height = (num_rows + 1) * cell_size

        # Set the fixed window size
        self.setFixedSize(window_width, window_height)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        addCar = QAction('Add Car', self)
        addCar.triggered.connect(lambda: self.addCar(event.pos()))
        contextMenu.addAction(addCar)

        if self.selected_car and self.selected_car.setting_destination:
            goHere = QAction('Go Here', self)
            goHere.triggered.connect(lambda: self.goHere(event.pos()))
            contextMenu.addAction(goHere)

        contextMenu.exec_(event.globalPos())

    def addGrid(self):
        cell_size = 100
        num_rows = int(self.parser.parking_spots)
        num_cols = int(self.parser.parking_spots)
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * cell_size
                y = row * cell_size
                parking_space = ParkingSpace(x, y, cell_size, cell_size)  # Create an instance of your custom class
                self.scene.addItem(parking_space)  # Add it to the scene


    def addCar(self, position):
        cell_size = 100
        x = int((position.x() - 50) // cell_size * cell_size + (cell_size - 90) / 2)
        y = int((position.y() - 50) // cell_size * cell_size + (cell_size - 90) / 2)
        car = Car(x, y, 90, 90)
        # car.settingDestinationSignal.connect(self.setSelectedCar) 
        self.scene.addItem(car)


    def goHere(self, position):
        cell_size = 100
        x = position.x() // cell_size
        y = position.y() // cell_size
        destination = QPoint(int(x), int(y))
        self.selected_car.moveToDestination(destination)
        self.selected_car.setting_destination = False
        self.selected_car = None  # Reset the selected car


    def setSelectedCar(self, car):
        self.selected_car = car