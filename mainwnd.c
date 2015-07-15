/*
 * mainwnd.c - main window of application
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dlfcn.h>
#include <omp.h>
#include "mainwnd.h"
#include "path.h"


/* Main window signals */
static void main_window_destroy(GtkWidget *w, gpointer data);
static void button_tlen_click(GtkWidget *w, gpointer data);
static void button_open_img_click(GtkWidget *w, gpointer data);
static void button_open_out_click(GtkWidget *w, gpointer data);
static void adj_change(GtkAdjustment *w, gpointer data);

/* Tlenization library function */
void (*tlen_image)(const char *in_file, const char *templ_file, const char *result_file, double level);

/* All application dialogs */
static void show_dialog(GtkWidget *parent, const char *title, const char *text, int type)
{
	GtkWidget *dialog = NULL;
	dialog = gtk_message_dialog_new(GTK_WINDOW(parent), GTK_DIALOG_MODAL | GTK_DIALOG_DESTROY_WITH_PARENT,
																		type, GTK_BUTTONS_OK, "%s", text);
	gtk_window_set_title(GTK_WINDOW(dialog), title);
	gtk_dialog_run(GTK_DIALOG(dialog));
	gtk_widget_destroy(dialog);
}

void main_window_init(struct main_window *mw)
{
	int w, h;

	omp_set_num_threads(2);
	#pragma omp parallel sections
	{
		#pragma omp section
		{
			mw->handle = dlopen(LIB_TLEN_PATH, RTLD_LAZY);
			tlen_image = dlsym(mw->handle, "tlen_image");
		}

		#pragma omp section
		{
			mw->builder = gtk_builder_new_from_file(MAIN_WINDOW_GLADE_FILE);

			/* Load main window from glade file */
			mw->wnd = GTK_WIDGET(gtk_builder_get_object(mw->builder, "window1"));
			gtk_window_get_size(GTK_WINDOW(mw->wnd), &w, &h);
			gtk_window_move(GTK_WINDOW(mw->wnd), gdk_screen_width() / 2 - w / 2, gdk_screen_height() / 2 - h / 2);
			g_signal_connect(G_OBJECT(mw->wnd), "destroy", G_CALLBACK(main_window_destroy), (gpointer)mw);

			mw->e_open_img = GTK_ENTRY(gtk_builder_get_object(mw->builder, "eOpenImg"));
			mw->e_open_out = GTK_ENTRY(gtk_builder_get_object(mw->builder, "eOpenOut"));
			mw->e_level = GTK_ENTRY(gtk_builder_get_object(mw->builder, "eLevel"));
			mw->i_main = GTK_IMAGE(gtk_builder_get_object(mw->builder, "iMain"));

			mw->adj_val = GTK_ADJUSTMENT(gtk_builder_get_object(mw->builder, "adjVal"));
			g_signal_connect(G_OBJECT(mw->adj_val), "value-changed", G_CALLBACK(adj_change), (gpointer)mw);

			mw->b_open_img = GTK_WIDGET(gtk_builder_get_object(mw->builder, "bOpenImg"));
			g_signal_connect(G_OBJECT(mw->b_open_img), "clicked", G_CALLBACK(button_open_img_click), (gpointer)mw);

			mw->b_open_out = GTK_WIDGET(gtk_builder_get_object(mw->builder, "bOpenOut"));
			g_signal_connect(G_OBJECT(mw->b_open_out), "clicked", G_CALLBACK(button_open_out_click), (gpointer)mw);

			mw->b_tlen = GTK_WIDGET(gtk_builder_get_object(mw->builder, "bTlen"));
			g_signal_connect(G_OBJECT(mw->b_tlen), "clicked", G_CALLBACK(button_tlen_click), (gpointer)mw);
		}
	}
}

void main_window_show(struct main_window *mw)
{
	gtk_widget_show_all(mw->wnd);
}

/* Free memory */
void main_window_release(struct main_window *mw)
{
	dlclose(mw->handle);
	gtk_widget_destroy(mw->wnd);
	gtk_main_quit();
}

static void main_window_destroy(GtkWidget *w, gpointer data)
{
	struct main_window *mw = data;
	main_window_release(mw);
}

static void button_tlen_click(GtkWidget *w, gpointer data)
{
	double val;
	struct main_window *mw = data;
	const char *in_text = gtk_entry_get_text(mw->e_open_img);
	const char *out_text = gtk_entry_get_text(mw->e_open_out);
	const char *level = gtk_entry_get_text(mw->e_level);

	sscanf(level, "%lf", &val);

	if (!strcmp(in_text, "")) {
		show_dialog(mw->wnd, "Warning!", "Выберите изображение!", GTK_MESSAGE_WARNING);
		return;
	}

	if (!strcmp(out_text, "")) {
		show_dialog(mw->wnd, "Warning!", "Выберите файл для сохранения!", GTK_MESSAGE_WARNING);
		return;
	}

	if (val == 0.0f) {
		show_dialog(mw->wnd, "Warning!", "Укажите уровень тленизации", GTK_MESSAGE_WARNING);
		return;
	}

	(*tlen_image)(in_text, IMG_TEMPL_TEXT, out_text, val);
	gtk_image_set_from_file(mw->i_main, out_text);
}

/* New image for tlenization */
static void button_open_img_click(GtkWidget *w, gpointer data)
{
	char *filename = NULL;
	struct main_window *mw = data;
	GtkWidget *dialog;

	dialog = gtk_file_chooser_dialog_new("Open Image",
										GTK_WINDOW(mw->wnd),
										GTK_FILE_CHOOSER_ACTION_OPEN,
										GTK_STOCK_CANCEL, GTK_RESPONSE_CANCEL,
										GTK_STOCK_OPEN, GTK_RESPONSE_ACCEPT,
										NULL);

	if (gtk_dialog_run(GTK_DIALOG(dialog)) == GTK_RESPONSE_ACCEPT) {
		filename = gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(dialog));
		gtk_entry_set_text(mw->e_open_img, filename);
		gtk_image_set_from_file(mw->i_main, filename);
	}
	gtk_widget_destroy(dialog);
	free(filename);
}

/* Tlenization level change */
static void adj_change(GtkAdjustment *w, gpointer data)
{
	char text[100];
	struct main_window *mw = data;

	double val = gtk_adjustment_get_value(w);

	memset(text, 0x00, 100);
	sprintf(text, "%f", val);
	gtk_entry_set_text(mw->e_level, text);
}

/* Save output image to this location */
static void button_open_out_click(GtkWidget *w, gpointer data)
{
	char *filename = NULL;
	GtkWidget *dialog = NULL;
	struct main_window *mw = data;

	dialog = gtk_file_chooser_dialog_new("Save Image",
										GTK_WINDOW(mw->wnd),
										GTK_FILE_CHOOSER_ACTION_SAVE,
										GTK_STOCK_CANCEL, GTK_RESPONSE_CANCEL,
										GTK_STOCK_SAVE, GTK_RESPONSE_ACCEPT,
										NULL);

	if (gtk_dialog_run(GTK_DIALOG(dialog)) == GTK_RESPONSE_ACCEPT) {
		filename = gtk_file_chooser_get_filename(GTK_FILE_CHOOSER(dialog));
		gtk_entry_set_text(mw->e_open_out, filename);
	}
	free(filename);
	gtk_widget_destroy(dialog);
}
