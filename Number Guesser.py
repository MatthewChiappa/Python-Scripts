print 'Please think of a number between 0 and 100!'

guess = 50
high = 100
low = 0

while True:
    input = raw_input('Is your secret number ' + str(guess) + '? Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly. ');
    if(input == 'h'):
        high = guess
        guess = (low + guess)/2
    elif(input == 'l'):
        low = guess
        guess = (high + guess)/2
    elif(input == 'c'):
        break

print 'Game over. Your secret number was:', guess 
        
