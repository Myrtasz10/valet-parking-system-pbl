from PyQt5.QtGui import QColor, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsRectItem

class ParkingSpace(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setPen(QPen(QColor(Qt.black)))
        self.setAcceptHoverEvents(True)  # Enable hover events

    def hoverEnterEvent(self, event):
        self.setPen(QPen(QColor('#333333'), 2))

    def hoverLeaveEvent(self, event):
        self.setPen(QPen(QColor('#000000'), 1))
