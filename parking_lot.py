from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QToolButton, QGraphicsView, QGraphicsScene, QGridLayout
from PyQt5.QtCore import Qt
from car import Car  # Make sure to import your Car class

class ParkingLot(QWidget):
    def __init__(self, parser):
        super().__init__()
        self.parser = parser
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create joystick layout
        joystick_layout = QGridLayout()

        # Create arrow buttons
        self.up_button = QToolButton(self)
        self.up_button.setArrowType(Qt.UpArrow)
        self.down_button = QToolButton(self)
        self.down_button.setArrowType(Qt.DownArrow)
        self.left_button = QToolButton(self)
        self.left_button.setArrowType(Qt.LeftArrow)
        self.right_button = QToolButton(self)
        self.right_button.setArrowType(Qt.RightArrow)

        # Add buttons to joystick layout
        joystick_layout.addWidget(self.up_button, 0, 1)
        joystick_layout.addWidget(self.down_button, 2, 1)
        joystick_layout.addWidget(self.left_button, 1, 0)
        joystick_layout.addWidget(self.right_button, 1, 2)

        # Add joystick layout to main layout
        self.layout.addLayout(joystick_layout)

        # Create a QGraphicsView to display the grid
        self.view = QGraphicsView(self)
        self.layout.addWidget(self.view)

        # Create a QGraphicsScene and set it in the view
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

        # Add a grid of items to the scene
        self.addGrid()

        # Add a car to the scene
        self.addCar()

        # Connect buttons to car's functions
        self.up_button.clicked.connect(self.car.move_up)
        self.down_button.clicked.connect(self.car.move_down)
        self.left_button.clicked.connect(self.car.move_left)
        self.right_button.clicked.connect(self.car.move_right)

    def addGrid(self):
        cell_size = 100
        num_rows = int(self.parser.parking_spots)
        num_cols = int(self.parser.parking_spots)
        for row in range(num_rows):
            for col in range(num_cols):
                x = col * cell_size
                y = row * cell_size
                self.scene.addRect(x, y, cell_size, cell_size)

    def addCar(self):
        cell_size = 100
        start_space = (0, 0)
        start_x = start_space[1] * cell_size
        start_y = start_space[0] * cell_size
        self.car = Car(start_x, start_y, 90, 90)
        self.scene.addItem(self.car)
