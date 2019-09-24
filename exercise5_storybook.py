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
     'book1': {'beginning':input('what is the beginning of your first story?'),
               'middle':input('what is the middle of your first story?'),
               'end':input('what is the end of your first story?'),
               'hero': input('who is the hero?')},
     'book2': {'beginning': input('what is the beginning of your second story?'),
              'middle': input('what is the middle of your second story?'),
              'end': input('what is the end of your second story?'),
              'hero': input('who is the hero?')},
     'book3': {'beginning':input('what is the beginning of your third story?'),
               'middle':input('what is the middle of your third story?'),
               'end':input('what is the end of your third story?'),
               'hero': input('who is the hero?')}
               }
print ('My storybook :D')
for key1 in storybook:
    print (key1)
    print('///////////////////')
    for key2 in storybook[key1]:
        print(key2, ':', storybook[key1][key2])
    print('///////////////////')




