BUILDDIR=./build

CC=/usr/bin/clang

SRC=./c/translate.c
OUT=$(BUILDDIR)/translate

CFLAGS=

default: all

all: main clean

main:
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -o $(OUT) $(SRC)

clean:
	rm -rf $(BUILDDIR)
