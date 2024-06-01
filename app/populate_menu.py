import sys
import csv
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


# def load_stylesheet(filename):
#     with open(filename, "r") as f:
#         return f.read()
    
# stylesheet = load_stylesheet("styles/styles.css")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/interface_main_window.ui", self)
        self.populate_menu()

        # self.setStyleSheet(stylesheet)
    
    def populate_menu(self):
        menu_layout = self.menu_widget.layout()
        print(menu_layout)

        with open("ohlcv_data.csv", mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            i = 0
            for row in csv_reader:
                base_symbol, quote_symbol, open_price, high, low, close_price, volume, timestamp = row
                button = QPushButton(f"{base_symbol} / {quote_symbol} Price:{close_price}")

                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                price_label = QLabel(f"Price: {close_price}")
                menu_layout.addWidget(button, i, 0)
                menu_layout.addWidget(price_label, i, 1, alignment=Qt.AlignRight)
                i += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
