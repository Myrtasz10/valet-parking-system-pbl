from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsRectItem, QMenu, QAction
from PyQt5.QtCore import QVariantAnimation, QPointF, QPoint
from PyQt5.QtCore import QObject, pyqtSignal
from parking_space import ParkingSpace, ParkingSpaceSingleton

class Car(QGraphicsRectItem):
    settingDestinationSignal = pyqtSignal(object) 

    def __init__(self, col, row, width, height, speed):
        self.parking_space_width = width + 10
        self.parking_space_height = height + 10

        self.col = col
        self.row = row

        start_x = col * self.parking_space_width + 5
        start_y = row * self.parking_space_height + 5

        super().__init__(start_x, start_y, width, height)

        singleton = ParkingSpaceSingleton()
        self.parking_spaces = singleton.parking_spaces

        self.setBrush(QColor('#ff0000'))
        self.setAcceptHoverEvents(True)
        self.speed = speed


    def hoverEnterEvent(self, event):
        self.setBrush(QColor('#cc0000'))

    def hoverLeaveEvent(self, event):
        self.setBrush(QColor('#ff0000'))

    def contextMenuEvent(self, event):
        contextMenu = QMenu()
        
        moveMenu = QMenu('Move', contextMenu)
        moveUp = QAction('↑', moveMenu)
        moveDown = QAction('↓', moveMenu)
        moveLeft = QAction('←', moveMenu)
        moveRight = QAction('→', moveMenu)
        
        moveUp.triggered.connect(self.move_up)
        moveDown.triggered.connect(self.move_down)
        moveLeft.triggered.connect(self.move_left)
        moveRight.triggered.connect(self.move_right)
        
        moveMenu.addAction(moveUp)
        moveMenu.addAction(moveDown)
        moveMenu.addAction(moveLeft)
        moveMenu.addAction(moveRight)
        
        contextMenu.addMenu(moveMenu)
        
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

    def move_up(self):
        start_space = (self.col, self.row)
        end_space = (self.col, self.row - 1)
        distance = self.parking_space_height / 50

        if self.parking_spaces[end_space[0]][end_space[1]].occupied:
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

        if self.parking_spaces[end_space[0]][end_space[1]].occupied:
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

        if self.parking_spaces[end_space[0]][end_space[1]].occupied:
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

        if self.parking_spaces[end_space[0]][end_space[1]].occupied:
            return 


        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)
        
        self.parking_spaces[start_space[0]][start_space[1]].occupied = False 
        self.parking_spaces[end_space[0]][end_space[1]].occupied = True 
