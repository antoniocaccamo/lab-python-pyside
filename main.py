import os
import sys

# from colorwidget import QColor
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QLibraryInfo, QTranslator, QLocale

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

    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = ':/translations'
    #if translator.load(QLocale.system(), 'example', '_', path):
    app.installTranslator(translator)
    app.setApplicationName("PyPlayer")
    app.setApplicationVersion("0.1.0")
    app.setWindowIcon(QIcon(":/icons/pyplayer.ico"))
    window = MainWindow()
    window.show()
    app.exec()
