from PySide6.QtWidgets import QWidget

from media.MediaTypeEnum import MediaTypeEnum
from players import BasePlayerWidget


class HiddenPlayerWidget(BasePlayerWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Hidden)
        pass
