# the game POP AND TOK
# multiple of 3 are POP
# multiple of 5 are TOK
# multiples of 3 and 5 are POPTOK
user_start = input('do you want to start the game(yes/no)?').lower()

while user_start == 'yes':

    number = int(input('input a number'))
    counter = 0
    while counter <= number:

        if counter == 0:
            print(0)
        elif counter % 3 == 0 and counter % 5 == 0:
            print('POPTOK')
        elif counter % 3 == 0:
            print('POP')
        elif counter % 5 == 0:
            print('TOK')
        else:
            print(counter)
        counter += 1

    user_start = input('do you want to carry on playing? (yes/no)')
    while True:
        if user_start =='yes':
            play = True
            break
        elif user_start =='no':
            play = False
            break
        else:
            user_start = input('do you want to carry on playing? (yes/no)')


