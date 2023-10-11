from app_window import Table
from parser_1 import Parser
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, \
                            QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect, QPropertyAnimation

if __name__ == '__main__':
    parser = Parser()
    parser.run()

    # Access the program parameters after the window is closed
    print(f'Number of parking spots: {parser.parking_spots}')
    print(f'Number of AGV shuttles: {parser.agv_shuttles}')
    print(f'Number of depots: {parser.depots}')
    print(f'Parking spot width: {parser.parking_spot_width}')
    print(f'Parking spot height: {parser.parking_spot_height}')
    print(f'AGV shuttles speed: {parser.speed}')
    
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
#    while(True):
#        app_window.start_animation(220, 128)
#        time.sleep(0.5)
#        app_window.start_animation(220, 228)
#        time.sleep(0.5)
#        app_window.start_animation(120, 228)
#        time.sleep(0.5)
#        app_window.start_animation(120, 128)
#        time.sleep(0.5)