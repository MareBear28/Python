num2Guess = 5
urGuess = input('Enter an integer b/n 1 and 10:\t')
play = 'Y'
while(play.upper() == 'Y'):
     while((not(urGuess.isdigit()))or((int(urGuess)<1)or(int(urGuess)>10))):
          print('Invalid Entry: Input needs to be an integer between 1 & 10')
          urGuess = input('Enter an integer b/n 1 and 10:\t')
     if(int(urGuess) == num2Guess):
          print('Great! You guessed it!')
     else:
          print('Sorry, wrong number')
     play = input('Want to play again? Y/N:\t')
     if(play.upper() == 'Y'):
          urGuess = input('Enter an integer b/n 1 and 10:\t')
if(play.upper()=='N'):
     print('End of program.')
        
    
