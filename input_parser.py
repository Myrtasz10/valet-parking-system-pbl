from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Parser:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle('Valet Parking System')
        self.parking_spots = None
        self.agv_shuttles = None
        self.depots = None
        self.parking_spot_width = None
        self.parking_spot_height = None
        self.speed = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.parking_spots_input = QLineEdit()
        self.agv_shuttles_input = QLineEdit()
        self.depots_input = QLineEdit()
        self.parking_spot_width_input = QLineEdit()
        self.parking_spot_height_input = QLineEdit()
        self.speed_input = QLineEdit()
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_submit)
        layout.addWidget(QLabel('Number of parking spots:'))
        layout.addWidget(self.parking_spots_input)
        layout.addWidget(QLabel('Number of AGV shuttles:'))
        layout.addWidget(self.agv_shuttles_input)
        layout.addWidget(QLabel('Number of depots:'))
        layout.addWidget(self.depots_input)
        layout.addWidget(QLabel('Parking spot width:'))
        layout.addWidget(self.parking_spot_width_input)
        layout.addWidget(QLabel('Parking spot height:'))
        layout.addWidget(self.parking_spot_height_input)
        layout.addWidget(QLabel('AGV shuttles speed:'))
        layout.addWidget(self.speed_input)
        layout.addWidget(self.submit_button)
        self.window.setLayout(layout)

    def on_submit(self):
        self.parking_spots = self.parking_spots_input.text()
        self.agv_shuttles = self.agv_shuttles_input.text()
        self.depots = self.depots_input.text()
        self.parking_spot_width = self.parking_spot_width_input.text()
        self.parking_spot_height = self.parking_spot_height_input.text()
        self.speed = self.speed_input.text()
        self.window.close()

    def run(self):
        self.window.show()
        self.app.exec_()
