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

#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <stdio.h>
#include "tlen.h"

IplImage* image = 0;
IplImage* templ = 0;
IplImage* new_templ = 0;
IplImage* dst = 0;

IplImage* img_resize( IplImage* src_img, int new_width, int new_height ) {
    IplImage* des_img;
    des_img = cvCreateImage(cvSize(new_width, new_height), src_img->depth, src_img->nChannels);
    cvResize(src_img, des_img, CV_INTER_LINEAR);
    return des_img;
}

void tlen_image( const char *in_file, const char *templ_file, const char *result_file, double level ) {
        // получаем картинку
        image = cvLoadImage(in_file, 1);
        assert( image != 0 );

        templ = cvLoadImage(templ_file, 1);
        assert( templ != 0 );    

        // размер шаблона
        new_templ = img_resize(templ, image->width, image->height);

        int width = new_templ->width;
        int height = new_templ->height;

        dst = cvCloneImage(new_templ);
        
        int x = 0;
        int y = 0;
        // задаём весовые коэффициенты
        double alpha = level;
        double beta = 0.5;
        // устанавливаем область интереса
        cvSetImageROI(image, cvRect(x,y,width,height));
        // взвешенная сумма
        cvAddWeighted(image, alpha, new_templ, beta, 0.0, dst);
        // освобождаем область интереса
        cvResetImageROI(image);
        
        cvSaveImage(result_file, dst);

        // освобождаем ресурсы
        cvReleaseImage( &image );
        cvReleaseImage( &templ );
        cvReleaseImage( &new_templ );
        cvReleaseImage( &dst );
}