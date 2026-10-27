import random

def string_checker(question, valid_ans=("yes", "no")):

    def yes_no(question):
        """Checks user response to a question for a yes/no answer and returns y/n."""
        while True:
            response = input(question).lower()
            if response == "yes" or response == "y":
                return "yes"
            elif response == "no" or response == "n":
                return "no"
            else:
                print("please enter yes / no")

    # Main routine
    # ask the user if they want instructions (check they say yes/no)

    # Display the instructions if the user wants to see them...

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

current_round = 0
score = 0

# Main Routine Starts here

rounds_lost = 0
rounds_won = 0
rounds_played = 0

# welcome the user to the game (heading)

current_round += 1

game_history = []
print("Math Multiplication Game")
print()

# Game loop starts here

want_instructions = ("yes, Yes, YES, y ")

input("Do you want to see the instructions? ")
if want_instructions == "yes":
    print('''
**** Instructions ****

To begin, choose the number of rounds (or press <enter> for 
infinite mode).

Then answer the equations given to you. You need to choose answers with either the numerals or word numbers, e.g. "1, 2, 3" "one, two, three"

Press <xxx> to end the game at anytime.

Good Luck!
    ''')

else:print()


# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

mode = num_rounds

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 999999999999999999999999999

while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n💽💽💽  Round {rounds_played + 1} (Infinite Mode)  💽💽💽"
    else:
        rounds_heading = f"\n💽💽💽  Round {rounds_played + 1} of {num_rounds} 💽💽💽"

    print(rounds_heading)

    first_number = random.randint(1, 12)
    second_number = random.randint(1, 12)

    correct_answer = first_number * second_number



    # Get the user's answer
    user_input = (
        input(f"What is {first_number} x {second_number}? ").strip().lower()
    )

    cps_list = f" {first_number} * {second_number} "

    result = eval(cps_list)

    comp_choice = random.choice(cps_list[:-1])

    # Validate and check the answer
    try:
        user_answer = int(user_input)
        if user_answer == correct_answer:
            print("✅ Correct! Nice job.")
            score += 1
            rounds_won += 1
        else:
            print(f"❌ Wrong. The correct answer was {correct_answer}.")
            rounds_lost += 1
    except:pass

    rounds_played += 1

# ask user if they want to see their gam history and output it if requested.
see_history = string_checker("\nDo you want to see your game history? ")
if see_history == "yes":
    for item in game_history:
        print(item)

    user_choice = input()

    first_number = random.randint(1, 12)
    second_number = random.randint(1, 12)

    correct_answer = first_number * second_number

    round_feedback = f"{first_number} * {second_number} = {user_choice} correct answer = {correct_answer}"
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"

    #  Game History / Statistics area

    if rounds_played > 0:
        # Caculate Statistics
        rounds_won = rounds_played - rounds_lost
        percent_won = rounds_won / rounds_played * 100
        percent_lost = rounds_lost / rounds_played * 100

        # Output Game Statistics
        print("📈📈📈 Game Statistics📉📉📉")
        print(f" Won: {percent_won:.2f} \t "
              f" Lost: {percent_lost:.2f} \t ")

    print()
    print("Thanks for playing.")