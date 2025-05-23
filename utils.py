def display_options(options, prompt):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

def get_user_choice(num_options):
    choice = input("Enter the number of your choice: ")
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < num_options:
            return choice_idx
    except ValueError:
        pass
    print("Invalid choice, please try again.")
    return None

def choose_option(options, prompt):
    while True:
        display_options(options, prompt)
        choice_idx = get_user_choice(len(options))
        if choice_idx is not None:
            return choice_idx
