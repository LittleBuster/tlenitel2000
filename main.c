/*
 * main.c - application start
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#include "app.h"


int main(int argc, char **argv)
{
	struct application_t *app = application_new();
	application_start(app, argc, argv);
	application_destroy(app);
	return 0;
}
