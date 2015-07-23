/*
 * app.c - all windows here
 *
 * Copyright (c) 2015 Denisov Sergey
 *
 * This file is released under the GPLv3
 *
 */

#include <stdlib.h>
#include "app.h"

struct application_t *application_new(void)
{
    struct application_t *app = NULL;
    app = (struct application_t *)malloc(sizeof(struct application_t));
    return app;
}

void application_start(struct application_t *app, int argc, char **argv)
{
	gtk_init(&argc, &argv);

	app->mw = main_window_new();
	main_window_show(app->mw);

	gtk_main();
    main_window_destroy(app->mw);
}

void application_destroy(struct application_t *app)
{
    free(app);
}
