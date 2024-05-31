import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random
import datetime

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Live Crypto Chart')
        self.canvas = MplCanvas()
        self.setCentralWidget(self.canvas)

        self.x = []
        self.y = []

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        # In a real scenario, you would fetch data from an API here
        # response = requests.get('https://api.ton.org/data/crypto')
        # data = response.json()
        # timestamp = data['timestamp']
        # value = data['value']

        # For demonstration purposes, we'll generate random data
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        value = random.uniform(0, 10)

        self.x.append(current_time)
        self.y.append(value)

        self.canvas.ax.clear()
        self.canvas.ax.plot(self.x, self.y, 'r')

        # Setting the labels
        self.canvas.ax.set_xlabel('Time')
        self.canvas.ax.set_ylabel('Price')
        self.canvas.ax.set_title('Live Crypto Price')

        # Rotate the x-tick labels for better readability
        self.canvas.ax.tick_params(axis='x', rotation=45)

        # Adjust the layout to fit everything
        self.canvas.figure.tight_layout()

        self.canvas.draw()


app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
