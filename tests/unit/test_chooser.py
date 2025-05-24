from src.chooser import OptionChooser
from unittest.mock import patch

def test_get_choice_valid_input() -> None:
    # Check if a user's valid choice is processed correctly
    chooser = OptionChooser(["a", "b", "c"], "Choose an option:")
    with patch('builtins.input', return_value='2'):
        choice = chooser.get_choice()
    assert choice == 1  # index 1 corresponds to input '2'

def test_get_choice_invalid_then_valid_input() -> None:
    # Check if an invalid choice triggers an additional input requirement
    chooser = OptionChooser(["a", "b", "c"], "Choose an option:")
    inputs = ['xyz', '5', '1']
    with patch('builtins.input', side_effect=inputs):
        choice = chooser.get_choice()
    assert choice == 0  # index 0 corresponds to input '1'
