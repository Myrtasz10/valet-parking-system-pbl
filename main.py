from PyQt5.QtWidgets import QApplication
import sys
from input_parser import Parser
from parking_lot import ParkingLot
import time

def process_moves(filename, parking_lot):
    with open(filename, 'r') as file:
        for line in file:
            action, car_id_str = line[0], line[1:].strip()  # Split the action (+/-) and car ID
            
            if action == '+':  # If the action is to add a car
                parking_lot.addCarAtDepot()
            elif action == '-':  # If the action is to remove a car
                car_id = int(car_id_str)
                parking_lot.remove_car(car_id)  # Assuming remove_car is a method to remove cars
            else:
                print(f"Invalid action in line: {line}")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    parser = Parser()
    parser.run()

    parking_lot = ParkingLot(parser)
    parking_lot.show()

    # process_moves("test.moves", parking_lot)

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

