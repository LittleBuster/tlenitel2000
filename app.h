/*
 * app.h - all windows here
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#ifndef __APPLICATION_H__
#define __APPLICATION_H__

#include "mainwnd.h"


struct application_t {
	struct main_window mw;
};

void application_start(struct application_t *app, int argc, char **argv);

#endif
