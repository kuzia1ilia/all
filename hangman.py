def hangman(word):
    wrong=0
    stages=["",
            "______     ",
            "      |    ",
            "      o    ",
            "     /|\   ",
            "     / \   ",
            ]
    rletters=list(word)
    board=["_"]*len(word)
    x=False
    print("Добропожаловать на казнь")
    while wrong<len(stages)-1:
        print("\n")
        msg="Введите букву:"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]="$"
        else:
            wrong+=1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_"not in board:
            print("Вы выйграли!Было загаданно слово:")
            print(" ".join(board))
            x=True
            break
    if not x :
        print("\n".join(stages[0:wrong]))
        print("ВЫ НЕ УГАДАЛИ")
hangman==(["кот","бор","ной"])
import random
random.randint(hangman)

