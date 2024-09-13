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


'''
Magic 8-Ball
The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

Magic 8-Ball, should I do this project?

We’ll be using the following 9 possible answers for our Magic 8-Ball:

Yes - definitely
It is decidedly so
Without a doubt
Reply hazy, try again
Ask again later
Better not tell you now
My sources say no
Outlook not so good
Very doubtful
The output of the program will have the following format:

[Name] asks: [Question]
Magic 8-Ball’s answer: [Answer]

For example:

Joe asks: Is this real life?
Magic 8-Ball's answer: Better not tell you now

Let’s get started!

Tasks
15/15 complete
Mark the tasks as complete by checking them off
Setting up

In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.


Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.


We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.

Generating a random number

In order for the answer to be different each time we run the program, we will utilize randomly generated values.

Note: This will be something new! But don’t worry, we will try to explain this topic thoroughly and also supply the code.

In Python, we can use the .randint() function from the random module to generate a random number from a range.

But first, let’s import this module so we can use its functions. Add this line of code to the top of magic8.py:

import random


Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:

random.randint(1, 9)

which will generate a random number between 1 (inclusive) and 9 (inclusive).

Next, add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.

Once you’re sure this is working as we expected, feel free to comment out this print() statement.

Control Flow

Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!

For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely”


Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

Recall that the 9 possible answers of the Magic 8-Ball are:

Yes - definitely

It is decidedly so

Without a doubt

Reply hazy, try again

Ask again later

Better not tell you now

My sources say no

Outlook not so good

Very doubtful


Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.

Seeing the result

Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format:

[Name] asks: [Question]

For example, when we run the program, the output should look something like:

Joe asks: Will I win the lottery?


Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:

Magic 8-Ball's answer: [answer]

For example, when running the program it should look something like:

Magic 8-Ball's answer: My sources say no


Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.

Run your program several times to see that it’s working as expected.

Optional Challenges

If you’re up for some more challenges, try implementing the following features to your program.

So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.

To do this, you will need to increase the range of randomly generated numbers and add additional elif statements for each new answer.


What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

 asks: Will I win the lottery?
Magic 8 Ball's answer: Outlook not so good

As you can see, the formatting of the output can use some improvement when there is no name provided.

We can address this by printing out just the question, such that it looks like the following:

Question: Will I win the lottery?
Magic 8-Ball's answer: Outlook not so good

You can implement this by creating an if/else statement such that:

If the name is an empty string, it will only print the question.
Else, the player’s name and question are both printed.

What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

To ensure that the fabric of reality is safe, we can create an if/else statement where:

If the question is an empty string, print out a message to the user.
Else, print the name and question, with the Magic 8-Ball’s answer.
Solution.

'''
import random
name = ' '
question = "Will i win the lottery?"
answer = ""

random_number = random.randint(1,11)
# print(random_number)
if random_number == 1:
  answer = 'Yes - definitly'
  print(answer)
elif random_number == 2:
  answer='It is decidedly so'
elif random_number == 3:
  answer ='Without a doubt'
elif random_number == 4:
  answer= 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer='Better not tell you know'
elif random_number == 7:
  answer ='My sources say no'
elif random_number == 8:
  answer= 'outlook not so good'
elif random_number == 9:
  answer ='Very doubtful'
elif random_number == 10:
  answer ='Very confidence'
elif random_number == 11:
  answer ='Try harder'
else:
  answer = 'Error'
if name == " ":
  print("Question ask: " + question)
else:
  print(name + " ask: " + question)
print("Magic 8-ball's answer: " + answer)

'''
Sal's Shipping
Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.
Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

Note that the walkthrough video for this project is slightly out of date — the walkthrough was done using a version of this project that uses functions. Feel free to come back to the video after having been introduced to functions!

'''


weight = 4.8
# ground shipping
if weight <= 2:
  cost = 20 + 1.50 * weight
  print('Ground shipping cost: ', cost)
elif weight > 2 and weight <= 6:
  cost = 20 + 3 * weight
  print('Ground shipping cost: ', cost)
elif weight > 6 and weight <= 10:
  cost = 20 + 4 * weight
  print('Ground shipping cost: ', cost)
elif  weight >10:
  cost = 20 + 4.75 * weight
  print('Ground shipping cost: ', cost)
else:
  cost = 'error'
  print('Ground shipping cost is not right: ', cost)

# Ground Shipping Premium
# 125
ground_Shipping_Premium = 125
print('You select ground shipping premium: ',  ground_Shipping_Premium)

# Drone Shipping
if weight <=2:
  cost = 4.50 * weight
  print('Drone shipping cost is : ', cost)
elif weight > 2 and weight <= 6:
  cost = 9 * weight
  print('Drone shipping cost is : ', cost)
elif weight > 6 and weight <= 10:
  cost = 12 * weight
  print('Drone shipping cost is : ', cost)
else:
  cost = 14.25 * weight
  print('Drone shipping cost is : ', cost)