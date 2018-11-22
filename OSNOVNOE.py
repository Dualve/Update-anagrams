import Chek as ch
import random

word_tuple = (["кот", "лес", "дом", "дед", "лёд", "род", "рис", "мир"],
              ["стол", "стул", "лист", "вода", "мерч", "болт", "лорд", "день", "пуля"],
              ["абзац", "аборт", "авеню", "аврал", "графа", "аллея", "алмаз", "алыча", "амбар"],
              ["предшествовать", "выгравированный", "государственный", "правительство", "самоотверженность"],
              ["common", "ability", "letter", "kingdom", "boyfriend", "campus", "consist", "include", "political"])

while True:
    starter = ch.chekInput("""
        If you want to start programme press 1,
        else press 2 for exit.\n""", int)

    if starter == 1:
        choice = ch.chekInput("""
        Choice the item of menu:
        1) Easy level.(word consists of 3 letters)
        2) Medium level.(word consists of 4 letters)
        3) Hard level.(word consists of 5 letters)
        4) Impossible level.(word consists of 6+ letters)
        5) English words level.\n""", int)

        if choice >= 1 and choice <= 5:

            word = list(word_tuple[choice - 1])
            word = str(word[random.randint(0, len(word) - 1)])
            word1 = list(word)
            random.shuffle(word1)
            print(" ".join(word1))
            print("\n* if you do not know the answer , click '?' *\n")

            answer_checker = 0
            try_checker = 0

            while True:
                word1 = ch.chekInput("Enter your variant of word:\n",str)
                if word1 == "?":
                    if answer_checker < choice:
                        print(word[answer_checker])
                        answer_checker += 1
                        print("You have", choice - answer_checker, "tips.")
                        continue
                    else:
                        print("You haven't tips.")
                        continue

                if word1.lower() == word:
                    print("Awesome! You guessed!")
                    break

                else:
                    try_checker += 1
                    if try_checker == choice:
                        print("Wrong,right variant is {}".format(word))
                        break
                    else:
                        print("Wrong.You have" ,choice - try_checker,"attempts.")

        else:
            print("Wrong menu item.")
            continue

    elif starter == 2:
        print("Goodbye.")
        break

    else:
        print("Wrong menu item.")
        continue
