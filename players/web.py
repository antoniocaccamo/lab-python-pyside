from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QLCDNumber, QWidget, QVBoxLayout, QLabel

from media.MediaTypeEnum import MediaTypeEnum
from players import BasePlayerWidget


class WebPlayerWidget(BasePlayerWidget):
    """

    """
    __wiew : QWebEngineView

    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Web)
        self.setLayout(QVBoxLayout())
        self.__wiew = QWebEngineView(self)
        self.layout().addWidget(self.__wiew)


    def play(self, media):
        self.__wiew.load(QUrl(media.local_path()))
        super().play(media)