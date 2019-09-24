respond = input('talk to your teacher')
while True:
    if '?' in respond:
        print('HAHAHA! AHAHAHAHHA!! OMG! WHAT a silly question! Go back TO SCHOOL!')
    elif '!' in respond:
        print('YES! YESS! I WANT YOU TO BE MOTIVATED!! YES!')
    elif respond == "I'm a doctor":
        print('WELLL DONE! YOU can now talk to me')
        break
    else:
        print('Go back to school!')
    respond = input('say something else to your teacher')