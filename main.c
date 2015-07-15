/*
 * main.c - application start
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#include <stdio.h>
#include <gtk/gtk.h>
#include <stdlib.h>
#include "app.h"
#include "mainwnd.h"


void application_start(struct application_t *app, int argc, char **argv)
{
	gtk_init(&argc, &argv);
	
	main_window_init(&app->mw);
	main_window_show(&app->mw);

	gtk_main();
}

int main(int argc, char **argv)
{
	struct application_t app;
	application_start(&app, argc, argv);
	return 0;
}