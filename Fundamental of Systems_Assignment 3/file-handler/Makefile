CC=gcc
CFLAGS=-I.
DEPS = wordsProcessorLL.h
OBJ = wordCount.o wordsProcessorLL.o

%.o: %.c $(DEPS)
		$(CC) -c -o $@ $< $(CFLAGS)
		
wordCount: $(OBJ)
		$(CC) -o $@ $^ $(CFLAGS)