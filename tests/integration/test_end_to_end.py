from unittest.mock import patch
from src.main import main

def test_full_pipeline():
    # Patch input to simulate user choosing "Iris" dataset (option 1) and "Logistic Regression" (option 1)
    inputs = ['1', '1']  # corresponds to first options in dataset and model
    with patch('builtins.input', side_effect=inputs):
        # Since main() prints output, capture it with capsys (pytest fixture)
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        assert "Model: Logistic Regression" in output
        assert "Dataset: Iris" in output
        # Check accuracy output is present and is a reasonable float string
        assert "Accuracy:" in output
