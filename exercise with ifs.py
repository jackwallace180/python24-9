age = 12
drivers_lisense = True

if age >= 18 and drivers_lisense == True:
    print('you can vote and drive')
elif age >= 18 and drivers_lisense == False:
        print('you can vote but not drive')
elif age >= 17 and drivers_lisense == True :
    print('you can drive but not vote')
elif age >= 17 and drivers_lisense == False:
    print('you cant drive or vote')
elif age >= 16:
    print('you cant legally drink but your friends may have your back, you also cant drive')
else:
    print('you are too young go back to school!')