#functions and functional programming

#functions take in arguements
#they have a block of code to run
#they output (return) something
#they need to be called to be executed

# good practices:
# good names (humans understand +descriptive)
# following convention (lowercase and separated with underscore)
# they should be atomic and small
      # this means they are testable
      # reduces technical debt
# comments when appropriate
# DO NOT PRINT IN FUNCTIONS --- Return
#separation of concerns
#TDD

# functions allow us to be DRY
# Dont Repeat Yourself

# aim for cleaner and DRYer and testable


def full_name(f_name, l_name):
    full = f_name + ' ' + l_name
    return full
print(full_name('jack','wallace'))

# this is the basis of a test (returns true or false)
# assertion (check for expected outcomes)
print(full_name('jack', 'wallace') == 'jack wallace')