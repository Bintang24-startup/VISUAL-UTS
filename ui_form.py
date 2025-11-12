# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionDATA_DONASI = QAction(Main)
        self.actionDATA_DONASI.setObjectName(u"actionDATA_DONASI")
        self.actionDATA_DONATUR = QAction(Main)
        self.actionDATA_DONATUR.setObjectName(u"actionDATA_DONATUR")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuAPLIKASI_KEUANGAN_MASJID = QMenu(self.menubar)
        self.menuAPLIKASI_KEUANGAN_MASJID.setObjectName(u"menuAPLIKASI_KEUANGAN_MASJID")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAPLIKASI_KEUANGAN_MASJID.menuAction())
        self.menuAPLIKASI_KEUANGAN_MASJID.addAction(self.actionDATA_DONASI)
        self.menuAPLIKASI_KEUANGAN_MASJID.addAction(self.actionDATA_DONATUR)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionDATA_DONASI.setText(QCoreApplication.translate("Main", u"DATA_DONASI", None))
        self.actionDATA_DONATUR.setText(QCoreApplication.translate("Main", u"DATA_DONATUR", None))
        self.menuAPLIKASI_KEUANGAN_MASJID.setTitle(QCoreApplication.translate("Main", u"APLIKASI KEUANGAN MASJID", None))
    # retranslateUi

