all:
	gcc -c -fPIC tlen.c -I. -Wall -O3 C:\OpenCV\lib\cv.lib C:\OpenCV\lib\highgui.lib C:\OpenCV\lib\cxcore.lib
	gcc -shared -Wall -O3 tlen.o -o libtlen.dll C:\OpenCV\lib\cv.lib C:\OpenCV\lib\highgui.lib C:\OpenCV\lib\cxcore.lib

clean:
	rm *.o libtlen.dll