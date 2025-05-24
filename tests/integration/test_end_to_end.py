import sys
from io import StringIO
from unittest.mock import patch
from src.main import main
import re

def test_full_pipeline_accuracy() -> None:
    # Check the full pipeline by mocking user, training a model, and validating the result
    inputs = ['1', '1']  # Select 'Iris' and 'Logistic Regression'
    with patch('builtins.input', side_effect=inputs):
        captured_output = StringIO()
        sys.stdout = captured_output

        main()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

    assert "Model: Logistic Regression" in output
    assert "Dataset: Iris" in output
    assert "Accuracy:" in output

    match = re.search(r'Accuracy:\s*([0-9.]+)', output)
    assert match is not None, "Accuracy not found in output"
    accuracy = float(match.group(1))
    assert accuracy == 1.0
