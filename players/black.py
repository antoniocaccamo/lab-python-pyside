from PySide6.QtWidgets import QWidget

from media import MediaTypeEnum
from players import BasePlayerWidget


class BlackPlayerWidget(BasePlayerWidget):
    """

    """

    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Black)
        pass
