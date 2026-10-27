"""
Name: (put your name here)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    while True:
        letter = input("Give an single uppercase letter: ")

        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue

        if letter not in ["A", "B", "C"]:
            print("Error: You provided the wrong character.")
            continue

        return letter

def get_digit():
    while True:
        digit = input("Give an single number character: ")

        if not digit.isdigit():
            print("Error: your input should be only digits.")
            continue

        if digit not in ["1", "2", "3"]:
            print("Error: a single digit needs to be in [1,3].")
            continue

        return digit


def check_pattern(letter, digit, lst):
    print("Strings with the pattern:")

    for word in lst:
        found_letter = False
        found_pattern = False

        for char in word:
            if char == letter:
                found_letter = True
            elif char == digit and found_letter:
                found_pattern = True
                break

        if found_pattern:
            print(word, end=" ")

    print()



#  The function main is INCOMPLETE, you must finish it
# before you submit
def main():
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
               "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A",
               "2AA@", "1B1B", "333B", "1@CC", "3@@C", "333C"]

    letter = get_letter()
    digit = get_digit()

    check_pattern(letter, digit, st_list)

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()