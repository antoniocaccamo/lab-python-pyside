import os
import sys

# from colorwidget import QColor
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from ui import MainWindow

props = {}
from containers import Container

if __name__ == "__main__":
    # Ensure the script is run from the correct directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.dirname(os.path.relpath(__file__))
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(path, "./images/playlist.png")))
    window = MainWindow()
    window.show()
    app.exec()
