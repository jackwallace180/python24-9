
# keeps looping an iterating until a condition is met
# OR it comes into a break statement

#while<condition>:
    #block
    # if <condition>:
      #break

#import time
#counter = 0
#while counter <10:
    #print(counter)
    #print('hello')
    #counter += 1
    #time.sleep(1)
#counter = 0
#while True:
    #print(counter)
    #print('WAAAAHHHHHH')
    #if counter > 10:
        #break
    #counter+=1
cars = ['volvo', 'skoda', 'ferrari', 'lambo']
counter = 0
max_length = len(cars)
while max_length > counter:
    print(counter +1, '-',cars[counter])
    counter += 1
