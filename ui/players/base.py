import datetime

import logging
from PySide6.QtCore import QTimer, Signal, Slot
from PySide6.QtWidgets import QWidget

from media import MediaTypeEnum, BaseMedia


class BasePlayerWidget(QWidget):
    """

    """

    _duration: float
    _timer: QTimer
    _startedAt: datetime.datetime
    _pausedAt: datetime.datetime
    _player_for: MediaTypeEnum
    _current_media: BaseMedia

    media_progess = Signal(float)
    media_ended = Signal()

    def __init__(self, parent: QWidget, player_for: MediaTypeEnum):
        super().__init__(parent)
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
        self._player_for = player_for
        self._timer = QTimer()

    def play(self, media: BaseMedia):
        assert media is not None
        self._reset()
        self._current_media = media
        self._startedAt = datetime.datetime.now()
        self._timer.timeout.connect(self._tick)
        self._timer.setInterval(500)  # 1 second interval
        self._timer.start(0)

        pass

    def pause(self):
        self._pausedAt = datetime.datetime.now()
        pass

    def stop(self):
        self._reset()
        pass

    def next(self):
        self._timer.stop()
        self.media_ended.emit()
        pass

    def _reset(self):
        self._startedAt = None
        self._pausedAt = None

    @Slot()
    def _tick(self):
        elapsed: datetime.timedelta = datetime.datetime.now() - self._startedAt
        if self._pausedAt is not None :
            elapsed += self._pausedAt
        # self.logger.info( f"progress {elapsed.total_seconds():0.2f} / {self._current_media.duration:0.2f} ")
        self.media_progess.emit(elapsed.total_seconds())
        if (elapsed.total_seconds() > self._current_media.duration):
            self.next()
