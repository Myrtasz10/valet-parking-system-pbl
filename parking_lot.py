from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QMenu, QAction, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QContextMenuEvent
from random import randint
import copy
import time
from PyQt5.QtWidgets import QMessageBox

from car import Car
from parking_space import ParkingSpace, ParkingSpaceSingleton
from A_star import free_up_space

class ParkingLot(QWidget):
    def __init__(self, parser):
        super().__init__()
        self.parser = parser

        self.parking_spaces = []
        parking_singleton = ParkingSpaceSingleton()
        parking_singleton.parking_spaces = self.parking_spaces 

        self.cars = []
        #4D
        self.histories = []
        self.parking_width = int(parser.parking_spot_width) * 50
        self.parking_height = int(parser.parking_spot_height) * 50
        self.num_rows = int(parser.parking_spots_rows)
        self.num_cols = int(parser.parking_spots_cols)
        self.depot_coords = (0, 0)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.view = QGraphicsView(self)
        self.layout.addWidget(self.view)
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        self.addGrid()
        self.addButton = QPushButton('Add Car at Depot', self)
        self.addButton.clicked.connect(self.addCarAtDepot)
        self.layout.addWidget(self.addButton)

        self.addButton = QPushButton('Remove Car from Depot', self)
        self.addButton.clicked.connect(self.removeCarFromDetpot)
        self.layout.addWidget(self.addButton)


        window_width = (self.num_cols + 1) * self.parking_width
        window_height = (self.num_rows + 1) * self.parking_height

        # Set the fixed window size
        self.setFixedSize(window_width, window_height)

    def is_free_space(self):
        free_space_count = 0  # Counter for unoccupied spaces
        for col_spaces in self.parking_spaces:
            for space in col_spaces:
                if not space.occupied:
                    free_space_count += 1
                    if free_space_count >= 2:  # Check if at least two free spaces are found
                        return True
        return False  # Less than two free spaces available

    def addCarAtDepot(self):
        col, row = self.depot_coords

        if not self.is_free_space():
            message = f"There must be at least one free parking space!"
            QMessageBox.information(None, "Cannot add car at depot", message)
            return

        if self.parking_spaces[col][row].occupied:
            free_up_space(self.parking_spaces, (col, row))

        car = Car(col, row, self.parking_width - 10, self.parking_height - 10, self.parser.speed, self)
        self.cars.append(car)
        self.scene.addItem(car)

        self.parking_spaces[col][row].car = car
        self.parking_spaces[col][row].occupied = True

    def removeCarFromDetpot(self):
        col, row = self.depot_coords

        if not self.parking_spaces[col][row].occupied:
            message = f"There is no car at depot"
            QMessageBox.information(None, "Cannot remove car from depot", message)
            return


        self.parking_spaces[col][row].car.remove_car()

    def contextMenuEvent(self, event):
        pos = event.pos()
        contextMenu = QMenu(self)
        addCar = QAction('Add Car', self)
        addCar.triggered.connect(lambda: self.addCar(pos))
        contextMenu.addAction(addCar)
        
        # New action for freeing up space
        freeSpace = QAction('Free Up Space', self)
        freeSpace.triggered.connect(lambda: self.freeUpSpace(pos))
        contextMenu.addAction(freeSpace)
        
        contextMenu.exec_(event.globalPos())

    def addGrid(self):
        for col in range(self.num_cols):
            col_spaces = []
            for row in range(self.num_rows):
                x = col * self.parking_width
                y = row * self.parking_height
                parking_space = ParkingSpace(x, y, self.parking_width, self.parking_height)
                col_spaces.append(parking_space)
                self.scene.addItem(parking_space)
            self.parking_spaces.append(col_spaces)
        
        depot_col, depot_row = self.depot_coords

        self.parking_spaces[depot_col][depot_row].setAsDepot()


    def addCar(self, position):
        col = int((position.x() - self.parking_width / 2) // self.parking_width)
        row = int((position.y() - self.parking_height / 2) // self.parking_height)

        if self.parking_spaces[col][row].occupied:
            return

        car = Car(col, row, self.parking_width - 10, self.parking_height - 10, self.parser.speed, self)
        self.cars.append(car)
        self.scene.addItem(car)

        self.parking_spaces[col][row].car = car
        self.parking_spaces[col][row].occupied = True


    def freeUpSpace(self, position):
        col = int((position.x() - self.parking_width / 2) // self.parking_width)
        row = int((position.y() - self.parking_height / 2) // self.parking_height)

        if not self.parking_spaces[col][row].occupied:
            QMessageBox.information(self, "Info", "This space is already free.")
            return

        free_up_space(self.parking_spaces, (col, row))

        
    #Dijkstra
    #self; desired vehicle column; row; parking lot history in Dijkstra; parking lot
    def pathfindToDepot(self, col, row, history, parking_lot):
        print(str(col), str(row))
        if col == 0 and row == 0:
            #histories are being printed, now extract and execute them (idk where you put the function to do that, preferably in car.py)
            print("path found!")
            history.append(copy.deepcopy(parking_lot))
            print(history)
            self.histories.append(copy.deepcopy(history))
            return
        if parking_lot in history:
            return
        print(parking_lot)
        print("not in")
        print(history)
        #apparently .append uses the reference to parking_lot, so a copy has to be made
        history.append(copy.deepcopy(parking_lot))

        c = 0
        for parking_column in parking_lot:
            r = 0
            for parking_space in parking_column:
                if parking_space is True:
                    print(str(c), str(self.num_cols))
                    print(str(r), str(self.num_rows))
                    # left
                    if c > 0:
                        if not parking_lot[c-1][r]:
                            print("left")
                            print(parking_lot)
                            parking_lot[c][r] = False
                            parking_lot[c-1][r] = True
                            
                            if c == col and r == row:
                                self.pathfindToDepot(col-1, row, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            else:
                                self.pathfindToDepot(col, row, copy.deepcopy(history), copy.deepcopy(parking_lot))
                                
                            print("exit left")
                            print(parking_lot)
                            parking_lot[c][r] = True
                            parking_lot[c-1][r] = False
                            print(parking_lot)
                    #up
                    if r > 0: 
                        if not parking_lot[c][r-1]:
                            print("up")
                            print(parking_lot)
                            parking_lot[c][r] = False
                            parking_lot[c][r-1] = True
                            if c == col and r == row:
                                self.pathfindToDepot(col, row-1, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            else:
                                self.pathfindToDepot(col, row, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            print("exit up")
                            print(parking_lot)
                            parking_lot[c][r] = True
                            parking_lot[c][r-1] = False         
                            print(parking_lot)

                    #right
                    if c < self.num_cols - 1:
                        if not parking_lot[c+1][r]:
                            print("right")
                            print(parking_lot)
                            parking_lot[c][r] = False
                            parking_lot[c+1][r] = True
                            if c == col and r == row:
                                self.pathfindToDepot(col+1, row, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            else:
                                self.pathfindToDepot(col, row, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            print("exit right")
                            print(parking_lot)
                            parking_lot[c][r] = True
                            parking_lot[c+1][r] = False
                            print(parking_lot)
                    #down
                    if r < self.num_rows - 1: 
                        if not parking_lot[c][r+1]:
                            print("down")
                            print(parking_lot)
                            parking_lot[c][r] = False
                            parking_lot[c][r+1] = True
                            if c == col and r == row:
                                self.pathfindToDepot(col, row+1, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            else:
                                self.pathfindToDepot(col, row, copy.deepcopy(history), copy.deepcopy(parking_lot))
                            print("exit down")
                            print(parking_lot)
                            parking_lot[c][r] = True
                            parking_lot[c][r+1] = False
                            print(parking_lot)
                r += 1
            c += 1
            
    #return: 2D list of boolean
    def mapParkingLot(self):
        parking_lot = []
        for parking_column in self.parking_spaces:
            column = []
            for parking_space in parking_column:
                print(parking_space.occupied)
                column.append(parking_space.occupied)
            parking_lot.append(column)
        return parking_lot

    def animateToDepot(self):
        print(self.histories)
        if(self.histories.count == 0):
            print("No path was found")
            return
        shortest_path = min(self.histories, key = len)
        print("The shortest path:", shortest_path)
        print("The cars:", self.cars)
        s = 0
        for state in shortest_path:
            if s >= len(shortest_path) - 1:
                print("terminated", s)
                return
            c = 0
            for column in state:
                r = 0
                for spot in column:
                    if spot and not shortest_path[s+1][c][r]:
                        print("Car moved!")
                        print(c, r, self.cars[0].col, self.cars[0].row)
                        
                        if c > 0 and not state[c-1][r] and shortest_path[s+1][c-1][r]:
                            print("Left moving")
                            print(state[c-1][r])
                            print(shortest_path[s+1][c-1][r])
                            for car_number in range(len(self.cars)):
                                if self.cars[car_number].col == c and self.cars[car_number].row == r:
                                    print("Left", car_number)
                                    #print("Prestate:", self.mapParkingLot())
                                    self.cars[car_number].move_left()
                                    #print("Poststate:", self.mapParkingLot())
                                    print("Left")
                                print(self.cars[car_number].col, c)
                                print(self.cars[car_number].row, r)
                        #else:
                        #    print("Left:")
                        #    print(state[c-1][r])
                        #    print(shortest_path[s+1][c-1][r])
                        
                        elif r > 0 and not state[c][r-1] and shortest_path[s+1][c][r-1]:
                            print("Up moving")
                            for car_number in range(len(self.cars)):
                                if self.cars[car_number].col == c and self.cars[car_number].row == r:
                                    print("Up", car_number)
                                    print("Prestate:", self.mapParkingLot())
                                    self.cars[car_number].move_up()
                                    print("Poststate:", self.mapParkingLot())
                                    print("Up")
                                print(self.cars[car_number].col, c)
                                print(self.cars[car_number].row, r)
                                
                        #else:
                        #    print("Up:")
                        #    print(state[c][r-1])
                        #    print(shortest_path[s+1][c][r-1])
                        
                        
                        elif c < self.num_cols - 1 and not state[c+1][r] and shortest_path[s+1][c+1][r]:
                            print("Right moving")
                            for car_number in range(len(self.cars)):
                                if self.cars[car_number].col == c and self.cars[car_number].row == r:
                                    print("Right", car_number)
                                    self.cars[car_number].move_right()
                                    print("Right")
                                print(self.cars[car_number].col, c)
                                print(self.cars[car_number].row, r)
                        #else:
                        #    print("Right:")
                        #    print(state[c+1][r])
                        #    print(shortest_path[s+1][c+1][r])
                        
                        
                        elif r < self.num_rows - 1 and not state[c][r+1] and shortest_path[s+1][c][r+1]:
                            print("Down moving")
                            for car_number in range(len(self.cars)):
                                if self.cars[car_number].col == c and self.cars[car_number].row == r:
                                    print("Down", car_number)
                                    self.cars[car_number].move_down()
                                    print("Down")
                                print(self.cars[car_number].col, c)
                                print(self.cars[car_number].row, r)
                        #else:
                        #    print("Down:")
                        #    print(state[c][r+1])
                        #    print(shortest_path[s+1][c][r+1])
                        
                    r += 1
                c += 1
            s += 1
                    
        

        