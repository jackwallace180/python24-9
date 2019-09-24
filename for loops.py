cars = ['skoda felica FUN', ' fiat panda 4x4','mustang ford', 'corvette']

# for <placeholder> in <iteratable>:
    # block of code
    # indented get run every iteration
# don't forget the colon

for car in cars:
    breakpoint()   #breakpoint will run 1 iteration at a time untill you type continue
    print(car)

embedded_list = [['filipe','francis'], ['mustapha','david','jillian']]

for data in embedded_list:
    print(data)
    for name in data:
        print(name.capitalize())
