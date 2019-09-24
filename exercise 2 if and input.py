rating = input('what is the film rating?').strip().lower()    # strip() removes spaces and lower() puts it into lower case for the if
if rating == '18':
    print('No one younger than 18 may see an 18 film in a cinema.')
elif rating == '15':
    print('No one younger than 15 may see a 15 film in a cinema.')
elif rating == '12a' or rating == '12':
    print('Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.')
elif rating == 'pg':
    print('General viewing, but some scenes may be unsuitable for young children')
elif rating == 'universal' or rating == 'u':
    print('everyone can watch')
else:
    print('this is not an official film rating')