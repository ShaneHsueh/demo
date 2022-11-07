"""
File: rocket.py
Name: Shane Hsueh
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
	build_head()   # build the head
	build_belt()   # build the upper belt
	build_upper()  # build the upper body
	build_lower()  # build the lower body
	build_belt()   # build the lower belt
	build_head()   # build the tail


def build_head():
	head = ""
	for i in range(SIZE):
		for j in range(i+1):
			head = '/' + head + '\\'
		for k in range(SIZE-i):
			head = ' ' + head + ' '
		print(head)
		head = ""


def build_belt():
	belt = ""
	for i in range(SIZE):
		belt = '==' + belt
	belt = '+' + belt + '+'
	print(belt)


def build_upper():
	upper = ""
	for i in range(SIZE):
		for j in range(i+1):
			upper = '/\\' + upper
		for k in range(SIZE-i-1):
			upper = '.' + upper + '.'
		upper = '|' + upper + '|'
		print(upper)
		upper = ""


def build_lower():
	lower = ""
	for i in range(SIZE):
		for j in range(SIZE-i):
			lower = '\\/' + lower
		for k in range(i):
			lower = '.' + lower + '.'
		lower = '|' + lower + '|'
		print(lower)
		lower = ""


if __name__ == '__main__':
	main()
