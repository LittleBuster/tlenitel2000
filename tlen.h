/*
 * tlen.h - Library for tlenization
 * Using OpenCV
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#ifndef __TLEN_H__
#define __TLEN_H__

#include <opencv/cv.h>


extern void tlen_image(const char *in_file, /* Input image */
					const char *templ_file,	/* Template file with "tlen" */
					const char *result_file, /* Output image */
					double level); /* Tlenization level 0.0 - 1.0 */


#endif
