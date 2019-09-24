student1 = {
    'name':'Arya Stark',
    'stream': 'Many Faces',
    'grade': 10,
    'complete modules': ['sword', 'augmented senses', 'no face']
}

students = {
    'studen1': student1,
    'student2': {
        'name': 'Stirling Archer',
    'stream': 'Chaos',
    'grade': 5,
    'complete modules': ['danger zone', 'robust liver', 'mummy issues']
    }
}
counter = 1    # starting the list at 1 then counting each key
for key1 in students:    # this is going into dict students
        print ('///////////////////////////////////////////////////')
        counter = 1    #reseting the counter for the start of each cycle
        for key2 in students[key1]:  #going into the dict in the dict students
            print(counter,'.', key2, ':', students[key1][key2])
            counter += 1       #incrementing the counter for each key

