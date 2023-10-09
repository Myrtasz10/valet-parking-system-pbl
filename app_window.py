import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

class TableExample:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        table_widget = QTableWidget()

        # Set the number of rows and columns
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)
        
        cell_size = 100
        
        for i in range(3):
            table_widget.setColumnWidth(i, cell_size)
            table_widget.setRowHeight(i, cell_size)

        # Populate the table with items (rectangular cells)
        for i in range(3):
            for j in range(3):
                item = QTableWidgetItem()
                table_widget.setItem(i, j, item)

        layout.addWidget(table_widget)
        self.window.setLayout(layout)  # Set the layout for the main window
        self.window.setWindowTitle("3x3 Table Example")

    def run(self):
        self.window.show()
        self.app.exec_()