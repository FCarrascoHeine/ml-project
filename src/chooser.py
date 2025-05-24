class OptionChooser:
    """Creates objects used to get input from the user."""
    def __init__(self, options, prompt) -> None:
        self.options = options
        self.prompt = prompt

    def get_choice(self):
        # Return the user's choice
        print(self.prompt)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")
        return self._ask_user()

    def _ask_user(self):
        # Use the input function to let the user choose among options
        choice = input("Enter the number of your choice: ")
        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(self.options):
                return choice_idx
        except ValueError:
            pass
        print("Invalid choice, please try again.")
        return self._ask_user()
