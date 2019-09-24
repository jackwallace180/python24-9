# Story book!
# Create a dictionary with 3 stories inside! like a book :)
# each story should be it's own dictionary with:
    # beggining, middle, end
    # hero
# Iterate over the the book, and print out each story! PRINT ALL of them :)
# Formatted of course
# hints:
 # you already built a dictionary with a story
 # You already have something to prompt user for input & build dictionaries
 # Now what we want is to create a book that hold 3 stories

# extra:
 # stick it in a while loop so we continue to listen to stories :)
 # It would be nice to be able to read only one story

storybook = {
     'book1': {'beggining':'there was a man called jack',
               'middle':'he was very bad at coding',
               'end':'filipe taught him very well and now he can code amazingly',
               'hero':'filipe'},
     'book2': {'beggining':'there was a man called josh',
               'middle':'he was very bad at swimming',
               'end':'mansuel taught him very well and now he can swim amazingly',
               'hero':'mansuel'},
     'book3': {'beggining':'there was a man called vishnu',
               'middle':'he was very bad at remembering peoples names',
               'end':'abror taught him everyones names and now he can greet everyone amazingly',
               'hero':'abror'}

}
for key1 in storybook:
    print ('title of book:',key1)
    print('///////////////////')
    for key2 in storybook[key1]:
        print(key2, ':', storybook[key1][key2])
    print('///////////////////')

