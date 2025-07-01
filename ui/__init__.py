


# import logging
# from typing import List, Dict
#
# from PySide6.QtCore import Slot, Signal
# from PySide6.QtGui import QAction
# from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMainWindow, QTabWidget, QSystemTrayIcon, QMenu, \
#     QApplication, QProgressBar, QGroupBox, QStackedLayout
# from dependency_injector.wiring import Provide
#
# from containers import Container
# from media import BaseMedia, WatchMedia, MediaTypeEnum
# from preferences import Setting
# from services import PreferenceService
# from ui.players import BasePlayerWidget, DigitalClockPlayerWidget, BlackPlayerWidget, HiddenPlayerWidget, \
#     PhotoPlayerWidget, VideoPlayerWidget, WebPlayerWidget
#
#
# class BaseWidget(QWidget):
#
#     def __init__(self, parent: QWidget ):
#         super().__init__(parent)
#         self.logger = logging.getLogger(
#             f"{__name__}.{self.__class__.__name__}",
#         )
#
#
# class ScreenWindow(BaseWidget):
#     """
#     This "window" is a QWidget. If it has no parent, it
#     will appear as a free-floating window as we want.
#     """
#     _index = 0
#     _current_player_widget: BasePlayerWidget
#     _current_media: BaseMedia
#     _screenWidgets: Dict[MediaTypeEnum, BasePlayerWidget]
#
#     media_progess = Signal(float)
#
#     def __init__(self, parent: QWidget, index: int = 0):
#         super().__init__(parent)
#         layout = QStackedLayout()
#         layout.setStackingMode(QStackedLayout.StackingMode.StackOne)
#         self.setLayout(layout)
#         self._index = index
#         self.setWindowTitle(f"{self}")
#
#         self._screenWidgets = {
#             MediaTypeEnum.Black: BlackPlayerWidget(self),
#             MediaTypeEnum.Hidden: HiddenPlayerWidget(self),
#             MediaTypeEnum.Watch: DigitalClockPlayerWidget(self),
#             MediaTypeEnum.Photo: PhotoPlayerWidget(self),
#             MediaTypeEnum.Video: VideoPlayerWidget(self),
#             MediaTypeEnum.Web : WebPlayerWidget(self)
#         }
#         # self._current_player_widget = clock
#         for wdgt in self._screenWidgets.values():
#             self.layout().addWidget(wdgt)
#         self._current_media = WatchMedia()
#         self._current_media.duration = 5.0
#         self.logger.info(f"{self} created ")
#
#         self.play()
#
#     def __str__(self):
#         return f"window {self._index + 1}:"
#
#     def play(self) -> None:
#         self.logger.info(f"{self} playing  [{self._current_media}] ")
#         self.layout().setCurrentIndex(self._current_media.media_type.value)
#         self._current_player_widget = self.layout().currentWidget()
#
#         self._current_player_widget.media_progess.connect(self.on_media_progress)
#         self._current_player_widget.media_ended.connect(self.next)
#         self.media_progess.emit(0)
#         self._current_player_widget.play(self._current_media)
#
#     def next(self):
#         self.logger.info(f"{self} ended    [{self._current_media}]")
#         self._current_player_widget.media_progess.disconnect()
#         self._current_player_widget.media_ended.disconnect()
#         self.play()
#
#     @Slot(float)
#     def on_media_progress(self, progress: float):
#         self.logger.debug(f"{self} progress [{self._current_media}]: {progress:0.2f} / {self._current_media.duration:0.2f} ")
#         self.media_progess.emit(progress * 100 / self._current_media.duration)
#
#
# class SettingWidget(BaseWidget):
#     """
#
#     """
#     _setting: Setting
#
#     def __init__(self, parent: QWidget, setting: Setting):
#         super().__init__(parent)
#         self._setting = setting
#         layout = QVBoxLayout()
#         self.label = QLabel(f"{self}", self)
#         grop_box = QGroupBox(self, title="Current Media")
#         grop_box.setWindowTitle("media")
#         grop_box.setLayout(QVBoxLayout())
#         self.progress_bar = QProgressBar(grop_box, minimum=0, maximum=100)
#         grop_box.layout().addWidget(self.progress_bar)
#         self.progress_bar.setValue(0)
#         layout.addWidget(self.label)
#         layout.addWidget(grop_box)
#         self.setLayout(layout)
#         self.window = ScreenWindow(parent=None, index=self._setting.index)
#         self.window.setGeometry(
#             self._setting.position.left, self._setting.position.top,
#             self._setting.size.width, self._setting.size.height
#         )
#         self.window.media_progess.connect(self.on_media_progress)
#         self.window.show()
#
#     @Slot(float)
#     def on_media_progress(self, progress: float):
#         self.logger.debug(f"{self} progress  {progress:0.2f}  ")
#         self.progress_bar.setValue(progress)
#
#     def __str__(self):
#         return f"setting window {self._setting.index + 1}:"
#
#
# class MainWindow(QMainWindow):
#     """
#     Main UI Window
#     """
#
#     _listOfSettingWidgets: List[SettingWidget] = list()
#
#     def __init__(self, preferenceService: PreferenceService = Provide[Container.preference_service]):
#         super().__init__()
#         self.logger = logging.getLogger(
#             f"{__name__}.{self.__class__.__name__}",
#         )
#         self.logger.info(f"creating {self.__class__.__name__}")
#         pref = preferenceService.preference
#         self.setWindowTitle(pref.computer_name)
#         self.setGeometry(
#             pref.position.left, pref.position.top,
#             pref.size.width, pref.size.height
#         )
#         tabs = QTabWidget()
#         tabs.setTabPosition(QTabWidget.North)
#         tabs.setMovable(True)
#
#         for setting in pref.settings:
#             title = f"Video Window {setting.index + 1}"
#             wdg = SettingWidget(tabs, setting)
#             tabs.addTab(wdg, title)
#             self._listOfSettingWidgets.append(wdg)
#
#         self.setCentralWidget(tabs)
#         self.destroyed.connect(self.closeEvent)
#
#         system_tray = QSystemTrayIcon(self)
#         menu = QMenu()
#         # Create quit button
#         btn_quit = QAction('Quit', self)
#         btn_quit.triggered.connect(QApplication.quit)
#         # Add buttons to menu
#         menu.addAction(btn_quit)
#         system_tray.setIcon(self.windowIcon())
#         system_tray.setContextMenu(menu)
#         system_tray.setVisible(True)
#
#     @Slot()
#     def closeEvent(self, event):
#         for setting in self._listOfSettingWidgets:
#             setting.window.close()
#         event.accept()
#         self.logger.info("app closed")