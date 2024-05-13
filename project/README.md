# __BLACKJACK GAME__
#### Video Demo: https://youtu.be/ny7GNOvIoxQ


#### Description:
This project is a blackjack game where the user can deposit, play with money and see your money


## __Libraries__

* random — Generate pseudo-random numbers. Documentation:https://docs.python.org/3/library/random.html
# There are two modules/libraries required to install, which are specified in the requirements.txt file.
* pyfiglet==1.0.2
* tabulate==0.9.0

# __Install Libraries__
To install the library is with this command
"""
pip install -r requirements.txt

"""

## __USAGE__

Write in the terminal

"""python project.py"""

Will return a table as follows:
"""
+---------+-----------+
| Menu    |   Options |
+=========+===========+
| Deposit |         1 |
+---------+-----------+
| Play    |         2 |
+---------+-----------+
| Money   |         3 |
+---------+-----------+
| Exit    |         4 |
+---------+-----------+
Write the option:
"""
The user can select 4 options between 1-4

## __Option 1__

if you select option 1 will return

"""
Deposit:

"""
The user can write the amount of money they want to deposit
if you dont put a valid input will return a message
"""
Write a Valid option
"""

## __Option 2__

if you select option 2 will return

"""
Bet:
"""
The user can write the amount of money the want to play
if you dont put a valid input will return a message
"""
Write a valid bet
"""
if the user write a valid bet
the game will start

### Example
"""
Your cards:Q♣, 9♣
Dealer hand:9♠
Hit or Stand:
"""
you can write hit or stand
hit = generate a new card
stand = stay with the cards

the values of the cards are:
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
10 = 10
j = 10
q = 10
k = 10
and the a have two values
a = 1 or a = 11
soft      hard

### Win or lose
to win you need to have 21 points or have more points that the dealer
if you pass 21 points you lose
the dealer will hit until he have less than 17 points

if you win your bet will multiply x2
if you lose you will lose your bet

## __Option 3__
if you select option 3
you can see your amount of money

### example
if you have $100
will return
"""
___  ___                          _    __  _____  _____
|  \/  |                       _ | |  /  ||  _  ||  _  |
| .  . | ___  _ __   ___ _   _(_) __) `| || |/' || |/' |
| |\/| |/ _ \| '_ \ / _ \ | | | \__ \  | ||  /| ||  /| |
| |  | | (_) | | | |  __/ |_| |_(   / _| |\ |_/ /\ |_/ /
\_|  |_/\___/|_| |_|\___|\__, (_)|_|  \___/\___/  \___/
                          __/ |
                         |___/
"""

## __Option 4__
This option is to exit the program with this message

"""
________________________________________  ___________
__  ____/_  __ \_  __ \__  __ \__  __ ) \/ /__  ____/
_  / __ _  / / /  / / /_  / / /_  __  |_  /__  __/
/ /_/ / / /_/ // /_/ /_  /_/ /_  /_/ /_  / _  /___
\____/  \____/ \____/ /_____/ /_____/ /_/  /_____/

"""
