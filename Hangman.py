""" This is a simple hangman game """

pics=["""\t\t _____
        |     |
              |
              |
              |
              |""",
      """\t\t _____
        |     |
        ○     |
              |
              |
              |""",
      """\t\t _____
        |     |
        ○     |
        |     |
              |
              |""",
      """\t\t _____
        |     |
        ○     |
       /|     |
              |
              |""",
      """\t\t _____
        |     |
        ○     |
       /|\    |
              |
              |""",
      """\t\t _____
        |     |
        ○     |
       /|\    |
       /      |
              |""",
      """\t\t _____
        |     |
        ○     |
       /|\    |
       / \    |
              |"""
      ]

def play():

    word = "#introduce word here
    right = ['_'] * len(word)
    wrong = ''

    print('\n' * 2 + 'H A N G M A N')

    while True:
        print('\n' + 'Word: ' + ' '.join(right).capitalize())
        print('Wrong letters: ' + ' '.join(wrong))
        print(pics[len(wrong)])

        if ''.join(right).isalpha():
            print('You won! :)')
            break
        if len(wrong) >= len(pics) - 1:
            print('You lost! :(. It was {}'.format(word))
            break

        let = get_letter()

        if let in word:
            for i in range(len(word)):
                if let == word[i]:
                    right[i] = let
        elif let in wrong:
            print('You gave this letter already!')
        else:
            wrong = wrong + let

def get_letter():

    while True:
        letter = input('Guess a letter: ')
        if len(letter) == 1 and letter.isalpha() == True:
            return letter.lower()

play()
