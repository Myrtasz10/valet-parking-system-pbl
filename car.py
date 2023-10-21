from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsRectItem, QMenu, QAction
from PyQt5.QtCore import QVariantAnimation, QPointF, QPoint
from PyQt5.QtCore import QObject, pyqtSignal

class Car(QGraphicsRectItem):
    settingDestinationSignal = pyqtSignal(object) 

    def __init__(self, x, y, width, height):
        super(Car, self).__init__(x, y, width, height)
        self.setBrush(QColor('#ff0000'))
        self.setAcceptHoverEvents(True)
        self.setting_destination = False

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

    def animate(self, start_space, end_space, cell_size, speed, distance):
        time = float(distance) / float(speed)
        time *= 1000
        time = int(time)

        start_x = start_space[1] * cell_size
        start_y = start_space[0] * cell_size
        end_x = end_space[1] * cell_size
        end_y = end_space[0] * cell_size

        self.animation = QVariantAnimation()
        self.animation.setDuration(time)
        self.animation.setStartValue(QPointF(start_x, start_y))
        self.animation.setEndValue(QPointF(end_x, end_y))
        self.animation.valueChanged.connect(self.setPos)
        self.animation.start()

    def move_up(self):
        self.animate((self.y() // 100, self.x() // 100), ((self.y() - 100) // 100, self.x() // 100), 100, 1, 1)

    def move_down(self):
        self.animate((self.y() // 100, self.x() // 100), ((self.y() + 100) // 100, self.x() // 100), 100, 1, 1)

    def move_left(self):
        self.animate((self.y() // 100, self.x() // 100), (self.y() // 100, (self.x() - 100) // 100), 100, 1, 1)

    def move_right(self):
        self.animate((self.y() // 100, self.x() // 100), (self.y() // 100, (self.x() + 100) // 100), 100, 1, 1)
