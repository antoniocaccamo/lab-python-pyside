import logging
from PySide6.QtCore import Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QApplication, QTabWidget)
from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from dependency_injector.wiring import Provide
from typing import List

import resources  # noqa: F401
from di import DIContainer
from services import PreferenceService
from ui import SettingWidget


class MainWindow(QMainWindow):
    """
    Main UI Window
    """

    _listOfSettingWidgets: List[SettingWidget] = list()

    def __init__(self, preferenceService: PreferenceService = Provide[DIContainer.preference_service]):
        super().__init__()
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
        self.logger.info(f"creating {self.__class__.__name__}")
        pref = preferenceService.preference
        self.setWindowTitle(pref.computer_name)
        self.setGeometry(
            pref.position.left, pref.position.top,
            pref.size.width, pref.size.height
        )
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for setting in pref.settings:
            tr  =self.tr("Video Window")
            title = f"{tr} {setting.index + 1}"
            wdg = SettingWidget(tabs, setting)
            tabs.addTab(wdg, title)
            self._listOfSettingWidgets.append(wdg)

        self.setCentralWidget(tabs)
        self.destroyed.connect(self.closeEvent)

        system_tray = QSystemTrayIcon(self)
        menu = QMenu()
        # Create quit button
        btn_quit = QAction('Quit', self)
        btn_quit.triggered.connect(QApplication.quit)
        # Add buttons to menu
        menu.addAction(btn_quit)
        system_tray.setIcon(self.windowIcon())
        system_tray.setContextMenu(menu)
        system_tray.setVisible(True)

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        file_menu = menu.addMenu("&File")
        file_menu.addAction(btn_quit)

    @Slot()
    def closeEvent(self, event):
        for setting in self._listOfSettingWidgets:
            setting.window.close()
        event.accept()
        self.logger.info("app closed")