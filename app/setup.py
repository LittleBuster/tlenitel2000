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
from cx_Freeze import setup, Executable

base = 'Win32GUI'

setup(name = 'Tlenitel2000',
      version = '0.0.1',
      executables = [Executable('main.py', icon='appimg/Tamako Market3.ico', base=base)],
      options = {'build_exe': {'includes': ['sip']}})