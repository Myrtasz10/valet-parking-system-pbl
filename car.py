from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtCore import QVariantAnimation, QPointF

class Car(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setBrush(QColor('red'))

    def animate(self, start_space, end_space, cell_size, speed, distance):
        # Calculate time
        time = float(distance) / float(speed)
        time *= 1000  # Convert to milliseconds
        time = int(time)

        start_x = (start_space[1] * cell_size) + (cell_size - self.rect().width()) / 2
        start_y = (start_space[0] * cell_size) + (cell_size - self.rect().height()) / 2
        end_x = (end_space[1] * cell_size) + (cell_size - self.rect().width()) / 2
        end_y = (end_space[0] * cell_size) + (cell_size - self.rect().height()) / 2

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

