/*
 * mainwnd.h - main window of application
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#ifndef __MAIN_WINDOW_H__
#define __MAIN_WINDOW_H__

#include <gtk/gtk.h>

struct main_window {
	GtkBuilder *builder;
	GtkWidget *wnd;
	GtkWidget *b_open_img;
	GtkWidget *b_open_out;
	GtkWidget *b_tlen;
	GtkEntry *e_open_img;
	GtkEntry *e_open_out;
	GtkEntry *e_level;
	GtkImage *i_main;
	GtkAdjustment *adj_val;
	void *handle;
};

struct main_window *main_window_new(void);

void main_window_show(struct main_window *mw);

void main_window_destroy(struct main_window *mw);

#endif
