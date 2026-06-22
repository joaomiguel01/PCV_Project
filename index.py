from stopwatch import Stopwatch
from problem import random_array_problem
from method_3 import bellman_held_karp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import sys

class Worker(QThread):
    finish_signal = pyqtSignal()
    def run(self):
        # Setup problem
        array = random_array_problem(20)

        # Method
        best_way, total_cost = bellman_held_karp(array)
        self.finish_signal.emit()

        # Print Array
        for i in range(len(array)):
            print(array[i], '\n')

        print(f"\n\n\nThe best way:{best_way}\nTotal cost: {total_cost}")



if __name__ == "__main__":
    # Stopwatch
    app = QApplication(sys.argv)
    stop_watch = Stopwatch()
    stop_watch.show()

    # Thread
    worker = Worker()
    worker.finish_signal.connect(stop_watch.stop)

    # Workflow
    stop_watch.start()
    worker.start()

    sys.exit(app.exec_())

