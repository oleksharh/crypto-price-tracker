import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ui/interface_main_window.ui", self)
        self.populate_menu()
    
    def populate_menu(self):
        menu_layout = self.menu_widget.layout()
        
        for i in range(1, 51):
            button = QPushButton(f"Label {i}", self)
            menu_layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
