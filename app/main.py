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

import sys
import os
import json
from PyQt4 import QtCore
from PyQt4 import QtGui
from urllib.request import urlretrieve
import mainWnd
import hashlib
from ftplib import FTP
from ctypes import cdll
import ctypes

class MainWindow(QtGui.QWidget):
	cfg = {}

	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		self.ui = mainWnd.Ui_mainForm()
		self.ui.setupUi(self)

		self.on_center()
		self.fname = ""

		self.lib = cdll.LoadLibrary("libtlen.dll")
		self.load_configs("config.cfg")
		self.ui.edOutUrl.hide()

		QtCore.QObject.connect(self.ui.pbT, QtCore.SIGNAL("clicked()"), self.on_tlen_clicked)
		QtCore.QObject.connect(self.ui.pbU, QtCore.SIGNAL("clicked()"), self.on_upload_clicked)
		QtCore.QObject.connect(self.ui.pbTU, QtCore.SIGNAL("clicked()"), self.on_tlen_and_up_clicked)
		QtCore.QObject.connect(self.ui.pbBrowse, QtCore.SIGNAL("clicked()"), self.on_browse_clicked)
		QtCore.QObject.connect(self.ui.slLevel, QtCore.SIGNAL("valueChanged(int)"), self.on_slider_change)

	def on_center(self):
		"""
		Set main window on screen center
		"""
		width = self.frameGeometry().width()
		height = self.frameGeometry().height()

		wid = QtGui.QDesktopWidget()
		screenWidth = wid.screen().width()
		screenHeight = wid.screen().height()

		self.setGeometry((screenWidth / 2) - (width / 2), (screenHeight / 2) - (height / 2), width, height)

	def load_configs(self, fname):
		"""
		Loading json configs file
		"""
		if not os.path.isfile( fname ):
			QtGui.QMessageBox.critical(self, 'Error', 'Отсутствует конфиг файл', QtGui.QMessageBox.Yes)
			return

		try:
			f = open(fname, "r")
			self.cfg = json.load(f)
			f.close()		
		except:
			QtGui.QMessageBox.critical(self, 'Error', 'Ошибка в файле конфигураций', QtGui.QMessageBox.Yes)
			return		

	def tlenization(self):
		"""
		Load C-Library with OpenCV Alpha tlenization
		"""
		self.ui.edOutUrl.hide()

		if self.ui.rbUrl.isChecked() == True:
			if self.ui.edUrl.text() == "":
				QtGui.QMessageBox.warning(self, 'Error', 'Нужна ссылка', QtGui.QMessageBox.Yes)
				return

			url_list = self.ui.edUrl.text().split("/")
			self.fname = url_list[len(url_list)-1]

			self.ui.pB.setValue(0)
			urlretrieve(self.ui.edUrl.text(), "img/" + self.fname)
			self.ui.pB.setValue(50)

			"""
			Call C-Library method
			"""
			self.lib.tlen_image(("img/" + self.fname).encode("utf-8"), "img/templ.jpg".encode("utf-8"), 
				"img/out.jpg".encode("utf-8"), ctypes.c_double(float(self.ui.slLevel.value() / 100)))
			self.ui.pB.setValue(100)
			os.remove("img/" + self.fname)


		if self.ui.rbPath.isChecked() == True:
			if self.ui.edPath.text() == "":
				QtGui.QMessageBox.warning(self, 'Error', 'Выберите файл', QtGui.QMessageBox.Yes)
				return

			path_list = self.ui.edPath.text().split("/")
			self.fname = path_list[len(path_list)-1]			

			self.ui.pB.setValue(0)
			"""
			Call C-Library method
			"""
			self.lib.tlen_image((self.ui.edPath.text()).encode("utf-8"), "img/templ.jpg".encode("utf-8"), 
				"img/out.jpg".encode("utf-8"), ctypes.c_double(float(self.ui.slLevel.value() / 100)))
			self.ui.pB.setValue(100)

		self.ui.lbPrev.setPixmap(QtGui.QPixmap("img/out.jpg"))

	def upload_file(self):
		"""
		Uploading images to ftp server
		"""
		self.ui.edOutUrl.hide()

		"""
		Create image filename hash
		"""
		m = hashlib.md5()
		m.update(self.fname.encode("utf-8"))
		res = str(m.hexdigest())

		"""
		Upload to server
		"""
		self.ui.pB.setValue(0)
		ftp = FTP( self.cfg["Ftp"]["ip"] )

		try:			
			ftp.login( self.cfg["Ftp"]["login"], self.cfg["Ftp"]["passwd"] )
			self.ui.pB.setValue(33)
		except:
			QtGui.QMessageBox.critical(self, 'Error', 'Неверный логин/пароль', QtGui.QMessageBox.Yes)
			return

		try:
			ftp.cwd( self.cfg["Ftp"]["path"] )
			self.ui.pB.setValue(66)
		except:
			QtGui.QMessageBox.critical(self, 'Error', 'Неверная удалённая папка', QtGui.QMessageBox.Yes)
			return

		try:
			ftp.storbinary("STOR " + res + ".jpg", open("img/out.jpg", "rb"))
			self.ui.pB.setValue(100)
		except:
			QtGui.QMessageBox.critical(self, 'Error', 'Ошибка загрузки файла', QtGui.QMessageBox.Yes)

		ftp.quit()

		"""
		Show http url with image
		"""
		self.ui.edOutUrl.show()
		self.ui.edOutUrl.setText( self.cfg["App"]["GetPath"] + res + ".jpg")

	def on_slider_change(self, level):
		self.ui.label_6.setText(str(level))

	def on_tlen_clicked(self):
		self.tlenization()

	def on_upload_clicked(self):
		self.upload_file()

	def on_tlen_and_up_clicked(self):
		self.tlenization()
		self.upload_file()

	def on_browse_clicked(self):
		self.ui.edPath.setText( QtGui.QFileDialog.getOpenFileName(self, 'Open file', "C:/") )
		self.ui.edOutUrl.hide()


def main():
	app = QtGui.QApplication(sys.argv)

	mw = MainWindow()
	mw.show()

	app.exec_()

if __name__ == '__main__':
    main()