#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEET_LEN 123 // to include null terminator

int readfile(char* buf, char* fn, char* perm) {

	FILE* fp;
	fp = fopen(fn, perm);

	// populate leet buffer
	fgets(buf, LEET_LEN, fp);

	fclose(fp);

	return 0;
}

int main(int argc, char** argv)
{

	if (argc < 2) {
		printf("Usage: %s <word to be translated>\n", argv[0]);
		exit(0);
	}

	char* translated = (char*) calloc(1, strlen(argv[1])); // allocate one object of size len(argv[1]) e.g. 55
	char* arg = (char*) calloc(1, strlen(argv[1]));
	strncat(arg, argv[1], strlen(argv[1]));

	char* leet_chars = (char*) malloc(LEET_LEN);
	readfile(leet_chars, "../leet.txt", "r");

	while (*arg) {
		strncat(translated, &leet_chars[ *arg++ % LEET_LEN ], 1);
	}

	arg -= strlen(translated);

	printf("Non-1337:\t\t%s\n", arg);
	printf("1337 translated:\t%s\n", translated);

	free(translated);
	free(leet_chars);

	return 1;
}