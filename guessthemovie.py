import random
movies = ["sadak 2", "bhag milkha bhag", "raabta", "avengers age of ultron", 'judwa 2', "endgame", '3 idiots', '_']
print("Hangman Game Movies")

    
p = random.randint(0, len(movies)-2)
movie_selected = movies[p]
for x in movie_selected:
    if x.isalpha() or x.isdigit():
        print('_ ', end='')
    else:
        print('  ', end='')
print()
lives = 10
words_guessed_correct = []
no_of_words_guessed = 0
distinct_words = []
for _ in movie_selected:
    if _ not in distinct_words and _ != ' ':
        distinct_words.append(_)

while True:
    if lives == 0:
        print("you lost all your lives")
        print("Game Over")
        break
    if len(words_guessed_correct) == len(distinct_words):
        print()
        print("Congrats you won!! Game Over")
        break
    print()
    print(f"You have {lives} lives left".format(lives))
    ans = input()
    if ans in distinct_words:
        print("You guessed a word")
        # print(distinct_words, words_guessed_correct)
        if ans not in words_guessed_correct:
            words_guessed_correct.append(ans)
        for x in movie_selected:
            if x in words_guessed_correct:
                print(x, end=' ')
            elif x == ' ':
                print(' ', end=' ')
            else:
                print(movies[-1], end=' ')
    else:
        print("wrong word, try again")
        lives -= 1
