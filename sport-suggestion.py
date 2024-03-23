print("Welcome! Let's find the sport that suits you best.")

# Ask questions
print("Answer the following questions with 'yes' or 'no':")
valid_answers = ["yes", "no"]

# Function for input validation
def validate_input(question):
    while True:
        answer = input(question).lower()
        if answer in valid_answers:
            return answer
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

# Validate and get answers
answer1 = validate_input("Do you enjoy team sports? ")
answer2 = validate_input("Are you comfortable with physical contact? ")
answer3 = validate_input("Do you prefer indoor or outdoor activities? ")
answer4 = validate_input("Do you enjoy fast-paced games? ")
answer5 = validate_input("Are you interested in individual sports? ")


# Analyze answers and suggest a sport
if answer1.lower() == "yes" and answer2.lower() == "yes":
    print("You might enjoy football or rugby!")
elif answer1.lower() == "yes" and answer2.lower() == "no":
    print("You might enjoy basketball or tennis!")
elif answer3.lower() == "outdoor" and answer4.lower() == "yes":
    print("You might enjoy football or rugby!")
elif answer3.lower() == "outdoor" and answer5.lower() == "yes":
    print("You might enjoy tennis or swimming!")
else:
    print("You might enjoy basketball or swimming!")
