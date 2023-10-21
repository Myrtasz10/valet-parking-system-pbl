from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsRectItem, QMenu, QAction
from PyQt5.QtCore import QVariantAnimation, QPointF, QPoint
from PyQt5.QtCore import QObject, pyqtSignal

class Car(QGraphicsRectItem):
    settingDestinationSignal = pyqtSignal(object) 

    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self.setBrush(QColor('#ff0000'))
        self.setAcceptHoverEvents(True)
        self.speed = speed
        self.parking_space_width = width + 10
        self.parking_space_height = height + 10

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
        
        setDestination = QAction('Set Destination')
        setDestination.triggered.connect(self.activateSetDestination)
        contextMenu.addAction(setDestination)
        
        contextMenu.exec_(event.screenPos())

    def activateSetDestination(self):
        self.setting_destination = True
        self.settingDestinationSignal.emit(self)  # Emit signal with self as argument
        print("Setting destination activated.")


    def moveToDestination(self, destination):
        dx = destination.x() * 100 - self.x()
        dy = destination.y() * 100 - self.y()
        moves_right = dx // 100
        moves_down = dy // 100

        for _ in range(abs(int(moves_right))):
            self.move_right() if moves_right > 0 else self.move_left()

        for _ in range(abs(int(moves_down))):
            self.move_down() if moves_down > 0 else self.move_up()

    def animate(self, start_space, end_space, 
                parking_space_width, parking_space_height, speed, distance):
        time = float(distance) / float(speed)
        time *= 1000
        time = int(time)

        start_x = start_space[1] * parking_space_width
        start_y = start_space[0] * parking_space_height
        end_x = end_space[1] * parking_space_width
        end_y = end_space[0] * parking_space_height

        self.animation = QVariantAnimation()
        self.animation.setDuration(time)
        self.animation.setStartValue(QPointF(start_x, start_y))
        self.animation.setEndValue(QPointF(end_x, end_y))
        self.animation.valueChanged.connect(self.setPos)
        self.animation.start()

    def move_up(self):
        start_space = (self.y() // self.parking_space_height, self.x() // self.parking_space_width)
        end_space = (start_space[0] - 1, start_space[1])
        distance = self.parking_space_height / 50

        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)

    def move_down(self):
        start_space = (self.y() // self.parking_space_height, self.x() // self.parking_space_width)
        end_space = (start_space[0] + 1, start_space[1])
        distance = self.parking_space_height / 50

        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)

    def move_left(self):
        start_space = (self.y() // self.parking_space_height, self.x() // self.parking_space_width)
        end_space = (start_space[0], start_space[1] - 1)
        distance = self.parking_space_width / 50

        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)

    def move_right(self):
        start_space = (self.y() // self.parking_space_height, self.x() // self.parking_space_width)
        end_space = (start_space[0], start_space[1] + 1)
        distance = self.parking_space_width / 50

        self.animate(start_space, 
                     end_space, 
                     self.parking_space_width,
                     self.parking_space_height, 
                     self.speed, distance)
