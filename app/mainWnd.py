# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWnd.ui'
#
# Created: Tue Dec  2 03:45:32 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
#
# Tlenitel 2000 is app for tlenization anime-images for quizes
# on Anison.fm (http://www.anison.fm)
#
# Copyright © 2014 by Sergey Denisov aka 'LittleBuster'
# E-Mail: DenisovS21 at gmail dor com (DenisovS21@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName(_fromUtf8("mainForm"))
        mainForm.resize(1056, 668)
        mainForm.setMinimumSize(QtCore.QSize(1056, 668))
        mainForm.setMaximumSize(QtCore.QSize(1056, 668))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("appimg/Tamako Market3.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        self.label = QtGui.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 1061, 671))
        self.label.setAutoFillBackground(False)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("appimg/fon-qwaser.jpg")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(mainForm)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 741, 141))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("appimg/radio-logo-b.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pB = QtGui.QProgressBar(mainForm)
        self.pB.setGeometry(QtCore.QRect(20, 590, 751, 23))
        self.pB.setProperty("value", 0)
        self.pB.setTextVisible(False)
        self.pB.setObjectName(_fromUtf8("pB"))
        self.pbTU = QtGui.QPushButton(mainForm)
        self.pbTU.setGeometry(QtCore.QRect(20, 620, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbTU.setFont(font)
        self.pbTU.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 75, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.pbTU.setIconSize(QtCore.QSize(24, 24))
        self.pbTU.setObjectName(_fromUtf8("pbTU"))
        self.widget = QtGui.QWidget(mainForm)
        self.widget.setGeometry(QtCore.QRect(20, 60, 751, 121))
        self.widget.setStyleSheet(_fromUtf8("QWidget {\n"
"    background-color: rgba(121, 121, 121, 150);\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.edUrl = QtGui.QLineEdit(self.widget)
        self.edUrl.setGeometry(QtCore.QRect(130, 10, 611, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edUrl.setFont(font)
        self.edUrl.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    background-color:rgba(139, 139, 139, 150);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.edUrl.setText(_fromUtf8(""))
        self.edUrl.setObjectName(_fromUtf8("edUrl"))
        self.edPath = QtGui.QLineEdit(self.widget)
        self.edPath.setGeometry(QtCore.QRect(130, 50, 521, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edPath.setFont(font)
        self.edPath.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    background-color:rgba(139, 139, 139, 150);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.edPath.setText(_fromUtf8(""))
        self.edPath.setObjectName(_fromUtf8("edPath"))
        self.rbUrl = QtGui.QRadioButton(self.widget)
        self.rbUrl.setGeometry(QtCore.QRect(10, 17, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbUrl.setFont(font)
        self.rbUrl.setStyleSheet(_fromUtf8("QWidget {\n"
"    color:rgb(255, 255, 255);\n"
"}"))
        self.rbUrl.setChecked(True)
        self.rbUrl.setObjectName(_fromUtf8("rbUrl"))
        self.rbPath = QtGui.QRadioButton(self.widget)
        self.rbPath.setGeometry(QtCore.QRect(10, 57, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rbPath.setFont(font)
        self.rbPath.setStyleSheet(_fromUtf8("QWidget {\n"
"    color:rgb(255, 255, 255);\n"
"}"))
        self.rbPath.setObjectName(_fromUtf8("rbPath"))
        self.pbBrowse = QtGui.QPushButton(self.widget)
        self.pbBrowse.setGeometry(QtCore.QRect(660, 50, 82, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbBrowse.setFont(font)
        self.pbBrowse.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 75, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Users/sergey/.designer/backup/images/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbBrowse.setIcon(icon1)
        self.pbBrowse.setIconSize(QtCore.QSize(24, 24))
        self.pbBrowse.setObjectName(_fromUtf8("pbBrowse"))
        self.slLevel = QtGui.QSlider(self.widget)
        self.slLevel.setGeometry(QtCore.QRect(90, 92, 581, 20))
        self.slLevel.setMinimum(1)
        self.slLevel.setMaximum(100)
        self.slLevel.setSingleStep(1)
        self.slLevel.setPageStep(1)
        self.slLevel.setProperty("value", 20)
        self.slLevel.setOrientation(QtCore.Qt.Horizontal)
        self.slLevel.setObjectName(_fromUtf8("slLevel"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 92, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(680, 92, 23, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_3 = QtGui.QLabel(mainForm)
        self.label_3.setGeometry(QtCore.QRect(-120, 0, 1021, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbT = QtGui.QPushButton(mainForm)
        self.pbT.setGeometry(QtCore.QRect(360, 620, 200, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbT.setFont(font)
        self.pbT.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 75, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.pbT.setIcon(icon1)
        self.pbT.setIconSize(QtCore.QSize(24, 24))
        self.pbT.setObjectName(_fromUtf8("pbT"))
        self.pbU = QtGui.QPushButton(mainForm)
        self.pbU.setGeometry(QtCore.QRect(570, 620, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbU.setFont(font)
        self.pbU.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 75, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:pad, x1:0.483, y1:1, x2:0.489, y2:0, stop:0 rgba(63, 63, 63, 255), stop:0.710227 rgba(75, 75, 198, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.pbU.setIcon(icon1)
        self.pbU.setIconSize(QtCore.QSize(24, 24))
        self.pbU.setObjectName(_fromUtf8("pbU"))
        self.lbPrev = QtGui.QLabel(mainForm)
        self.lbPrev.setGeometry(QtCore.QRect(20, 190, 751, 391))
        self.lbPrev.setMinimumSize(QtCore.QSize(751, 391))
        self.lbPrev.setMaximumSize(QtCore.QSize(751, 391))
        self.lbPrev.setText(_fromUtf8(""))
        self.lbPrev.setScaledContents(True)
        self.lbPrev.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbPrev.setObjectName(_fromUtf8("lbPrev"))
        self.label_5 = QtGui.QLabel(mainForm)
        self.label_5.setGeometry(QtCore.QRect(820, 550, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.edOutUrl = QtGui.QLineEdit(mainForm)
        self.edOutUrl.setGeometry(QtCore.QRect(30, 540, 721, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edOutUrl.setFont(font)
        self.edOutUrl.setStyleSheet(_fromUtf8("QLineEdit {\n"
"    background-color:rgba(139, 139, 139, 150);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}"))
        self.edOutUrl.setText(_fromUtf8(""))
        self.edOutUrl.setReadOnly(True)
        self.edOutUrl.setObjectName(_fromUtf8("edOutUrl"))

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(_translate("mainForm", "Тленитель 2000 HD", None))
        self.pbTU.setText(_translate("mainForm", "Тленить и залить", None))
        self.rbUrl.setText(_translate("mainForm", "По ссылке", None))
        self.rbPath.setText(_translate("mainForm", "Из файла", None))
        self.pbBrowse.setText(_translate("mainForm", "Обзор", None))
        self.label_4.setText(_translate("mainForm", "Уровень", None))
        self.label_6.setText(_translate("mainForm", "20", None))
        self.label_3.setText(_translate("mainForm", "<html><head/><body><p><span style=\" color:#ffffff;\">Тленитель 2000</span></p></body></html>", None))
        self.pbT.setText(_translate("mainForm", "Тленить", None))
        self.pbU.setText(_translate("mainForm", "Залить", None))
        self.label_5.setText(_translate("mainForm", "<html><head/><body><p align=\"center\"><span style=\" color:#a5a5a5;\">by LittleBuster</span></p><p align=\"center\"><span style=\" color:#a5a5a5;\">DenisovS21@gmail.com</span></p></body></html>", None))

