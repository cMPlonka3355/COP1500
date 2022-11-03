#Connor Plonka
#The following is a quiz on some basic concepts and commands for Introduction to Computer Programming.
#sources used:
#https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

import sys
import random


def yes_or_no(choice):
    if choice == "Y":
        return True
    else:
        return False


def math_questions():
    operators = ["+", "-", "*", "/", "**", "//", "%"]
    operation = operators[random.randint(0, 6)]
    first_num = random.randint(1, 15)
    second_num = random.randint(1, 15)
    correct_answer = None
    user_answer = None

    if operation == "+":
        correct_answer = first_num + second_num
        question = str(first_num) + " + " + str(second_num) + " = "
        user_answer = float(input(question))
    elif operation == "-":
        correct_answer = first_num - second_num
        question = str(first_num) + " - " + str(second_num) + " = "
        user_answer = float(input(question))
    elif operation == "*":
        correct_answer = first_num * second_num
        question = str(first_num) + " * " + str(second_num) + " = "
        user_answer = float(input(question))
    elif operation == "/":
        correct_answer = round(first_num / second_num, 2)
        question = str(first_num) + " / " + str(second_num) + " = "
        user_answer = float(input(question))
    elif operation == "**":
        correct_answer = first_num ** 3
        question = str(first_num) + " ** 3 = "
        user_answer = float(input(question))
    elif operation == "//":
        correct_answer = first_num // second_num
        question = str(first_num) + " // " + str(second_num) + " = "
        user_answer = float(input(question))
    elif operation == "%":
        correct_answer = first_num % second_num
        question = str(first_num) + " % " + str(second_num) + " = "
        user_answer = float(input(question))

    if user_answer == correct_answer:
        return True
    else:
        return False


def string_questions():
    words = ["jargon", "gobbelygook", "fire", "is", "matador"]
    word_one = words[(random.randint(0, 4))]
    word_two = words[random.randint(0, 4)]
    word_format = random.randint(1, 4)
    correct_answer = None
    user_answer = None

    if word_format == 1:
        correct_answer = word_one + " " + word_two
        question = "print('" + word_one + "', '" + word_two + "')\n"
        user_answer = input(question)
    elif word_format == 2:
        correct_answer = word_one + word_two
        question = "print('" + word_one + "' + '" + word_two + "')\n"
        user_answer = input(question)
    elif word_format == 3:
        correct_answer = word_one + word_two
        question = "print('" + word_one + "', '" + word_two + "', sep='')\n"
        user_answer = input(question)
    elif word_format == 4:
        correct_answer = word_one + " " + word_two + "!"
        question = "print('" + word_one + "', '" + word_two + "', end='!')\n"
        user_answer = input(question)

    if user_answer == correct_answer:
        return True
    else:
        return False


def relational_questions():
    operators = ["==", "!=", ">", "<", ">=", "<="]
    chosen_operator = operators[random.randint(0, 5)]
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)
    correct_answer = None
    user_answer = None

    if chosen_operator == "==":
        correct_answer = str(first_num == second_num)
        question = str(first_num) + " == " + str(second_num) + " "
        user_answer = input(question)
    elif chosen_operator == "!=":
        correct_answer = str(first_num != second_num)
        question = str(first_num) + " != " + str(second_num) + " "
        user_answer = input(question)
    elif chosen_operator == ">":
        correct_answer = str(first_num > second_num)
        question = str(first_num) + " > " + str(second_num) + " "
        user_answer = input(question)
    elif chosen_operator == "<":
        correct_answer = str(first_num < second_num)
        question = str(first_num) + " < " + str(second_num) + " "
        user_answer = input(question)
    elif chosen_operator == ">=":
        correct_answer = str(first_num >= second_num)
        question = str(first_num) + " >= " + str(second_num) + " "
        user_answer = input(question)
    elif chosen_operator == "<=":
        correct_answer = str(first_num <= second_num)
        question = str(first_num) + " <= " + str(second_num) + " "
        user_answer = input(question)

    if user_answer == correct_answer:
        return True
    else:
        return False


def boolean_questions():
    operators = ["and", "or", "not"]
    chosen_operator = operators[random.randint(0, 2)]
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)
    third_num = random.randint(0, 20)
    fourth_num = random.randint(0, 20)
    correct_answer = None
    user_answer = None

    if chosen_operator == "and":
        correct_answer = str((first_num == second_num) and (third_num == fourth_num))
        question = str(first_num) + " == " + str(second_num) + " and " + str(third_num) + " == " + str(fourth_num) + " "
        user_answer = input(question)
    elif chosen_operator == "or":
        correct_answer = str((first_num >= second_num) or (third_num <= fourth_num))
        question = str(first_num) + " >= " + str(second_num) + " or " + str(third_num) + " <= " + str(fourth_num) + " "
        user_answer = input(question)
    elif chosen_operator == "not":
        correct_answer = str(not first_num > fourth_num)
        question = "not " + str(first_num) + " > " + str(fourth_num) + " "
        user_answer = input(question)

    if user_answer == correct_answer:
        return True
    else:
        return False


#Main Code
def main():

    #Introduction to the quiz. Gets name for the farewell message later
    print("This is the Introduction to Computer Programming Quiz. You will be tested on the basic concepts learned.")
    name = input("Please tell us your name. ")
    print("You will be given 20 example programming commands, and must correctly identify what their outputs are.")
    print("Any answers for math problems that result in an answer that is not an integer should be rounded to the "
          "second decimal place.")

    try_again = True

    while try_again:
        score = 0
        for question in range(20):
            selection = random.randint(1, 4)
            print(question + 1, end=". ")
            if selection == 1:
                answered_correctly = math_questions()
                if answered_correctly:
                    score += 1
            elif selection == 2:
                answered_correctly = string_questions()
                if answered_correctly:
                    score += 1
            elif selection == 3:
                answered_correctly = relational_questions()
                if answered_correctly:
                    score += 1
            elif selection == 4:
                answered_correctly = boolean_questions()
                if answered_correctly:
                    score += 1

    #farewell message, as well as reminder for the user to tally their score for the quiz.
        print("you have completed the quiz.")
        if score == 20:
            print("Yippee! " * 2, "You got all the questions correct", sep='', end="!\n")
        elif score > 14:
            print("You didn't get them all correct, but you passed.")
        else:
            print("YIKES! You really need to study more.")

        try_again_choice = input("Would you like to try the quiz again? Y/n ")
        try_again = yes_or_no(try_again_choice)

    print("Have a ", "lovely " * 2,  "day " + name + ". :)", sep="")

#runs Main Code
main()