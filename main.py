import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Input and Output App')

# Create labels and input fields for each data item
parking_spots_label = QLabel('Number of parking spots (N x N, N = 3, 4, 5, 6, 7, 8):')
parking_spots_input = QLineEdit()

agv_shuttles_label = QLabel('Number of AGV shuttles:')
agv_shuttles_input = QLineEdit()

depots_label = QLabel('Number of depots (1 or 2):')
depots_input = QLineEdit()

parking_spot_width_label = QLabel('Parking spot width (2.5 [m]):')
parking_spot_width_input = QLineEdit()

parking_spot_height_label = QLabel('Parking spot height (5.5 [m]):')
parking_spot_height_input = QLineEdit()

speed_label = QLabel('AGV shuttles speed (0.5 - 2.0 [m/s]):')
speed_input = QLineEdit()

output_label = QLabel('')

# Define a function to display the entered data
def display_inputs():
    parking_spots = parking_spots_input.text()
    agv_shuttles = agv_shuttles_input.text()
    depots = depots_input.text()
    parking_spot_width = parking_spot_width_input.text()
    parking_spot_height = parking_spot_height_input.text()
    speed = speed_input.text()

    output_label.setText(f'Number of parking spots: {parking_spots}\n'
                         f'Number of AGV shuttles: {agv_shuttles}\n'
                         f'Number of depots: {depots}\n'
                         f'Parking spot width: {parking_spot_width}\n'
                         f'Parking spot height: {parking_spot_height}\n'
                         f'AGV shuttles speed: {speed}')

submit_button = QPushButton('Submit')
submit_button.clicked.connect(display_inputs)

# Create a vertical layout to arrange the widgets
layout = QVBoxLayout()
layout.addWidget(parking_spots_label)
layout.addWidget(parking_spots_input)
layout.addWidget(agv_shuttles_label)
layout.addWidget(agv_shuttles_input)
layout.addWidget(depots_label)
layout.addWidget(depots_input)
layout.addWidget(parking_spot_width_label)
layout.addWidget(parking_spot_width_input)
layout.addWidget(parking_spot_height_label)
layout.addWidget(parking_spot_height_input)
layout.addWidget(speed_label)
layout.addWidget(speed_input)
layout.addWidget(submit_button)
layout.addWidget(output_label)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
