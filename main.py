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


    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
