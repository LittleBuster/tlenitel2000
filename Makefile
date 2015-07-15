CC=gcc
CFLAGS=-O3 -Wall -I. -L. -Wno-deprecated-declarations  -fopenmp
LDFLAGS=`pkg-config --cflags --libs gtk+-3.0`
LDFLAGS2=-lopencv_core -lopencv_highgui
LDFLAGS3=`pkg-config --cflags --libs jansson`

all: tlenitel

tlenitel: main.o mainwnd.o
	#cv library
	$(CC) -fPIC -c tlen.c -o tlen.o $(CFLAGS) $(LDFLAGS2)
	$(CC) -shared tlen.o -o libtlen.so $(CFLAGS) $(LDFLAGS2)
	#Application
	$(CC) main.o mainwnd.o -o tlenitel $(CFLAGS) $(LDFLAGS) $(LDFLAGS2) $(LDFLAGS3) -ldl
	strip tlenitel
	mkdir bin
	mv tlenitel bin/
	cp libtlen.so bin/
	cp -r img bin/
	cp mainWnd.glade bin/

main.o: main.c
	$(CC) -c main.c $(CFLAGS) $(LDFLAGS)

mainwnd.o: mainwnd.c
	$(CC) -c mainwnd.c $(CFLAGS) $(LDFLAGS) $(LDFLAGS3)

clean:
	rm -rf *.o bin/ mainWnd.glade~ libtlen.so
