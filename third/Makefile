all: main.cpp BigInt.cpp
	g++ -c -fPIC BigInt.cpp
	g++ -shared -o libBigInt.so BigInt.o
	LD_LIBRARY_PATH=./ g++ main.cpp -lBigInt -I. -Wl,-rpath,. -L. -o long_ariph
windows: main.cpp BigInt.cpp
	g++ -c BigInt.cpp
	g++ -shared -o BigInt.dll BigInt.o
	g++ main.cpp BigInt.dll -I. -Wl,-rpath,. -L. -o long_ariph.exe

Python_Win64:
	swig -c++ -python BigInt.i
	g++ -c BigInt.cpp
	g++ -c bigInt_wrap.cxx -IC:\Python27\include
	g++ BigInt.o bigInt_wrap.o -Ic:\python27\include -Lc:\python27\libs -lpython27 -shared -o _BigInt.pyd
Python_U:	
	swig -c++ -python BigInt.i
	g++ -fPIC -c BigInt.cpp
	g++ -fPIC -c BigInt_wrap.cxx -I/usr/include/python2.7
	g++ -shared BigInt.o BigInt_wrap.o -o _BigInt.so
