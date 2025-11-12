# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'donasi_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1085, 505)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 30, 311, 41))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 100, 111, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 140, 101, 20))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 180, 131, 20))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 220, 111, 20))
        self.simpanButton = QPushButton(Form)
        self.simpanButton.setObjectName(u"simpanButton")
        self.simpanButton.setGeometry(QRect(230, 400, 90, 29))
        self.ubahButton = QPushButton(Form)
        self.ubahButton.setObjectName(u"ubahButton")
        self.ubahButton.setGeometry(QRect(390, 400, 90, 29))
        self.hapusButton = QPushButton(Form)
        self.hapusButton.setObjectName(u"hapusButton")
        self.hapusButton.setGeometry(QRect(560, 400, 90, 29))
        self.idDonasiInput = QLineEdit(Form)
        self.idDonasiInput.setObjectName(u"idDonasiInput")
        self.idDonasiInput.setGeometry(QRect(300, 100, 231, 28))
        self.jumlahInput = QLineEdit(Form)
        self.jumlahInput.setObjectName(u"jumlahInput")
        self.jumlahInput.setGeometry(QRect(300, 220, 231, 28))
        self.tglMasukInput = QDateEdit(Form)
        self.tglMasukInput.setObjectName(u"tglMasukInput")
        self.tglMasukInput.setGeometry(QRect(300, 180, 231, 29))
        self.idDonaturInput = QComboBox(Form)
        self.idDonaturInput.setObjectName(u"idDonaturInput")
        self.idDonaturInput.setGeometry(QRect(300, 140, 231, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; color:#00007f;\">FORM DONASI</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ID DONASI", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ID DONATUR", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TANGGAL MASUK", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"JUMLAH", None))
        self.simpanButton.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.ubahButton.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.hapusButton.setText(QCoreApplication.translate("Form", u"UBAH", None))
    # retranslateUi

