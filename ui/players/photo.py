from PySide6.QtWidgets import QWidget

from media import MediaTypeEnum
from ui.players.base import BasePlayerWidget


class PhotoPlayerWidget(BasePlayerWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, MediaTypeEnum.Photo)
        pass
