"""data_structures/recursive_binary.py

This module implements a guessing game using a recursive function that
interacts with the user to pinpoint a number chosen by the user between 0 and
100. The game uses a binary search strategy, recursively narrowing down the
range based on user feedback whether the guessed number is too high, too low,
or correct. Enhancements include flexible input handling, guess count tracking,
and error handling.
"""

def find(low, high, guess_count=0):
    """
    Recursively guess a number within a specified range by asking the user if
    the guess is too high, too low, or correct.

    Args:
        low (int): The lower bound of the range within which the function is currently guessing.
        high (int): The upper bound of the range within which the function is currently guessing.
        guess_count (int): The current count of guesses made.

    The function repeatedly calculates the midpoint for the current range as
    the guess, and narrows the range based on the user's input. It accepts
    variations of 'lower', 'higher', and 'yes'. The recursion terminates when
    the user indicates that the guess is correct, and it reports the total
    number of guesses.
    """
    if low > high:
        print("Hmm, it seems there's a misunderstanding. Let's start over.")
        return

    mid = (high + low) // 2  # Calculate the midpoint for the current range
    answer = input(f'Is it {mid}? (lower/higher/yes): ').strip().lower()

    valid_lower = ['l', 'lower', 'low']
    valid_higher = ['h', 'higher', 'high']
    valid_yes = ['y', 'yes', 'correct', 'right']

    if any(ans == answer for ans in valid_yes):  # Base case: Guess is correct
        print(f'Got it! It took {guess_count + 1} guesses.')
    elif any(ans == answer for ans in valid_lower):
        if mid == low:  # Prevent infinite loop if mid equals low
            print("It seems there might be some confusion.")
            return
        find(low, mid - 1, guess_count + 1)  # Recursive case: Guess was too low
    elif any(ans == answer for ans in valid_higher):
        if mid == high:  # Prevent infinite loop if mid equals high
            print("It seems there might be some confusion.")
            return
        find(mid + 1, high, guess_count + 1)  # Recursive case: Guess was too high
    else:
        print("Please enter a valid response: 'lower', 'higher', or 'yes'.")
        find(low, high, guess_count)  # Recursive call with the same values if input is invalid

def search():
    """
    Initiates a number guessing game where the user thinks of a number between
    0 and 100, and the program attempts to guess it.

    The function sets up the game by printing instructions and then calls the
    recursive `find()` function to start the guessing process. This function
    includes a loop to allow repeated play until the user decides to quit. The
    game tracks the number of guesses taken to correctly guess the number.
    """
    print('Think of a number from 0 to 100.')
    print('Answer with:')
    print('   lower (your num is lower)')
    print('   higher (your num is higher)')
    print('   yes (guess is right).')

    while True:
        find(0, 100)  # Start the recursive guessing with the full range
        if input("Do you want to play again? (y/n): ").strip().lower() != 'y':
            print("Thanks for playing!")
            break
