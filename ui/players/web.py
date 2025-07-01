from PySide6.QtWidgets import QWidget

from media import MediaTypeEnum
from ui.players.base import BasePlayerWidget


class WebPlayerWidget(BasePlayerWidget):
    """

    """

    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Web)
        pass
