import datetime
import logging
from shutil import which

from PySide6.QtCore import Slot, QTimer, QTime, Signal
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLCDNumber

from media import BaseMedia, MediaTypeEnum


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
        self._timer.start(200)
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
        if self._pausedAt is not None:
            elapsed += self._pausedAt
        # self.logger.info( f"progress {elapsed.total_seconds():0.2f} / {self._current_media.duration:0.2f} ")
        self.media_progess.emit(elapsed.total_seconds())
        if (elapsed.total_seconds() > self._current_media.duration):
            self.next()


class BlackPlayerWidget(BasePlayerWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Black)
        pass


class HiddenPlayerWidget(BasePlayerWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Hidden)
        pass


class PhotoPlayerWidget(BasePlayerWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent, MediaTypeEnum.Photo)
        pass

class VideoPlayerWidget(BasePlayerWidget):
    """

    """
    _player : QMediaPlayer
    #_vout : QVideoWidget

    def __init__(self, parent: QWidget = None):
        super().__init__(parent, MediaTypeEnum.Video)
        self.setLayout(QVBoxLayout())
        vout = QVideoWidget(self)
        self.layout().addWidget(vout)
        self._player = QMediaPlayer()
        self._player.setVideoOutput(vout)
        self._player.mediaStatusChanged.connect(self._onMediaStatusChanged)
        self._player.errorOccurred.connect(self._onErrorOccurred)

    @Slot()
    def _onErrorOccurred(self):
        pass

    @Slot()
    def _onMediaStatusChanged(self):
        match self._player.mediaStatusChanged:
            case 1:
                self.logger.debug("loading")
            case _ :
                self.logger.debug("media status changed to %s", self._player.mediaStatus())

    @Slot()
    def _onPlaybackStateChanged(self):
        self._player.playbackState()

class WebPlayerWidget(BasePlayerWidget):
    """
    
    """
    
    def __init__(self, parent: QWidget):
        super().__init__(parent, MediaTypeEnum.Web)
        pass


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
