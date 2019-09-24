# control flow - if statement
# controls where the code is going to go,
# depending on the result of the evaluation that return true or false
# it runs a block of code or not

# if <condition>:
    # block  - blocks do stuff
# elif <condition>:
#   block
# else:
#    block

weather = 'storm'

if 'rain' in weather and 'storm' in weather:
    print('stay home')
elif weather == 'rain' or weather == 'storm':
    print('bring an umbrella')
elif weather == 'snow':
    print('bring a scarf')
else:
    print('the weather isnt bad')