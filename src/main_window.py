# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(686, 595)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 58, 101))
        self.imageOutputVertLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.imageOutputVertLayout.setSpacing(0)
        self.imageOutputVertLayout.setObjectName(u"imageOutputVertLayout")
        self.imageOutputVertLayout.setContentsMargins(0, 4, 0, 8)
        self.imageLabel = QLabel(self.verticalLayoutWidget)
        self.imageLabel.setObjectName(u"imageLabel")

        self.imageOutputVertLayout.addWidget(self.imageLabel)

        self.outputLabel = QLabel(self.verticalLayoutWidget)
        self.outputLabel.setObjectName(u"outputLabel")

        self.imageOutputVertLayout.addWidget(self.outputLabel)

        self.generateButton = QPushButton(Dialog)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(590, 550, 80, 26))
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(90, 20, 481, 101))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineTextImageInput = QLineEdit(self.verticalLayoutWidget_2)
        self.lineTextImageInput.setObjectName(u"lineTextImageInput")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineTextImageInput.sizePolicy().hasHeightForWidth())
        self.lineTextImageInput.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.lineTextImageInput)

        self.lineTextOutput = QLineEdit(self.verticalLayoutWidget_2)
        self.lineTextOutput.setObjectName(u"lineTextOutput")
        sizePolicy.setHeightForWidth(self.lineTextOutput.sizePolicy().hasHeightForWidth())
        self.lineTextOutput.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.lineTextOutput)

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(580, 20, 82, 101))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.imageInputButton = QPushButton(self.verticalLayoutWidget_3)
        self.imageInputButton.setObjectName(u"imageInputButton")

        self.verticalLayout_4.addWidget(self.imageInputButton)

        self.outputButton = QPushButton(self.verticalLayoutWidget_3)
        self.outputButton.setObjectName(u"outputButton")

        self.verticalLayout_4.addWidget(self.outputButton)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 140, 631, 26))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkUseFlatBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkUseFlatBox.setObjectName(u"checkUseFlatBox")

        self.horizontalLayout.addWidget(self.checkUseFlatBox)

        self.verticalLayoutWidget_5 = QWidget(Dialog)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(30, 180, 71, 41))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scale_label = QLabel(self.verticalLayoutWidget_5)
        self.scale_label.setObjectName(u"scale_label")

        self.verticalLayout_5.addWidget(self.scale_label)

        self.verticalLayoutWidget_6 = QWidget(Dialog)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(100, 180, 160, 41))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setSpacing(16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scale_LineEdit = QLineEdit(self.verticalLayoutWidget_6)
        self.scale_LineEdit.setObjectName(u"scale_LineEdit")
        self.scale_LineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scale_LineEdit.sizePolicy().hasHeightForWidth())
        self.scale_LineEdit.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.scale_LineEdit)

        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(30, 240, 641, 291))
        self.preview_tab = QWidget()
        self.preview_tab.setObjectName(u"preview_tab")
        self.imageLabel_2 = QLabel(self.preview_tab)
        self.imageLabel_2.setObjectName(u"imageLabel_2")
        self.imageLabel_2.setGeometry(QRect(10, 10, 281, 161))
        self.verticalLayoutWidget_7 = QWidget(self.preview_tab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(430, 40, 160, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imgOutSizeX = QLabel(self.verticalLayoutWidget_7)
        self.imgOutSizeX.setObjectName(u"imgOutSizeX")

        self.verticalLayout_2.addWidget(self.imgOutSizeX)

        self.imgOutSizeY = QLabel(self.verticalLayoutWidget_7)
        self.imgOutSizeY.setObjectName(u"imgOutSizeY")

        self.verticalLayout_2.addWidget(self.imgOutSizeY)

        self.tabWidget.addTab(self.preview_tab, "")
        self.barLabel = QLabel(Dialog)
        self.barLabel.setObjectName(u"barLabel")
        self.barLabel.setGeometry(QRect(30, 547, 201, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.imageLabel.setText(QCoreApplication.translate("Dialog", u"Image:", None))
        self.outputLabel.setText(QCoreApplication.translate("Dialog", u"Output:", None))
#if QT_CONFIG(tooltip)
        self.generateButton.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Generate .schematica File</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.generateButton.setText(QCoreApplication.translate("Dialog", u"Generate!", None))
        self.imageInputButton.setText(QCoreApplication.translate("Dialog", u"Open...", None))
        self.outputButton.setText(QCoreApplication.translate("Dialog", u"Open...", None))
#if QT_CONFIG(tooltip)
        self.checkUseFlatBox.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Change the Palette to Flat.</p><p>The map will be flat with only 51 Colours, instead of the normal 153.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkUseFlatBox.setText(QCoreApplication.translate("Dialog", u"Use Flat Colour Palette", None))
        self.scale_label.setText(QCoreApplication.translate("Dialog", u"Scale:", None))
        self.scale_LineEdit.setText(QCoreApplication.translate("Dialog", u"1.0", None))
        self.imageLabel_2.setText("")
        self.imgOutSizeX.setText(QCoreApplication.translate("Dialog", u"X:", None))
        self.imgOutSizeY.setText(QCoreApplication.translate("Dialog", u"Y:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preview_tab), QCoreApplication.translate("Dialog", u"Preview", None))
        self.barLabel.setText("")
    # retranslateUi

