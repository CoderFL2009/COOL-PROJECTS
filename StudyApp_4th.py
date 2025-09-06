import random
import textwrap
import sys
import keyboard


# ANSI escape codes for colors
GREEN = "\033[92m"  # Green text for terms
BLUE = "\033[94m"   # Blue text for definitions
RESET = "\033[0m"   # Reset to default




def load_vocabulary(filename):
    """Load vocabulary terms and definitions from a text file"""
    vocabulary = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify UTF-8 encoding
            for line in file:
                line = line.strip()
                if ' - ' in line:  # Check if the line contains the expected separator
                    term, definition = line.split(' - ', 1)
                    vocabulary[term] = definition
                else:
                    print(f"Skipping Invalid line: {line}")    # Informs about the invalid line
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. ")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
    return vocabulary




def study_mode(vocabulary):
    """Run the study mode of the app"""
    keys = list(vocabulary.keys())
    random.shuffle(keys)


    for term in keys:
        definition = vocabulary[term]
        wrapped_definition =textwrap.fill(definition, width=100)


        # Print the definition in blue
        print("\nDefinition:")
        print(f"{BLUE}{wrapped_definition}{RESET}")           # Change the definition to blue
        input("Press ENTER to reveal the term...")


        # Print the term in green
        print(f"\nTerm: {GREEN}{term}{RESET}")     # Change the term color to green
        print(f"\nPress the ESC key to exit or SPACE BAR to continue...")


        # Wait for the user input
        while True:
            if keyboard.is_pressed('esc'):                      # Check if ESC key is pressed
                print("Exiting Study Mode.")
                return
            if keyboard.is_pressed('space'):                     # Check if SPACE BAR is pressed
                break




def quiz_mode(vocabulary):
    """Run the quiz mode of the app"""
    keys = list(vocabulary.keys())
    random.shuffle(keys)


    correct_answers = 0
    total_questions = len(keys)


    for term in keys:
        definition = vocabulary[term]
        wrapped_definition = textwrap.fill(definition, width=100)


        # Print the definition in blue
        print("\nDefinition:")
        print(f"{BLUE}{wrapped_definition}{RESET}")  # Change the definition color to blue


        user_input = input("What is the term? (Type 'esc' to exit): ")
        if user_input.lower() == 'esc':
            break


        # Check the answer
        if user_input.strip().lower() == term.lower():
            correct_answers += 1
            print("Correct!")
        else:
            print(f"Incorrect! The correct term was: {term}")


    # Display results
    print(f"\nCorrect: {correct_answers} / {total_questions} ({(correct_answers / total_questions) * 100:.2f}%)")

    


def main():
    vocabulary = load_vocabulary('vocabulary2.txt')


    while True:
        print("\n1 for Study Mode, \n2 for Quiz Mode, \nESC to Exit")
        choice = input("Enter your choice: ")


        if choice == '1':
            study_mode(vocabulary)
        elif choice == '2':
            quiz_mode(vocabulary)
        elif choice.lower() == 'esc':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main()