Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

wordbank = ['engineering','bhimavaram','btech','vishnu','women',
            'college','degree','hangman','project','wise','group','google',
            'spontaneous','python','pycharm','game','advanced','expertise']

bored = True
while bored:
    # draw gallows
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.goto(-135,-35)

    word = random.choice(wordbank)

    for i in word:
        turtle.write('_ ', True, font=("Courier", 14, "normal"))

    correct = []
    wrong = 0
    terminate = False
    while wrong < 6 and not terminate:
        letter = turtle.textinput('Hangman','Guess a letter:')
        turtle.goto(-135,-35)
        time.sleep(1)
        if letter not in correct:
            for i in word:
                if i == letter:
                    turtle.write(letter.upper() + ' ', True, font=("Courier", 14, "normal"))
                    time.sleep(1)
                    correct += letter
                else:
                    turtle.write('_ ', True, font=("Courier", 14, "normal"))
        if letter not in word:
            wrong += 1
            drawMan(wrong)
        if wrong == 6:
            turtle.goto(-135,-35)
            for i in word:
                if i in correct:
                    turtle.write('_ ', True, font=("Courier", 14, "normal"))
                else:
                    turtle.write(i.upper() + ' ',True, font=("Courier", 14, "normal"))
                    time.sleep(1)
            turtle.goto(-74, -60)
            turtle.write('Sorry, you lose!',True, align='center', font=("Courier", 14, "normal"))
            time.sleep(1)
        if len(correct) == len(word):
            turtle.goto(-74, -60)
            turtle.write('Congratulations you won!!!',True,align='center', font=("Courier", 14, "normal"))
            time.sleep(1)
            terminate = True

