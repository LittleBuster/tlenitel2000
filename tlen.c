/*
 * tlen.c - Library for tlenization
 * Using OpenCV
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#include <opencv/highgui.h>
#include <stdio.h>
#include "tlen.h"


static IplImage* img_resize(IplImage* src_img, int new_width, int new_height)
{
    IplImage* des_img;
    des_img = cvCreateImage(cvSize(new_width, new_height), src_img->depth, src_img->nChannels);
    cvResize(src_img, des_img, CV_INTER_LINEAR);
    return des_img;
}

void tlen_image(const char *in_file, const char *templ_file, const char *result_file, double level)
{
    int x = 0;
    int y = 0;
    IplImage* dst;
    IplImage* image, *gray_image;
    IplImage* templ;
    IplImage* new_templ;
    int width, height;
    double alpha, beta;

    /* Get image */
    image = cvLoadImage(in_file, 1);
    assert(image != 0);

    templ = cvLoadImage(templ_file, 1);
    assert(templ != 0);

    /* Size of template */
    new_templ = img_resize(templ, image->width, image->height);
    width = new_templ->width;
    height = new_templ->height;
    dst = cvCloneImage(new_templ);

    alpha = level;
    beta = 0.5;

    /* Set area */
    cvSetImageROI(image, cvRect(x, y, width, height));
    /* Summ */
    cvAddWeighted(image, alpha, new_templ, beta, 0.0, dst);
    /* Free area */
    cvResetImageROI(image);

    /* Set black-white image */
    gray_image = cvCreateImage(cvSize(image->width,image->height), 8, 1);
    cvCvtColor(dst, gray_image, CV_RGB2GRAY);

    cvSaveImage(result_file, gray_image, NULL);

    /* Fre memory */
    cvReleaseImage(&image);
    cvReleaseImage(&gray_image);
    cvReleaseImage(&templ);
    cvReleaseImage(&new_templ);
    cvReleaseImage(&dst);
}
