import random
answers = ['''Undoubtedly', 'I think so', 'It's not clear yet, try again', 'Don't even think about it', 
'Foregone', 'Most likely', 'Ask later', 'My answer is no', 'No doubt', 
'Good prospects', 'Best not to tell', 'Not according to me, no', 'Definitely yes', 
'Signs say yes', 'Can't predict now', 'Prospects not good', 
'You can be sure of that', 'Yes', 'Concentrate and ask again', 'Very doubtful''']

print('''Hi, I'm a magic ball, and I know the answer to any question you have.''')
print('''What's your name?''') 
n = input()
print('Hi,', n)

while True:
    print('Enter a question so that the answer is YES or NO')
    question = input()
    print(random.choice(answers))
    print('Again? y/n')
    again = input()
    if again == 'y':
        continue
    else:
        print('Come back if you have any questions!')
        break