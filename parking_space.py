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
    


# def heuristic(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# def move_car_to_destination(parking_spaces, start, goal):
#     cols, rows = len(parking_spaces), len(parking_spaces[0])
    
#     pq = [(0, start)]
#     costs = {start: 0}
#     came_from = {start: None}
    
#     while pq:
#         current_cost, current = heapq.heappop(pq)
        
#         if current == goal:
#             break
            
#         neighbors = [(current[0] + dx, current[1] + dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]]
#         neighbors = [(col, row) for col, row in neighbors if 0 <= col < cols and 0 <= row < rows]
        
#         for neighbor in neighbors:
#             new_cost = current_cost + 1
            
#             if neighbor not in costs or new_cost < costs[neighbor]:
#                 if not parking_spaces[neighbor[0]][neighbor[1]].occupied or neighbor == goal:
#                     costs[neighbor] = new_cost
#                     priority = new_cost + heuristic(goal, neighbor)
#                     heapq.heappush(pq, (priority, neighbor))
#                     came_from[neighbor] = current
                    
#     if goal not in came_from:
#         return "Path not found"

#     # Reconstruct the path
#     current = goal
#     path = []
#     while current is not None:
#         path.append(current)
#         current = came_from[current]
#     path.reverse()
    
#     # Perform the moves
#     for from_pos, to_pos in zip(path[:-1], path[1:]):
#         from_col, from_row = from_pos
#         to_col, to_row = to_pos
#         car = parking_spaces[from_col][from_row].car

#         if to_col > from_col:
#             car.move_right()
#         elif to_col < from_col:
#             car.move_left()
#         elif to_row > from_row:
#             car.move_down()
#         elif to_row < from_row:
#             car.move_up()

#     return "Car moved successfully"