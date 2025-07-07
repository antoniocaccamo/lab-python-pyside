from __future__ import annotations
from preferences import Setting

from PySide6.QtGui import QIcon

from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QCheckBox, QTabWidget, QPushButton, QHBoxLayout, \
    QGroupBox, QFormLayout, QLabel, QSpinBox, QProgressBar, QComboBox

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot)

from ui.basewidget import BaseWidget
from ui.screenwindow import ScreenWindow


class SettingWidget(BaseWidget):
    """

    """
    _setting: Setting

    def __init__(self, parent: QWidget, setting: Setting):
        super().__init__(parent)
        self._setting = setting

        layout = QVBoxLayout()
        

        # widget = QWidget(self)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        
        #widget.setLayout(QVBoxLayout())
        self.setContentsMargins(0, 0, 0, 0)
        # lock checkbox
        self.checkbox_lock = QCheckBox(self)
        
        self.checkbox_lock.setText("Lock")
        self.checkbox_lock.setIcon(QIcon(":/icons/lock.png"))
        layout.addWidget(self.checkbox_lock)
        # 
        self.setting_tab_widget = QTabWidget(self)

        self.setting_tab_widget.setObjectName(u"setting_tab_widget")
        self.setting_tab_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        self.checkbox_lock.checkStateChanged.connect(lambda state: self.setting_tab_widget.setEnabled(   False if state ==  Qt.CheckState.Checked else True  ))
        self.setting_tab_widget.addTab(self.defineMediaPlaylistTab(), "Media Playlist")
        self.setting_tab_widget.addTab(self.defineTimingTab(), "Timing")
        self.setting_tab_widget.addTab(self.defineSizeDimensionsTab(), self.tr("Size & Dimensions"))
        layout.addWidget(self.setting_tab_widget)

        self.setLayout(layout)
        
        self.button_play.setDown(True) 
        self.button_stop.setDown(True)

        self.setLayout(layout)

        # self.setupUi()

        self.window = ScreenWindow(parent=None, index=self._setting.index)
        self.window.setGeometry(
            self._setting.position.left, self._setting.position.top,
            self._setting.size.width, self._setting.size.height
        )
        self.window.media_progess.connect(self.on_media_progress)

        self.window.setWindowTitle(f"Video Window {self._setting.index + 1}")
        self.window.show()
        self.start()

    def start(self) -> None:
        self.window.playList = self._setting.playlist
        self.window.start()

    # @DeprecationWarning
    # def setupUi(self):
    #     sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(0)
    #     sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
    #     self.setSizePolicy(sizePolicy)
    #     self.setMaximumSize(QSize(856, 709))
    #     self.verticalLayout = QVBoxLayout()
    #     self.verticalLayout.setObjectName(u"verticalLayout")
    #     self.widget = QWidget(self)
    #     self.widget.setObjectName(u"widget")
    #     self.verticalLayout_3 = QVBoxLayout(self.widget)
    #     self.verticalLayout_3.setObjectName(u"verticalLayout_3")
    #     self.lock_checkbox = QCheckBox(self.widget)
    #     self.lock_checkbox.setObjectName(u"lock_checkbox")
    #     sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    #     sizePolicy1.setHorizontalStretch(0)
    #     sizePolicy1.setVerticalStretch(1)
    #     sizePolicy1.setHeightForWidth(self.lock_checkbox.sizePolicy().hasHeightForWidth())
    #     self.lock_checkbox.setSizePolicy(sizePolicy1)
     
    #     self.lock_checkbox.setIcon(QIcon(":/icons/lock.png"))

    #     self.verticalLayout_3.addWidget(self.lock_checkbox)

    #     self.setting_tab_widget = QTabWidget(self.widget)
    #     self.setting_tab_widget.setObjectName(u"setting_tab_widget")
    #     self.setting_tab_widget.setEnabled(True)
    #     sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
    #     sizePolicy2.setHorizontalStretch(0)
    #     sizePolicy2.setVerticalStretch(0)
    #     sizePolicy2.setHeightForWidth(self.setting_tab_widget.sizePolicy().hasHeightForWidth())
    #     self.setting_tab_widget.setSizePolicy(sizePolicy2)
    #     self.tab_1 = QWidget()
    #     self.tab_1.setObjectName(u"tab_1")
    #     self.verticalLayout_2 = QVBoxLayout(self.tab_1)
    #     self.verticalLayout_2.setObjectName(u"verticalLayout_2")
    #     self.widget_3 = QWidget(self.tab_1)
    #     self.widget_3.setObjectName(u"widget_3")
    #     self.verticalLayout_5 = QVBoxLayout(self.widget_3)
    #     self.verticalLayout_5.setObjectName(u"verticalLayout_5")
    #     self.playlist_widget = QWidget(self.widget_3)
    #     self.playlist_widget.setObjectName(u"playlist_widget")
    #     self.formLayout_3 = QFormLayout(self.playlist_widget)
    #     self.formLayout_3.setObjectName(u"formLayout_3")
    #     self.label_5 = QLabel(self.playlist_widget)
    #     self.label_5.setObjectName(u"label_5")

    #     self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

    #     self.comboBox = QComboBox(self.playlist_widget)
    #     self.comboBox.setObjectName(u"comboBox")
    #     self.comboBox.setMaximumSize(QSize(103, 32))

    #     self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox)

    #     self.verticalLayout_5.addWidget(self.playlist_widget)

    #     self.button_widget = QWidget(self.widget_3)
    #     self.button_widget.setObjectName(u"button_widget")
    #     self.horizontalLayout_2 = QHBoxLayout(self.button_widget)
    #     self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
    #     self.pushButton = QPushButton(self.button_widget)
    #     self.pushButton.setObjectName(u"pushButton")
        
    #     self.pushButton.setIcon(QIcon(":/icons/play.png"))
    #     self.pushButton.setCheckable(False)
    #     self.pushButton.setFlat(False)

    #     self.horizontalLayout_2.addWidget(self.pushButton)

    #     self.pushButton_2 = QPushButton(self.button_widget)
    #     self.pushButton_2.setObjectName(u"pushButton_2")
    #     icon2 = QIcon()
    #     icon2.addFile(u":/icons/pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    #     self.pushButton_2.setIcon(icon2)

    #     self.horizontalLayout_2.addWidget(self.pushButton_2)

    #     self.pushButton_3 = QPushButton(self.button_widget)
    #     self.pushButton_3.setObjectName(u"pushButton_3")
    #     icon3 = QIcon()
    #     icon3.addFile(u":/icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
    #     self.pushButton_3.setIcon(icon3)

    #     self.horizontalLayout_2.addWidget(self.pushButton_3)

    #     self.verticalLayout_5.addWidget(self.button_widget)

    #     self.groupBox_4 = QGroupBox(self.widget_3)
    #     self.groupBox_4.setObjectName(u"groupBox_4")

    #     self.verticalLayout_5.addWidget(self.groupBox_4)

    #     self.progressbar_media = QProgressBar(self.widget_3)
    #     self.progressbar_media.setObjectName(u"media_progressbar")
    #     self.progressbar_media.setValue(24)

    #     self.verticalLayout_5.addWidget(self.progressbar_media)

    #     self.verticalLayout_2.addWidget(self.widget_3)

    #     self.setting_tab_widget.addTab(self.tab_1, "")
    #     self.tab_2 = QWidget()
    #     self.tab_2.setObjectName(u"tab_2")
    #     self.setting_tab_widget.addTab(self.tab_2, "")
    #     self.tab_3 = QWidget()
    #     self.tab_3.setObjectName(u"tab_3")
    #     self.verticalLayout_4 = QVBoxLayout(self.tab_3)
    #     self.verticalLayout_4.setObjectName(u"verticalLayout_4")
    #     self.widget1 = QWidget(self.tab_3)
    #     self.widget1.setObjectName(u"widget1")
    #     self.horizontalLayout = QHBoxLayout(self.widget1)
    #     self.horizontalLayout.setObjectName(u"horizontalLayout")
    #     self.groupBox_2 = QGroupBox(self.widget1)
    #     self.groupBox_2.setObjectName(u"groupBox_2")
    #     self.formLayout = QFormLayout(self.groupBox_2)
    #     self.formLayout.setObjectName(u"formLayout")
    #     self.label = QLabel(self.groupBox_2)
    #     self.label.setObjectName(u"label")

    #     self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

    #     self.spinBox = QSpinBox(self.groupBox_2)
    #     self.spinBox.setObjectName(u"spinBox")

    #     self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox)

    #     self.label_2 = QLabel(self.groupBox_2)
    #     self.label_2.setObjectName(u"label_2")

    #     self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

    #     self.spinBox_2 = QSpinBox(self.groupBox_2)
    #     self.spinBox_2.setObjectName(u"spinBox_2")

    #     self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2)

    #     self.horizontalLayout.addWidget(self.groupBox_2)

    #     self.groupBox = QGroupBox(self.widget1)
    #     self.groupBox.setObjectName(u"groupBox")
    #     self.formLayout_2 = QFormLayout(self.groupBox)
    #     self.formLayout_2.setObjectName(u"formLayout_2")
    #     self.label_4 = QLabel(self.groupBox)
    #     self.label_4.setObjectName(u"label_4")

    #     self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

    #     self.spinBox_3 = QSpinBox(self.groupBox)
    #     self.spinBox_3.setObjectName(u"spinBox_3")

    #     self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_3)

    #     self.label_3 = QLabel(self.groupBox)
    #     self.label_3.setObjectName(u"label_3")

    #     self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

    #     self.spinBox_4 = QSpinBox(self.groupBox)
    #     self.spinBox_4.setObjectName(u"spinBox_4")

    #     self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_4)

    #     self.horizontalLayout.addWidget(self.groupBox)

    #     self.verticalLayout_4.addWidget(self.widget1)

    #     self.setting_tab_widget.addTab(self.tab_3, "")

    #     self.verticalLayout_3.addWidget(self.setting_tab_widget)

    #     self.verticalLayout.addWidget(self.widget)

    #     self.retranslate_ui()

    #     self.setting_tab_widget.setCurrentIndex(0)


    def defineMediaPlaylistTab(self) -> QWidget:
        widget = QWidget(self.setting_tab_widget)
        widget.setObjectName("tab_media_playlist")
        widget.setLayout(QVBoxLayout())
        widget.layout().setContentsMargins(0, 0, 0, 0)

        grpbox_buttons = QGroupBox(title="Controls")
        grpbox_buttons.setLayout(QHBoxLayout())
        widget.layout().addWidget(grpbox_buttons)

        self.button_play = QPushButton("", grpbox_buttons)
        self.button_play.setIcon(QIcon(":/icons/play.png"))
        self.button_pause = QPushButton("Pause", grpbox_buttons)
        self.button_pause.setIcon(QIcon(":/icons/pause.png"))
        self.button_stop = QPushButton("Stop", grpbox_buttons)
        self.button_stop.setIcon(QIcon(":/icons/stop.png"))
        grpbox_buttons.layout().addWidget(self.button_play)
        grpbox_buttons.layout().addWidget(self.button_pause)
        grpbox_buttons.layout().addWidget(self.button_stop)

        grpbox_current_media = QGroupBox( title="Current Media")
        grpbox_current_media.setWindowTitle("media")
        grpbox_current_media.setLayout(QVBoxLayout())
        widget.layout().addWidget(grpbox_current_media)

        self.progressbar_media = QProgressBar(grpbox_current_media, minimum=0, maximum=100)
        self.progressbar_media.setValue(0)
        grpbox_current_media.layout().addWidget(self.progressbar_media)

         
        
        return widget
    
    def defineTimingTab(self) -> QWidget:
        widget = QWidget(self.setting_tab_widget)
        widget.setObjectName("tab_timing")
        widget.setLayout(QVBoxLayout())
        widget.layout().setContentsMargins(0, 0, 0, 0)
        return widget

    def defineSizeDimensionsTab(self) -> QWidget:
        widget = QWidget(self.setting_tab_widget)
        widget.setObjectName("tab_size_dimensions")
        widget.setLayout(QVBoxLayout())
        widget.layout().setContentsMargins(0, 0, 0, 0)
        return widget
    # defineSizeDimensionsTab


    @Slot(float)
    def on_media_progress(self, progress: float):
        self.logger.debug(f"{self} progress  {progress:0.2f}  ")
        self.progressbar_media.setValue(progress)

    def __str__(self):
        return f"setting window {self._setting.index + 1}:"
