#!/usr/bin/python3

'''
What I want to do:
	1. write leet characters to file ordered by a hashed index
		a. For easy access of get operations
		b. Get ASCII value of alphabet char, then store its leet candidate at the resultant array offset
'''

LEET_LEN	= 122
LEET_CHARS	= [
				"@",
				"4",
				"b",
				"8",
				"<",
				"[",
				"d",
				"D",
				"3",
				"3",
				"f",
				"F",
				"9",
				"6",
				"h",
				"H",
				"!",
				"1",
				"j",
				"J",
				"k",
				"K",
				"|",
				"L",
				"m",
				"M",
				"n",
				"N",
				"0",
				"0",
				"p",
				"P",
				"q",
				"Q",
				"r",
				"5",
				"$",
				"5",
				"t",
				"7",
				"u",
				"U",
				"v",
				"V",
				"w",
				"W",
				"*",
				"X",
				"y",
				"Y",
				"z",
				"Z",
				" ",
			  ]

# lowercase -> [97, 122]
# uppercase -> [67, 90]
def main():
	# preprocessing
	charset = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ "
	leet_chars = [None] * LEET_LEN
	for i in range(len(charset)):
		leet_chars[ord(charset[i]) % LEET_LEN] = LEET_CHARS[i]

	# write to dictionary file
	with open("../leet.txt", "a") as fp:
		for i in range(len(leet_chars)):
			if leet_chars[i] is None:
				fp.write('-')
			else:
				fp.write(leet_chars[i])

if __name__ == "__main__":
	main()
