"""Integration Project for Introduction to Computer Science
The following is code for a quiz, based on basic computer science principles such as math operators, string format,
relational operators, and boolean operators. Users can take the quiz multiple times.

Input:
    Name
    Answers to Questions
    Choice in Retaking Quiz
Output:
    Introductory Remarks and Needed Info
    Quiz Questions
    Message based on Grade
    Question on Retaking Quiz
Example:
    This is the Introduction to Computer Programming Quiz. You will be tested on the basic concepts learned.
    Please tell us your name. Connor
    You will be given 20 example programming commands, and must correctly identify what their outputs are.
    Any answers for math problems that result in an answer that is not an integer should be rounded to the
    second decimal place.
    Relational and Boolean questions will have an answer of True or False. Print questions will have answer of
    string.
    *20 RANDOM QUESTIONS*
        Example Questions and Answers:
            2 + 3 = 5

            print('fire' + 'is')
            fire is

            0 < 3 True

            4 == 4 and 5 == 9 False
            
    *GRADE MESSAGE*
        Example Message if Grade is 20/20:
            Yippee! Yippee! You got all the questions correct!

    Would you like to try the quiz again? Y/n n
    Have a lovely lovely day Connor. :)
Sources:
    https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/"""

__author__ = 'Connor Plonka'

import random


def yes_or_no(choice):
    """
    Returns True or False depending on input from user
    :param choice: string value
    :return: boolean
    """
    if choice.upper() == "Y":
        return True
    else:
        return False


def math_questions():
    """
    Gives the user a computer science based math question to solve, using python math operators
    Compares user answer to computer-made correct answer
    :return: boolean
    """
    operators = ["+", "-", "*", "/", "**", "//", "%"]
    operation = operators[random.randint(0, 6)]
    first_num = random.randint(1, 15)
    second_num = random.randint(1, 15)
    correct_answer = None
    user_answer = None
    question = None

    if operation == "+":
        correct_answer = first_num + second_num
        question = str(first_num) + " + " + str(second_num) + " = "
    elif operation == "-":
        correct_answer = first_num - second_num
        question = str(first_num) + " - " + str(second_num) + " = "
    elif operation == "*":
        correct_answer = first_num * second_num
        question = str(first_num) + " * " + str(second_num) + " = "
    elif operation == "/":
        correct_answer = round(first_num / second_num, 2)
        question = str(first_num) + " / " + str(second_num) + " = "
    elif operation == "**":
        correct_answer = first_num ** 3
        question = str(first_num) + " ** 3 = "
    elif operation == "//":
        correct_answer = first_num // second_num
        question = str(first_num) + " // " + str(second_num) + " = "
    elif operation == "%":
        correct_answer = first_num % second_num
        question = str(first_num) + " % " + str(second_num) + " = "

    get_answer = False
    while not get_answer:
        try:
            user_answer = float(input(question))
            get_answer = True
        except ValueError:
            print("You did not input a float number. Please try again.")

    if user_answer == correct_answer:
        return True
    else:
        return False


def string_questions():
    """
    Gives the user a computer science based string question to solve, using print statements formats
    :return: boolean
    """
    words = ["jargon", "gobbelygook", "fire", "is", "matador"]
    word_one = words[(random.randint(0, 4))]
    word_two = words[random.randint(0, 4)]
    word_format = random.randint(1, 4)
    correct_answer = None
    question = None

    if word_format == 1:
        correct_answer = word_one + " " + word_two
        question = "print('" + word_one + "', '" + word_two + "')\n"
    elif word_format == 2:
        correct_answer = word_one + word_two
        question = "print('" + word_one + "' + '" + word_two + "')\n"
    elif word_format == 3:
        correct_answer = word_one + word_two
        question = "print('" + word_one + "', '" + word_two + "', sep='')\n"
    elif word_format == 4:
        correct_answer = word_one + " " + word_two + "!"
        question = "print('" + word_one + "', '" + word_two + "', end='!')\n"

    user_answer = input(question)

    if user_answer == correct_answer:
        return True
    else:
        return False


def relational_questions():
    """
    Gives the user a computer science based question on relational operators, with answers being True or False
    :return: boolean
    """
    operators = ["==", "!=", ">", "<", ">=", "<="]
    chosen_operator = operators[random.randint(0, 5)]
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)
    correct_answer = None
    question = None

    if chosen_operator == "==":
        correct_answer = str(first_num == second_num)
        question = str(first_num) + " == " + str(second_num) + " "
    elif chosen_operator == "!=":
        correct_answer = str(first_num != second_num)
        question = str(first_num) + " != " + str(second_num) + " "
    elif chosen_operator == ">":
        correct_answer = str(first_num > second_num)
        question = str(first_num) + " > " + str(second_num) + " "
    elif chosen_operator == "<":
        correct_answer = str(first_num < second_num)
        question = str(first_num) + " < " + str(second_num) + " "
    elif chosen_operator == ">=":
        correct_answer = str(first_num >= second_num)
        question = str(first_num) + " >= " + str(second_num) + " "
    elif chosen_operator == "<=":
        correct_answer = str(first_num <= second_num)
        question = str(first_num) + " <= " + str(second_num) + " "

    user_answer = input(question)

    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False


def boolean_questions():
    """
    Gives the user a computer science based question on boolean operators, answers being either True or False
    :return: boolean
    """
    operators = ["and", "or", "not"]
    chosen_operator = operators[random.randint(0, 2)]
    first_num = random.randint(0, 20)
    second_num = random.randint(0, 20)
    third_num = random.randint(0, 20)
    fourth_num = random.randint(0, 20)
    correct_answer = None
    question = None

    if chosen_operator == "and":
        correct_answer = str((first_num == second_num) and (third_num == fourth_num))
        question = str(first_num) + " == " + str(second_num) + " and " + str(third_num) + " == " + str(fourth_num) + " "
    elif chosen_operator == "or":
        correct_answer = str((first_num >= second_num) or (third_num <= fourth_num))
        question = str(first_num) + " >= " + str(second_num) + " or " + str(third_num) + " <= " + str(fourth_num) + " "
    elif chosen_operator == "not":
        correct_answer = str(not first_num > fourth_num)
        question = "not " + str(first_num) + " > " + str(fourth_num) + " "

    user_answer = input(question)

    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False


#   Main Code
def main():
    """
    Main Code, getting name, printing introduction and rules of quiz, and doing random-generated questions
    Depending on score, certain messages are given, with special text art created for a perfect score
    """
#   Introduction to the quiz. Gets name for the farewell message later
    print("This is the Introduction to Computer Programming Quiz. You will be tested on the basic concepts learned.")
    name = input("Please tell us your name. ")
    print("You will be given 20 example programming commands, and must correctly identify what their outputs are.")
    print("Any answers for math problems that result in an answer that is not an integer should be rounded to the "
          "second decimal place.")
    print("Relational and Boolean questions will have an answer of True or False. Print questions will have answer of "
          "string.")

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

#   farewell message, as well as reminder for the user to tally their score for the quiz.
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


#   runs Main Code
if __name__ == "__main__":
    main()
