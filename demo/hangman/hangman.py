"""
File: hangman.py
Name: Hsueh Shane
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = random_word()
    print(word)
    guess(word)


def guess(word):
    time = N_TURNS  # 剩餘生命
    display = ""    # 目前猜到的結果
    for i in range(len(word)):
        display += '-'
    print('The word looks like: ' + display)
    print('You have ' + str(time) + ' guesses left.')
    while True:
        while True:
            answer = input('Your guess: ')
            if answer.isalpha() and len(answer) == 1:  # 確認輸入資訊是否為單一英文字母，並將其大寫化)
                answer = answer.upper()
                break
            print('illegal format.')       # 不正確的話則迴圈要求重新輸入

        if answer in word:                 # 如果有猜到答案
            renew_display = ""
            for i in range(len(word)):
                if word[i] == answer:      # 更新猜到的結果
                    renew_display += answer
                else:
                    renew_display += display[i]
            display = renew_display
            print('You are correct!')
            print('The word looks like: ' + renew_display)
            print('You have ' + str(time) + ' guesses left.')
            if renew_display == word:                                         # 全部猜到的話跳出迴圈
                print('You are correct!\nYou win!!\nThe word was: ' + word)
                break
        elif answer not in word:   # 如果沒猜到
            time -= 1              # 生命扣1
            print("There is no " + answer + "'s in the word.")
            if time > 0:
                print('You have ' + str(time) + ' guesses left.')
                print('The word looks like: ' + display)
            else:                                      # 生命為0時跳出迴圈
                print('You are completely hung :(')
                print('The word was: ' + word)
                break


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
