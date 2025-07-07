from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLCDNumber, QWidget, QVBoxLayout, QLabel

from media import MediaTypeEnum
from players import BasePlayerWidget


class PhotoPlayerWidget(BasePlayerWidget):

    """
    PhotoPlayerWidget is a widget for displaying photo content.
    It is designed to show a simple label indicating that it is a photo player.
    """

    def __init__(self, parent: QWidget = None):
        super().__init__(parent, MediaTypeEnum.Photo)
        self.setLayout(QVBoxLayout())
        lbl = QLabel("Photo Player", self)
        lbl.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(lbl)
