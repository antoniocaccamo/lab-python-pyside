import logging
import __future__

from PySide6.QtWidgets import QWidget


class BaseWidget(QWidget):

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
