from stopwatch import Stopwatch, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import sys
from time import sleep

class Worker(QThread):
    finish_signal = pyqtSignal()
    def run(self):
        # Insert the solution here
        for i in range(10):
            sleep(1)
            print(i)
        
        self.finish_signal.emit()
        
            

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

