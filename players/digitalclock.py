import datetime

from PySide6.QtCore import QTimer, Slot, QTime
from PySide6.QtWidgets import QLCDNumber, QWidget, QVBoxLayout

from media.MediaTypeEnum import MediaTypeEnum
from players import BasePlayerWidget


class DigitalClockPlayerWidget(BasePlayerWidget):
    """

    """

    _date: QLCDNumber
    _time: QLCDNumber
    _lcd_timer = QTimer()

    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Watch)
        self.setLayout(QVBoxLayout())
        self._date = QLCDNumber(self)
        self._date.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self._date.setDigitCount(10)
        self._time = QLCDNumber(self)
        self._time.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self._time.setDigitCount(8)

        self.layout().addWidget(self._time)
        self.layout().addWidget(self._date)

        self._lcd_timer.timeout.connect(self._show_time)
        self._lcd_timer.start(1000)

        self._show_time()

        self.destroyed.connect(lambda: self.logger.info("destroying"))

    @Slot()
    def _show_time(self):
        now = datetime.datetime.now()
        time = QTime.currentTime()
        text = now.strftime("%H:%M:%S")

        # Blinking effect
        if (time.second() % 2) == 0:
            text = text.replace(":", " ")
        self._date.display(now.strftime("%d-%m-%Y"))
        self._time.display(text)
