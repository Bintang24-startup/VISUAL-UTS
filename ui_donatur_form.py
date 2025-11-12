# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donatur_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1148, 505)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 90, 91, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 130, 91, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 170, 101, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 210, 101, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 30, 351, 41))
        self.idDonaturInput = QLineEdit(Form)
        self.idDonaturInput.setObjectName(u"idDonaturInput")
        self.idDonaturInput.setGeometry(QRect(250, 90, 191, 28))
        self.namaInput = QLineEdit(Form)
        self.namaInput.setObjectName(u"namaInput")
        self.namaInput.setGeometry(QRect(250, 130, 191, 28))
        self.telpInput = QLineEdit(Form)
        self.telpInput.setObjectName(u"telpInput")
        self.telpInput.setGeometry(QRect(250, 170, 191, 28))
        self.alamatInput = QTextEdit(Form)
        self.alamatInput.setObjectName(u"alamatInput")
        self.alamatInput.setGeometry(QRect(250, 210, 381, 131))
        self.simpanButton = QPushButton(Form)
        self.simpanButton.setObjectName(u"simpanButton")
        self.simpanButton.setGeometry(QRect(180, 410, 90, 29))
        self.ubahButton = QPushButton(Form)
        self.ubahButton.setObjectName(u"ubahButton")
        self.ubahButton.setGeometry(QRect(320, 410, 90, 29))
        self.hapusButton = QPushButton(Form)
        self.hapusButton.setObjectName(u"hapusButton")
        self.hapusButton.setGeometry(QRect(470, 410, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID DONATUR", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NAMA", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TELEPON ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ALAMAT", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00007f;\">Form Donatur</span></p></body></html>", None))
        self.simpanButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.ubahButton.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.hapusButton.setText(QCoreApplication.translate("Form", u"UBAH", None))
    # retranslateUi

