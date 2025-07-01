from PySide6.QtCore import Slot
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout

from media import MediaTypeEnum
from ui.players.base import BasePlayerWidget


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
