# This is a practice on if statement
'''
Easy-Level Python Exercises
Odd or Even Checker:
Write a program that takes an integer input from the user and 
checks if the number is odd or even. Print "Even" if the number is even, and "Odd" if it is odd.
'''
question = int(input('Enter a number: '))
reminder = question % 2 == 0
formula = question % 2
if (reminder):
    print('The number is even since the reminder is:', formula)
else:
    print('The number is Odd, since it have a reminder of: ', formula )


'''
Simple Calculator:
Create a program that takes two numbers and a mathematical 
operator (+, -, *, /) as input from the user and performs the operation. 
Use if, elif, and else statements to determine the operation and print the result.
'''
number_one= int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))
operator_choice = input('Enter the operator, (+, -, *, /): ')

while operator_choice != '+' and operator_choice != '-' and operator_choice != '*' and operator_choice != '/':
    print('Wrong selection!')
    operator_choice = input('Please Enter the operator, (+, -, *, /): ')

if operator_choice == '+':
    answer = number_one + number_two
    print('The addition of number_one and number_two is: ', answer)
elif operator_choice == "-":
    answer = number_one - number_two
    print('The substraction of number_one from number_two is: ', answer)
elif operator_choice == '*':
    answer = number_one * number_two
    print('The multiplcation of number_one with number_two is: ', answer)
elif operator_choice == "/":
    answer = number_one / number_two
    print('Number_one divided by Number_two gives us: ', answer)
else:
    answer = 'Wrong input'

'''
Grade Checker:
Write a program that takes a numeric grade (0-100) as input and prints the corresponding letter grade using the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F
'''
grade_point = 59
if grade_point >= 90 and grade_point <= 100:
    grade_letter = 'A'
    print('Any grade between 90-100 receives grade letter: ', grade_letter)
elif grade_point >=80 and grade_point <= 89:
    grade_letter = 'B'
    print('Any grade between 80-89 receives grade letter: ', grade_letter)
elif grade_point >= 70 and grade_point <= 79:
    grade_letter = 'C'
    print('Any grade between 70-79 receives grade letter: ', grade_letter)
elif grade_point >=60 and grade_point <= 69:
    grade_letter = 'D'
    print('Any grade between 60-69 receives grade letter: ', grade_letter)
else:
    grade_letter = 'F'
    print('Any grade below 60 receives garde: ', grade_letter)

'''
Vowel or Consonant Checker:
Write a program that takes a single character input from the user and checks 
whether it is a vowel (a, e, i, o, u) or a consonant. If the input is not a letter, print an error message.
'''
user_input = input('Enter any alphabatic character to check if it is a vowel or a constant:  ')
if user_input != str(input):
    print('Please enter a letter character: ')
else:
    user_input = input('Please enter a letter character: ')
if user_input == 'A' or user_input == 'E' or user_input == 'I' or user_input == 'O' or user_input == 'U':
    user_inputs = user_input.lower()
    print('The letter character is vowel: ', user_inputs)
else:
    print('The letter character is not a vowel: ', user_input)

'''
Simple Login System:
Create a program that takes a username and password as input. 
If the username is "admin" and the password is "1234", print "Access Granted". 
Otherwise, print "Access Denied".
'''

enter_user_name = input('Enter a user name: ')
enter_passcode = input('Enter the password: ')
if enter_user_name == 'admin' and enter_passcode == '1234':
    print('Access Grandted')
else:
    print('Access Denied')
    
'''
Weather Suggestions:
Write a program that asks the user for the current temperature and suggests an activity based on 
the following conditions:

If the temperature is above 30°C, suggest "Go swimming."
If the temperature is between 20°C and 30°C, suggest "Go for a walk."
If the temperature is below 20°C, suggest "Stay inside and read a book."
'''
temp = int(input('What is the weather looks like today: '))
if temp >= 30:
    print('Today is a good weather it is', temp,  'You can go swimming')
elif temp >= 20 and temp <= 30:
    print('The weather is ' + str(temp) + ' and it is good for a walk')
else:
    print('The weather is', {temp}, 'and i suggest to stay home and do some reading1')

'''
Age Group Finder:
Write a program that takes an age as input and categorizes it into different age groups:
0-12: Child
13-19: Teenager
20-64: Adult
65 and above: Senior
'''

age = int(input('Please enter your age to find your category: '))
if age <= 12:
    ages = 'Child'
    print('The age group is: ' + ages)
elif age >= 13 and age <= 19:
    ages = 'Teenager'
    print('The age ground is: '+ ages)
elif age >= 20 and age <= 64:
    ages = 'Adult'
    print('The age group is: ' + ages)
else:
    ages = 'Senior'
    print('The age group is: ' + ages)

'''
Number Comparison:
Write a program that takes two numbers as input from the user 
and prints which one is greater or if they are equal.
'''
number_one = int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))

# check if n1 is greater than the n2
# check if n2 is greater than n2
# check if n1 = n2 and vise versa 
if number_one > number_two:
    print(str(number_one)+  ' is greater than ' + str(number_two))
elif number_two > number_one:
    print('The second number is ' + str(number_two)+ ' is greater than ' + str(number_one))
elif number_one == number_two:
    print(str(number_one) + ' is equal to ' + str(number_two))
else:
    print('Error')


"""
Password Strength Checker:
Write a program that takes a password as input and checks its strength based on the following conditions:

If the password length is less than 6 characters, print "Weak Password".
If the password length is between 6 and 10 characters and contains only letters or digits, print "Moderate Password".
If the password is more than 10 characters long and contains a mix of letters, digits, and special characters, print "Strong Password".
"""

"""
Simple ATM System:
Create a program that simulates an ATM. The user has a fixed balance of $1,000. Allow the user to 
"deposit," "withdraw," or "check balance." Use if, elif, and else statements to 
determine the operation and display the updated balance.
"""


print('                            ')
print(' WELCOME TO XXXX ATM SERVICE')
print('                            ')
print('                            ')
atm_prompt = input(" What do you like to do today?\n Enter 'D' to deposit.\n Enter 'W' to withdraw. \n Enter 'C' to check balance: ")
current_balance = 1000
if atm_prompt == 'D':
    # global current_balance
    atm_user = int(input('How much money would you like to deposite today? '))
    atm_calc = current_balance + atm_user
    print('The amount you deposited is: ' , atm_user ,  'and you current balance is: ', atm_calc)
elif atm_prompt == 'W':
    atm_user = int(input('How much money would you like to withdraw from your account? '))
    amount_withdraw = atm_user
    atm_calc = current_balance - atm_user
    print('The amount you withdraw is ', amount_withdraw, 'and your current balance is: ', atm_calc)
elif atm_prompt == 'C':
    atm_calc = current_balance
    print('Your current balance is: ', atm_calc)
else:
    atm_prompt == 'Wrong selection!'
    atm_user = "What do you like to do today?\n Enter 'D' to deposit.\n Enter 'W' to withdraw. \n Enter 'C' to check balance:"
    print(atm_user)

'''
Traffic Light Simulation:
Write a program that takes a color (red, yellow, green) as input and prints the appropriate action:

Red: "Stop"
Yellow: "Ready to Stop"
Green: "Go"

'''
traffic_color = input('What is the color of the light?: ')
if traffic_color == 'Red':
    traffic_sign = 'Stop'
    print('The color of the traffic light is ' + traffic_color + ' and you MUST STOP!')
elif traffic_color == 'Yellow':
    traffic_sign = 'Ready to Stop'
    print('The color is of the traffic is', traffic_color, 'and you should prepare to stop')
else:
    traffic_color == 'Green'
    traffic_sign = 'Go'
    print('The traffic sign is', traffic_color, 'and You can Go')

