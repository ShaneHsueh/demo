"""
File: anagram.py
Name: Shane
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dictionary = []
dictionary_short_version = []


def main():
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    word = input('Find anagrams for: ')
    read_dictionary()

    start = time.time()
    find_anagrams(word)
    end = time.time()

    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dictionary
    with open(FILE, 'r') as f:
        for line in f:
            dictionary += line.split()


def find_anagrams(s):
    global dictionary_short_version

    # 創造一本新字典 裡面只含字數一樣，且字母也都一樣的單字
    for i in range(len(dictionary)):
        if len(s) == len(dictionary[i]):
            correct = 0
            for j in range(len(s)):
                if dictionary[i][j] not in s or s[j] not in dictionary[i]:
                    break
                else:
                    correct += 1
            if correct == len(s):
                dictionary_short_version += [dictionary[i]]

    number_list = []
    answer_list = []
    # 把單字組合數字化
    for i in range(len(s)):
        number_list += [i]

    find_anagrams_helper(number_list, [], s, answer_list)

    # 印答案
    for i in range(len(answer_list)):
        print('Searching...')
        print('Found: ' + answer_list[i])
    print('Searching...')
    print(str(len(answer_list)) + ' anagrams: ' + str(answer_list))


def find_anagrams_helper(number_list, current_list, word, answer_list):
    answer = ''
    # 字串長度滿的時候丟進答案清單
    if len(number_list) == len(current_list):
        for i in range(len(current_list)):
            answer += word[current_list[i]]
        if answer not in answer_list:
            answer_list += [answer]

    else:
        # 用數字排列單字可變化的組合
        for number in number_list:
            if number in current_list:
                pass
            else:
                # choose
                current_list.append(number)
                # 搜尋字典是否有相同的字首 有才進recursion
                answer = ''
                for i in range(len(current_list)):
                    answer += word[current_list[i]]
                if has_prefix(answer) is True:
                    # explore
                    find_anagrams_helper(number_list, current_list, word, answer_list)
                # un-choose
                current_list.pop()


def has_prefix(sub_s):
    for i in range(len(dictionary_short_version)):
        if dictionary_short_version[i].startswith(sub_s) is True:
            return True


if __name__ == '__main__':
    main()
