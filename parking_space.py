from PyQt5.QtGui import QColor, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsRectItem
import heapq

class ParkingSpace(QGraphicsRectItem):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.setPen(QPen(QColor(Qt.black)))
        self.setAcceptHoverEvents(True)
        self.occupied = False
        self.car = None 

    def hoverEnterEvent(self, event):
        self.setPen(QPen(QColor('#333333'), 2))

    def hoverLeaveEvent(self, event):
        self.setPen(QPen(QColor('#000000'), 1))

class ParkingSpaceSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ParkingSpaceSingleton, cls).__new__(cls)
            cls._instance.parking_spaces = []
        return cls._instance