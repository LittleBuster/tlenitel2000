CC=gcc
CFLAGS=-O3 -Wall -I. -Wno-deprecated-declarations -fopenmp -ldl
LDFLAGS=`pkg-config --cflags --libs gtk+-3.0`
LDFLAGS2=-lopencv_core -lopencv_highgui

all: tlenitel

tlenitel: main.o mainwnd.o app.o
	#cv library
	$(CC) -fPIC -c tlen.c -o tlen.o $(CFLAGS) $(LDFLAGS2)
	$(CC) -shared tlen.o -o libtlen.so $(CFLAGS) $(LDFLAGS2)
	#Application
	$(CC) main.o mainwnd.o app.o -o tlenitel $(CFLAGS) $(LDFLAGS)
	strip tlenitel
	mkdir bin
	mv tlenitel bin/
	cp libtlen.so bin/
	cp -r img bin/
	cp mainWnd.glade bin/

app.o: app.c
	$(CC) -c app.c $(CFLAGS) $(LDFLAGS)

main.o: main.c
	$(CC) -c main.c $(CFLAGS) $(LDFLAGS)

mainwnd.o: mainwnd.c
	$(CC) -c mainwnd.c $(CFLAGS) $(LDFLAGS)

clean:
	rm -rf *.o bin/ mainWnd.glade~ libtlen.so
