#PyQuiz made by PB PRIME PLAY

print('Welcome to the PyQuiz!')
print('RULES')
print('1. Please write all answers in CAPSLOCK.')
print('2. Each correct answer gives 5 points.')
a=input('What is your name? : ')
print('Welcome to the Quiz,',a)
b=input('What is the largest city on Earth by area? : ')
if b=='NEW YORK':
    score=5
    print("That's right! You now have",score,'points.')
else:
    score=0
    print('Sorry. That is incorrect. The correct answer is NEW YORK. You now have',score,'points.')
c=input('What is the largest creature on Earth? : ')
if c=='BLUE WHALE':
    score=score+5
    print("That's right! You now have",score,'points.')
else:
    score=score+0
    print('Sorry. That is incorrect. The correct answer is BLUE WHALE. You now have',score,'points.')
print('Thanks for playing,',a,'. Your final score is',score,'points.')
