# Draw the hangman based on the number of wrong guesses
def draw_hangman(wrong_guesses):
    hangman = [
        r'''
           ____
          |    |
          |    
          |   
          |   
          |
        ======''',
        '''
           ____
          |    |
          |    O
          |   
          |   
          |
        ======''',
        '''
           ____
          |    |
          |    O
          |    |
          |   
          |
        ======''',
        '''
           ____
          |    |
          |    O
          |   /|
          |   
          |
        ======''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |   
          |
        ======''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |   / 
          |
        ======''',
        '''
           ____
          |    |
          |    O
          |   /|\\
          |   / \\
          |
        ======'''
    ]
    print(hangman[wrong_guesses])