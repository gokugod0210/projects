"""
flow of project
1.user will choose r/p/s
2.computer will also choose
3.print the result

many cases

"""
import random
options=['rock','paper','scissor']
user_choice=input("enter a choice: ")
comp_choice=random.choice(options)
if user_choice==comp_choice:
    print('tie')
elif user_choice=='rock':
    print('wins')
elif comp_choice=='rock':
    print('lose')
elif user_choice=='paper' and comp_choice=='scissor':
    print('lose')
elif user_choice=='scissor' and comp_choice=='paper':
    print('win')

print(f"comp choice={comp_choice}")
