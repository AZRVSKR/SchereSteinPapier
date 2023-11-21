import random

def get_user_choice():
    user_choice = input("Wähle Stein, Papier oder Schere: ").lower()
    while user_choice not in ['stein', 'papier', 'schere']:
        print("Ungültige Eingabe. Bitte wähle Stein, Papier oder Schere.")
        user_choice = input("Wähle Stein, Papier oder Schere: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['stein', 'papier', 'schere'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Unentschieden!"
    elif (
        (user_choice == 'stein' and computer_choice == 'schere') or
        (user_choice == 'papier' and computer_choice == 'stein') or
        (user_choice == 'schere' and computer_choice == 'papier')
    ):
        return "Du gewinnst!"
    else:
        return "Der Computer gewinnt!"

def play_game():
    print("Willkommen bei Stein-Papier-Schere!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Du hast {user_choice} gewählt.")
    print(f"Der Computer hat {computer_choice} gewählt.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()