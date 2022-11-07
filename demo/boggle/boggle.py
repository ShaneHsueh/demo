"""
File: boggle.py
Name: Shane
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dictionary = []
dictionary_short_version = []


def main():
	read_dictionary()
	line1 = input('1 row of letters: ')
	check_word(line1)

	line2 = input('2 row of letters: ')
	check_word(line2)

	line3 = input('3 row of letters: ')
	check_word(line3)

	line4 = input('4 row of letters: ')
	check_word(line4)

	start = time.time()
	find_anagrams(line1, line2, line3, line4)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def check_word(word):
	# 確認輸入格式是否正確
	if len(word.split()) != 4:
		print('Illegal input')
		quit()
	for i in range(4):
		if len(word.split()[i]) != 1:
			print('Illegal input')
			quit()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as f:
		for line in f:
			dictionary += line.split()


def find_anagrams(line1, line2, line3, line4):
	global dictionary_short_version
	# 將輸入的四行字元建立成16個單字的list
	word_list = []
	for i in range(4):
		word_list += line1.split()[i].lower()
		word_list += line2.split()[i].lower()
		word_list += line3.split()[i].lower()
		word_list += line4.split()[i].lower()

	# 創造一本新字典 裡面只含字數一樣，且字母也都一樣的單字
	for i in range(len(dictionary)):
		if len(dictionary[i]) >= 4:
			correct = 0
			for j in range(len(dictionary[i])):
				if dictionary[i][j] not in word_list:
					break
				else:
					correct += 1
			if correct == len(dictionary[i]):
				dictionary_short_version += [dictionary[i]]

	number_list = []
	answer_list = []
	# 把單字組合數字化
	for i in range(16):
		number_list += [i]

	find_anagrams_helper(number_list, word_list, [], answer_list)

	# 印答案
	for i in range(len(answer_list)):
		print('Found: ' + answer_list[i])
	print('There are ' + str(len(answer_list)) + ' words in total.')


def find_anagrams_helper(number_list, word_list, current_list, answer_list):
	answer = ''
	for number in number_list:
		# first choose
		if len(current_list) == 0:
			current_list.append(number)
			go_to_recursion(number_list, word_list, current_list, answer_list)

		else:
			n = number - current_list[-1]

			if number in current_list:
				pass

			elif number % 4 == 0:
				if n == 4 or n == -4 or n == -1 or n == 3 or n == -5:
					current_list.append(number)
					go_to_recursion(number_list, word_list, current_list, answer_list)

			elif number % 4 == 1 or number % 4 == 2:
				if -5 <= n <= -3 or -1 <= n <= 1 or 3 <= n <= 5:
					current_list.append(number)
					go_to_recursion(number_list, word_list, current_list, answer_list)

			elif number % 4 == 3:
				if n == 4 or n == -4 or n == 1 or n == -3 or n == 5:
					current_list.append(number)
					go_to_recursion(number_list, word_list, current_list, answer_list)

	if len(current_list) >= 4:
		# 長度超過4以後開始跟字典對答案
		for i in range(len(current_list)):
			answer += word_list[current_list[i]]
		if answer not in answer_list and answer in dictionary_short_version:
			answer_list += [answer]
			# 若有在字典內，要繼續將字的長度延伸
			go_to_recursion_over4(number_list, word_list, current_list, answer_list)


def go_to_recursion(number_list, word_list, current_list, answer_list):
	# 搜尋字典是否有相同的字首 有才進recursion
	answer = ''
	for i in range(len(current_list)):
		answer += word_list[current_list[i]]
	if has_prefix(answer) is True:
		# explore
		find_anagrams_helper(number_list, word_list, current_list, answer_list)
	# un-choose
	current_list.pop()


def go_to_recursion_over4(number_list, word_list, current_list, answer_list):
	# 搜尋字典是否有相同的字首 有才進recursion
	answer = ''
	for i in range(len(current_list)):
		answer += word_list[current_list[i]]
	if has_prefix(answer) is True:
		# explore
		find_anagrams_helper(number_list, word_list, current_list, answer_list)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(dictionary_short_version)):
		if dictionary_short_version[i].startswith(sub_s) is True:
			return True


if __name__ == '__main__':
	main()
