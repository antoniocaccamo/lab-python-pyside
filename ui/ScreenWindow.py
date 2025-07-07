from __future__ import annotations

from PySide6.QtCore import Signal, Slot
from typing import Dict

from media.MediaPlaylist import MediaPlaylist


from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QStackedLayout, QWidget

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)


from media.BaseMedia import BaseMedia
from media.MediaTypeEnum import MediaTypeEnum
from media.WatchMedia import WatchMedia
from players import BasePlayerWidget, BlackPlayerWidget, DigitalClockPlayerWidget, \
    HiddenPlayerWidget, PhotoPlayerWidget, VideoPlayerWidget, WebPlayerWidget

from ui import BaseWidget

class ScreenWindow(BaseWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    _index = 0
    _current_player_widget: BaseWidget
    _current_media: BaseMedia
    _screenWidgets: Dict[MediaTypeEnum, BasePlayerWidget]
    _playList: MediaPlaylist = None

    media_progess = Signal(float)



    def __init__(self, parent: QWidget, index: int = 0):
        super().__init__(parent)
        layout = QStackedLayout()
        layout.setStackingMode(QStackedLayout.StackingMode.StackOne)
        self.setLayout(layout)
        self._index = index
        self.setWindowTitle(f"{self}")

        self._screenWidgets = {
            MediaTypeEnum.Black: BlackPlayerWidget(self),
            MediaTypeEnum.Hidden: HiddenPlayerWidget(self),
            MediaTypeEnum.Watch: DigitalClockPlayerWidget(self),
            MediaTypeEnum.Photo: PhotoPlayerWidget(self),
            MediaTypeEnum.Video: VideoPlayerWidget(self),
            MediaTypeEnum.Web: WebPlayerWidget(self)
        }
        # self._current_player_widget = clock
        for wdgt in self._screenWidgets.values():
            self.layout().addWidget(wdgt)
        self._current_media = WatchMedia()
        self._current_media.duration = 5.0
        self.logger.info(f"{self} created ")

    @property
    def playList(self) -> MediaPlaylist:
        return self._playList

    @playList.setter
    def playList(self, value: MediaPlaylist):
        self._playList = value
        
    
    def start(self) -> None:
        assert self._playList, "PlayList must be set before starting the player"
        self.logger.info(f"{self} starting with playlist: {self._playList}")
        self._current_media = self._playList.get_current_media()
        self.__play()

    def stop(self) -> None:
        pass

    def pause(self) -> None:
        pass

    def resume(self) -> None:
        pass

    
    def __play(self) -> None:
        self.logger.info(f"{self} playing  [{self._current_media}] ")
        self.layout().setCurrentIndex(self._current_media.media_type.value)
        self._current_player_widget = self.layout().currentWidget()

        self._current_player_widget.media_progess.connect(self.on_media_progress)
        self._current_player_widget.media_ended.connect(self.__next)
        self.media_progess.emit(0)
        self._current_player_widget.play(self._current_media)

    def __next(self):
        self.logger.info(f"{self} ended    [{self._current_media}]")
        self._current_player_widget.media_progess.disconnect()
        self._current_player_widget.media_ended.disconnect()
        self._current_media = self._playList.get_current_media()
        self.__play()

    def __str__(self):
        return f"window {self._index + 1}:"

    @Slot(float)
    def on_media_progress(self, progress: float):
        self.logger.debug(
            f"{self} progress [{self._current_media}]: {progress:0.2f} / {self._current_media.duration:0.2f} ")
        self.media_progess.emit(progress * 100 / self._current_media.duration)
