# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 595)
        MainWindow.setStyleSheet(u"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_frame_a = QFrame(self.header)
        self.header_frame_a.setObjectName(u"header_frame_a")
        self.header_frame_a.setFrameShape(QFrame.StyledPanel)
        self.header_frame_a.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.header_frame_a)

        self.header_frame_b = QFrame(self.header)
        self.header_frame_b.setObjectName(u"header_frame_b")
        self.header_frame_b.setFrameShape(QFrame.StyledPanel)
        self.header_frame_b.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.header_frame_b)

        self.header_frame_c = QFrame(self.header)
        self.header_frame_c.setObjectName(u"header_frame_c")
        self.header_frame_c.setFrameShape(QFrame.StyledPanel)
        self.header_frame_c.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.header_frame_c)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_frame_c)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lb_start = QLabel(self.frame)
        self.lb_start.setObjectName(u"lb_start")

        self.horizontalLayout.addWidget(self.lb_start)

        self.in_start = QLineEdit(self.frame)
        self.in_start.setObjectName(u"in_start")
        self.in_start.setFrame(True)

        self.horizontalLayout.addWidget(self.in_start)

        self.lb_count = QLabel(self.frame)
        self.lb_count.setObjectName(u"lb_count")

        self.horizontalLayout.addWidget(self.lb_count)

        self.in_count = QLineEdit(self.frame)
        self.in_count.setObjectName(u"in_count")

        self.horizontalLayout.addWidget(self.in_count)

        self.lb_combine = QLabel(self.frame)
        self.lb_combine.setObjectName(u"lb_combine")

        self.horizontalLayout.addWidget(self.lb_combine)

        self.in_combine = QLineEdit(self.frame)
        self.in_combine.setObjectName(u"in_combine")

        self.horizontalLayout.addWidget(self.in_combine)

        self.lb_check = QCheckBox(self.frame)
        self.lb_check.setObjectName(u"lb_check")

        self.horizontalLayout.addWidget(self.lb_check)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.header_frame_c)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.s_draw_img = QPushButton(self.frame_2)
        self.s_draw_img.setObjectName(u"s_draw_img")

        self.horizontalLayout_4.addWidget(self.s_draw_img)

        self.s_combine_audio = QPushButton(self.frame_2)
        self.s_combine_audio.setObjectName(u"s_combine_audio")

        self.horizontalLayout_4.addWidget(self.s_combine_audio)

        self.s_make_vid = QPushButton(self.frame_2)
        self.s_make_vid.setObjectName(u"s_make_vid")

        self.horizontalLayout_4.addWidget(self.s_make_vid)

        self.s_options = QPushButton(self.frame_2)
        self.s_options.setObjectName(u"s_options")
        self.s_options.setMaximumSize(QSize(19, 16777215))

        self.horizontalLayout_4.addWidget(self.s_options)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.header_frame_c)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.header)

        self.contents = QFrame(self.centralwidget)
        self.contents.setObjectName(u"contents")
        self.contents.setFrameShape(QFrame.StyledPanel)
        self.contents.setFrameShadow(QFrame.Raised)
        self.content_layout = QHBoxLayout(self.contents)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.contents)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.footer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.footer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addWidget(self.footer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 779, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuOpti_n = QMenu(self.menubar)
        self.menuOpti_n.setObjectName(u"menuOpti_n")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOpti_n.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.lb_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lb_count.setText(QCoreApplication.translate("MainWindow", u"count", None))
        self.lb_combine.setText(QCoreApplication.translate("MainWindow", u"combine", None))
        self.lb_check.setText("")
        self.s_draw_img.setText(QCoreApplication.translate("MainWindow", u"draw IMG", None))
        self.s_combine_audio.setText(QCoreApplication.translate("MainWindow", u"Combine Audio", None))
        self.s_make_vid.setText(QCoreApplication.translate("MainWindow", u"make vid", None))
        self.s_options.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuOpti_n.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

