from PyQt5.QtWidgets import QApplication
import sys
from input_parser import Parser
from parking_lot import ParkingLot

if __name__ == '__main__':
    app = QApplication(sys.argv)

    parser = Parser()
    parser.run()

    parking_lot = ParkingLot(parser)
    parking_lot.show()

    # Example usage of the animate function
    start_space = (0, 0)
    end_space = (0, 1)
    cell_size = 100  # This should match the size used in addGrid

    parking_lot.car.animate(start_space, end_space, cell_size, parser.speed, parser.parking_spot_width)

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
