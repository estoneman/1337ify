#!/usr/bin/python3

import sys

LEET_LEN = 122

def readfile(filename):
	with open(f"../{filename}", "r") as fp:
		return fp.readlines()


def main():
	if (len(sys.argv) < 2):
		print(f"Usage: {sys.argv[0]} <word to be translated>")
	else:
		word = sys.argv[1]
		new_word = ""
		key = readfile("leet.txt")

		for ch in word:
			new_word += key[0][ ord(ch) % LEET_LEN ]

		print(new_word)

if __name__ == "__main__":
	main()
