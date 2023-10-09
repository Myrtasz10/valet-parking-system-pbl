from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Parser:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.window.setWindowTitle('Input and Output App')

        # Define instance variables for program parameters
        self.parking_spots = None
        self.agv_shuttles = None
        self.depots = None
        self.parking_spot_width = None
        self.parking_spot_height = None
        self.speed = None

        self.setup_ui()

    def setup_ui(self):
        # Create labels and input fields for each data item
        self.parking_spots_label = QLabel('Number of parking spots (N x N, N = 3, 4, 5, 6, 7, 8):')
        self.parking_spots_input = QLineEdit()

        self.agv_shuttles_label = QLabel('Number of AGV shuttles:')
        self.agv_shuttles_input = QLineEdit()

        self.depots_label = QLabel('Number of depots (1 or 2):')
        self.depots_input = QLineEdit()

        self.parking_spot_width_label = QLabel('Parking spot width (2.5 [m]):')
        self.parking_spot_width_input = QLineEdit()

        self.parking_spot_height_label = QLabel('Parking spot height (5.5 [m]):')
        self.parking_spot_height_input = QLineEdit()

        self.speed_label = QLabel('AGV shuttles speed (0.5 - 2.0 [m/s]):')
        self.speed_input = QLineEdit()

        self.output_label = QLabel('')

        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_submit)

        # Create a vertical layout to arrange the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.parking_spots_label)
        layout.addWidget(self.parking_spots_input)
        layout.addWidget(self.agv_shuttles_label)
        layout.addWidget(self.agv_shuttles_input)
        layout.addWidget(self.depots_label)
        layout.addWidget(self.depots_input)
        layout.addWidget(self.parking_spot_width_label)
        layout.addWidget(self.parking_spot_width_input)
        layout.addWidget(self.parking_spot_height_label)
        layout.addWidget(self.parking_spot_height_input)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.output_label)
        self.window.setLayout(layout)

    def on_submit(self):
        # Retrieve and store the entered data in instance variables
        self.parking_spots = self.parking_spots_input.text()
        self.agv_shuttles = self.agv_shuttles_input.text()
        self.depots = self.depots_input.text()
        self.parking_spot_width = self.parking_spot_width_input.text()
        self.parking_spot_height = self.parking_spot_height_input.text()
        self.speed = self.speed_input.text()

        # Close the window after submitting
        self.window.close()

    def run(self):
        self.window.show()
        self.app.exec_()