// TlenLib is library for tlenization anime-images for quizes
// on Anison.fm (http://www.anison.fm)
//
// Copyright © 2014 by Sergey Denisov aka 'LittleBuster'
// E-Mail: DenisovS21 at gmail dor com (DenisovS21@gmail.com)
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 3
// as published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>

#ifndef TLEN_LIB_H
#define TLEN_LIB_H

extern void tlen_image( 
	const char *in_file, 
	const char *templ_file, 
	const char *result_file, 
	double level // 0..1
	);

#endif