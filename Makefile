exploit : exploit.o
	gcc -o exploit exploit.o 

exploit.o : exploit.c exploit.h
	gcc -c exploit.c
	
clean: rm exploit.o
