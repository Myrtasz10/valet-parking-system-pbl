from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsRectItem, QMenu, QAction
from PyQt5.QtCore import QVariantAnimation, QPointF, QPoint
from PyQt5.QtCore import QObject, pyqtSignal, QEventLoop
from parking_space import ParkingSpace, ParkingSpaceSingleton

class Car(QGraphicsRectItem):
    settingDestinationSignal = pyqtSignal(object) 

    def __init__(self, col, row, width, height, speed, containing_parking_lot):
        self.parking_space_width = width + 10
        self.parking_space_height = height + 10

        self.col = col
        self.row = row

        start_x = col * self.parking_space_width + 5
        start_y = row * self.parking_space_height + 5

        super().__init__(start_x, start_y, width, height)

        self.singleton = ParkingSpaceSingleton()
        self.parking_spaces = self.singleton.parking_spaces

        self.setBrush(QColor('#0000ff'))
        self.setAcceptHoverEvents(True)
        self.speed = speed
        
        self.parking_lot = containing_parking_lot


    def hoverEnterEvent(self, event):
        self.setBrush(QColor('#0000cc'))

    def hoverLeaveEvent(self, event):
        self.setBrush(QColor('#0000ff'))

    def contextMenuEvent(self, event):
        contextMenu = QMenu()
        
        moveMenu = QMenu('Move', contextMenu)
        moveUp = QAction('↑', moveMenu)
        moveDown = QAction('↓', moveMenu)
        moveLeft = QAction('←', moveMenu)
        moveRight = QAction('→', moveMenu)
        moveToDepot = QAction('Move to depot', contextMenu)
        
        moveUp.triggered.connect(self.move_up)
        moveDown.triggered.connect(self.move_down)
        moveLeft.triggered.connect(self.move_left)
        moveRight.triggered.connect(self.move_right)
        moveToDepot.triggered.connect(self.move_to_depot)
        
        moveMenu.addAction(moveUp)
        moveMenu.addAction(moveDown)
        moveMenu.addAction(moveLeft)
        moveMenu.addAction(moveRight)
        
        contextMenu.addMenu(moveMenu)
        contextMenu.addAction(moveToDepot)
        
        # setDestination = QAction('Set Destination')
        # setDestination.triggered.connect(self.activateSetDestination)
        # contextMenu.addAction(setDestination)
        
        contextMenu.exec_(event.screenPos())



    def animate(self, start_space, end_space, 
                parking_space_width, parking_space_height, speed, distance):
        time = float(distance) / float(speed)
        time *= 1000
        time = int(time)

        self.col = end_space[0]
        self.row = end_space[1]

        current_x, current_y = self.x(), self.y()

        end_x = current_x + (end_space[0] - start_space[0]) * parking_space_width
        end_y = current_y + (end_space[1] - start_space[1]) * parking_space_height

        self.animation = QVariantAnimation()
        self.animation.setDuration(time)
        self.animation.setStartValue(QPointF(current_x, current_y))
        self.animation.setEndValue(QPointF(end_x, end_y))
        self.animation.valueChanged.connect(self.setPos)
        self.animation.start()
        
        #await for animation to finish
        loop = QEventLoop()

        def animation_finished():
            loop.quit()

        self.animation.finished.connect(animation_finished)

        # Start the animation
        self.animation.start()

        # Wait for the animation to finish
        loop.exec_()

    def move_up(self):
        start_space = (self.col, self.row)
        end_space = (self.col, self.row - 1)
        distance = self.parking_space_height / 50
        try:
            if self.parking_spaces[end_space[0]][end_space[1]].occupied:
                return 
        except IndexError:
            print("Can't move past the parking lot")
            return
        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)
        
        self.parking_spaces[start_space[0]][start_space[1]].occupied = False 
        self.parking_spaces[end_space[0]][end_space[1]].occupied = True 

    def move_down(self):
        start_space = (self.col, self.row)
        end_space = (self.col, self.row + 1)
        distance = self.parking_space_height / 50
        try:
            if self.parking_spaces[end_space[0]][end_space[1]].occupied:
                return 
        except IndexError:
            print("Can't move past the parking lot")
            return

        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)
        
        self.parking_spaces[start_space[0]][start_space[1]].occupied = False 
        self.parking_spaces[end_space[0]][end_space[1]].occupied = True 

    def move_left(self):
        start_space = (self.col, self.row)
        end_space = (self.col - 1, self.row)
        distance = self.parking_space_width / 50
        try:
            if self.parking_spaces[end_space[0]][end_space[1]].occupied:
                return 
        except IndexError:
            print("Can't move past the parking lot")
            return

        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)
        
        self.parking_spaces[start_space[0]][start_space[1]].occupied = False 
        self.parking_spaces[end_space[0]][end_space[1]].occupied = True 

    def move_right(self):
        start_space = (self.col, self.row)
        end_space = (self.col + 1, self.row)
        distance = self.parking_space_width / 50
        try:
            if self.parking_spaces[end_space[0]][end_space[1]].occupied:
                return 
        except IndexError:
            print("Can't move past the parking lot")
            return


        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)
        
        self.parking_spaces[start_space[0]][start_space[1]].occupied = False 
        self.parking_spaces[end_space[0]][end_space[1]].occupied = True 
        
    def move_to_depot(self):
        for parking_column in self.parking_spaces:
            for parking_space in parking_column:
                print(parking_space.occupied)
        self.parking_lot.pathfindToDepot(self.col, self.row, [], self.parking_lot.mapParkingLot())
        self.parking_lot.animateToDepot()
        
        
